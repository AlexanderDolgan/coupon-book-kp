"""Собирает готовые страницы из исходников в src/. Каждая страница — один самодостаточный файл:
фото, логотип, шрифты и библиотека QR встроены внутрь, интернет не нужен.

    python3 build.py

src/guest-book.html -> guest-book.html              книга гостя
src/admin.html      -> admin-coupons.html           админка: выданные купоны
                       admin-book-template.html     админка: шаблон книги
                       admin-coupon-template.html   админка: шаблон купона

Три страницы админки собираются из одного исходника: у каждой свой экран, меню ведёт
из файла в файл. Админка берёт шрифты, токены KP UI, типограф и рисунок QR из
src/guest-book.html (метки /*FONTS*/, /*TOKENS*/, /*TYPOJS*/, /*QRJS*/), чтобы страницы
не расходились.
"""
import base64
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'src')
SKELETON = ('<!doctype html><html lang="ru"><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
            'html{scroll-padding-top:env(safe-area-inset-top,0px)}body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#fff;color:#000}'
            'img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}</style></head><body>\n')
MIME = {'.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.svg': 'image/svg+xml'}
QR_TAG = '<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js"></script>'
PHOTO = r"'(img/[\w.-]+\.(?:jpg|jpeg|png))'"

# страницы админки: экран, имя файла, заголовок вкладки
ADMIN_PAGES = [
    ('issued', 'admin-coupons.html', 'Выданные купоны'),
    ('book', 'admin-book-template.html', 'Шаблон книги'),
    ('template', 'admin-coupon-template.html', 'Шаблон купона'),
]


def read(rel):
    with open(os.path.join(SRC, rel), encoding='utf-8') as f:
        return f.read()


def data_uri(rel):
    with open(os.path.join(SRC, rel), 'rb') as f:
        raw = f.read()
    return 'data:' + MIME[os.path.splitext(rel)[1].lower()] + ';base64,' + base64.b64encode(raw).decode('ascii')


def between(text, start, end, include_end=True):
    i = text.index(start)
    j = text.index(end, i)
    return text[i:j + (len(end) if include_end else 0)]


def embed(src, output, photos=None, head=''):
    """Встраивает библиотеку QR, фото и логотип; пишет готовый файл.
    photos — какие фото нужны странице (по умолчанию все, что встречаются в данных);
    head — скрипт с настройками страницы, ставится перед основным скриптом."""
    assert src.count(QR_TAG) == 1, 'QR script tag not found'
    lib = read(os.path.join('vendor', 'qrcode.min.js'))
    assert '</script' not in lib
    if photos is None:
        photos = sorted(set(re.findall(PHOTO, src)))
    # таблица «путь → data URI», её читает asset() на странице
    assets = '{' + ','.join('"' + p + '":"' + data_uri(p) + '"' for p in photos) + '}'
    src = src.replace(QR_TAG, '<script>' + lib + '</script>\n<script>window.__ASSETS=' + assets + ';' + head + '</script>')
    logo = 'src="img/logo.svg"'
    assert logo in src, 'logo not found'
    src = src.replace(logo, 'src="' + data_uri('img/logo.svg') + '"')
    # проверка: не осталось ни файлов рядом, ни подгрузки с других адресов
    left = re.findall(r'''(?:src|href)="(?!data:|#|tel:|mailto:|')[^"]*"''', src)   # ' — значение собирает скрипт
    assert not left, left
    assert not re.findall(r'url\((?!"?data:)[^)]*\)', src), 'external url() left'
    out = SKELETON + src + '\n</body></html>\n'
    with open(os.path.join(ROOT, output), 'w', encoding='utf-8') as f:
        f.write(out)
    print(output.ljust(28), str(round(len(out.encode('utf-8')) / 1024)).rjust(5), 'КБ,', len(photos), 'фото')


# ---------- книга гостя ----------
guest = read('guest-book.html')
embed(guest, 'guest-book.html')

# ---------- админка: три страницы из одного исходника ----------
admin = read('admin.html')
shared = {
    '/*FONTS*/': '\n'.join(line for line in guest.split('\n') if line.startswith('@font-face')),
    '/*TOKENS*/': between(guest, '/* KP UI 5.24 tokens', '* { box-sizing: border-box; }', include_end=False),
    '/*TYPOJS*/': between(guest, '  // типограф:', '  function typo(root) {', include_end=False) + between(guest, '  function typo(root) {', '\n  }\n'),
    '/*QRJS*/': between(guest, '  // Знак «Красной Поляны»', '  function qrSvg(text) {', include_end=False) + between(guest, '  function qrSvg(text) {', '\n  }\n'),
}
for mark, text in shared.items():
    assert admin.count(mark) == 1, mark
    assert text.strip(), mark
    admin = admin.replace(mark, text)

all_photos = sorted(set(re.findall(PHOTO, admin)))
needs = {
    'issued': [],                                                                       # в списке купонов фото нет
    'template': sorted(set(re.findall(PHOTO, between(admin, '  const T = {', '\n  };')))),  # фото одного купона
    'book': all_photos,                                                                 # обложка и каталог купонов
}
files = {page: name for page, name, _ in ADMIN_PAGES}
title = '<title>Админка купонной книги</title>'
assert admin.count(title) == 1
for page, name, label in ADMIN_PAGES:
    head = 'window.__PAGE=' + json.dumps(page) + ';window.__FILES=' + json.dumps(files) + ';'
    embed(admin.replace(title, '<title>' + label + ' · админка купонной книги</title>'), name, photos=needs[page], head=head)

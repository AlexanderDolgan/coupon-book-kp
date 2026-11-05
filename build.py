"""Собирает самодостаточные HTML-файлы: фото, логотип, шрифты и библиотека QR встроены внутрь,
внешних файлов и ссылок на CDN не остаётся.

    python3 build.py

Книга гостя:  prototype.html -> coupon-book-prototype.html, publish/index.html
Админка:      admin.html     -> coupon-book-admin.html,     publish-admin/index.html

Админка берёт шрифты, токены KP UI, типограф и рисунок QR из prototype.html
(метки /*FONTS*/, /*TOKENS*/, /*TYPOJS*/, /*QRJS*/), чтобы два прототипа не расходились.
"""
import base64
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
SKELETON = ('<!doctype html><html lang="ru"><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
            'html{scroll-padding-top:env(safe-area-inset-top,0px)}body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#fff;color:#000}'
            'img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}</style></head><body>\n')
MIME = {'.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.svg': 'image/svg+xml'}
QR_TAG = '<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcode-generator/1.4.4/qrcode.min.js"></script>'


def read(rel):
    with open(os.path.join(ROOT, rel), encoding='utf-8') as f:
        return f.read()


def data_uri(rel):
    with open(os.path.join(ROOT, rel), 'rb') as f:
        raw = f.read()
    return 'data:' + MIME[os.path.splitext(rel)[1].lower()] + ';base64,' + base64.b64encode(raw).decode('ascii')


def between(text, start, end, include_end=True):
    i = text.index(start)
    j = text.index(end, i)
    return text[i:j + (len(end) if include_end else 0)]


def embed(src, outputs):
    """Встраивает библиотеку QR, фото из данных и логотип; пишет готовые файлы."""
    assert src.count(QR_TAG) == 1, 'QR script tag not found'
    lib = read(os.path.join('vendor', 'qrcode.min.js'))
    assert '</script' not in lib
    # фото из данных: таблица «путь → data URI», её читает asset() на странице
    photos = sorted(set(re.findall(r"'(img/[\w.-]+\.(?:jpg|jpeg|png))'", src)))
    assets = '{' + ','.join('"' + p + '":"' + data_uri(p) + '"' for p in photos) + '}'
    src = src.replace(QR_TAG, '<script>' + lib + '</script>\n<script>window.__ASSETS=' + assets + ';</script>')
    logo = 'src="img/logo.svg"'
    assert logo in src, 'logo not found'
    src = src.replace(logo, 'src="' + data_uri('img/logo.svg') + '"')
    # проверка: не осталось ни файлов рядом, ни подгрузки с других адресов
    left = re.findall(r'''(?:src|href)="(?!data:|#|tel:|mailto:|')[^"]*"''', src)   # ' — значение собирает скрипт
    assert not left, left
    assert not re.findall(r'url\((?!"?data:)[^)]*\)', src), 'external url() left'
    out = SKELETON + src + '\n</body></html>\n'
    for name in outputs:
        path = os.path.join(ROOT, name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(out)
    print(outputs[0], len(out.encode('utf-8')), 'bytes;', len(photos), 'photos')


proto = read('prototype.html')
embed(proto, ['coupon-book-prototype.html', os.path.join('publish', 'index.html')])

admin = read('admin.html')
parts = {
    '/*FONTS*/': '\n'.join(line for line in proto.split('\n') if line.startswith('@font-face')),
    '/*TOKENS*/': between(proto, '/* KP UI 5.24 tokens', '* { box-sizing: border-box; }', include_end=False),
    '/*TYPOJS*/': between(proto, '  // типограф:', '  function typo(root) {', include_end=False) + between(proto, '  function typo(root) {', '\n  }\n'),
    '/*QRJS*/': between(proto, '  // Знак «Красной Поляны»', '  function qrSvg(text) {', include_end=False) + between(proto, '  function qrSvg(text) {', '\n  }\n'),
}
for mark, text in parts.items():
    assert admin.count(mark) == 1, mark
    assert text.strip(), mark
    admin = admin.replace(mark, text)
embed(admin, ['coupon-book-admin.html', os.path.join('publish-admin', 'index.html')])

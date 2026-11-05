# KP UI 5.24 — переменные и токены

Источник: Figma `UI 5.24 - KP` (p3n9vFOlcUIkMenRCgXmYc). База — Ant Design System for Figma, кастомизированная под Красную Поляну (префикс `kp*`).
Коллекции: **1. Colors** (278, режимы Light/Dark), **2. Dimensions** (81, Large/Default/Compact), **3. Typography** (27, Large/Default/Compact), **4. Components** (1944 — не выгружал, компонентные алиасы). Плюс 20 текстовых стилей и 10 стилей эффектов.

Ниже — только то, что нужно для редизайна Купонной книги. Значения — Light. Dark — в `kp-ui-tokens.json`.

## Палитры бренда

| Шаг | kpBrand (красный) | kpBrandSecondary (сине-серый) |
|---|---|---|
| 0 | — | `#ffffff` |
| 1 | `#feedec` | `#f4f6fb` |
| 2 | `#fddbd9` | `#eaeef6` |
| 3 | `#fbb9b6` | `#d3d8e5` |
| 4 | `#fa908c` | `#b9c0d0` |
| 5 | `#fc5e54` | `#8b92a7` |
| 6 | `#e63621` ← primary | `#6a728a` |
| 7 | `#b82918` | `#565c71` |
| 8 | `#911a0d` | `#3e4252` ← text |
| 9 | `#651208` | `#353a48` |
| 10 | `#3c0703` | `#2c313f` |
| 11 | — | `#1d202b` |

Доп. фоны для тегов `kpExternalColors/1–4`: `#fff0f6` `#e6f4ff` `#fffbe6` `#f6ffed`.

## Семантические цвета (Light)

**Primary / Link**
- `colorPrimary` `#e63621` (kpBrand/6) · hover `#fc5e54` (5) · active `#b82918` (7)
- `colorPrimaryBg` `#feedec` · `colorPrimaryBgHover` `#fddbd9` · `colorPrimaryBorder` `#fbb9b6` · `colorPrimaryBorderHover` `#fa908c`
- `colorPrimaryText` `#e63621` · hover `#fc5e54` · active `#b82918`
- `colorLink` = colorPrimary, hover/active = primary hover/active

**Text**
- `colorText` `#3e4252` (sec/8) · `colorTextHeading` = colorText
- `colorTextSecondary` `#6a728a` (sec/6) · `colorTextLabel` = secondary · `colorTextHeadingSecondary` = secondary
- `colorTextTertiary` `#8b92a7` (sec/5) · `colorTextDescription` = tertiary · `colorTextPlaceholder` = tertiary
- `colorTextQuaternary` `#b9c0d0` (sec/4) · `colorTextDisabled` = quaternary
- `colorTextLightSolid` `#ffffff` · `kpColorTextDarkSolid` `#3e4252` · `kpColorTextInvert` `#ffffff`

**Icon**
- `colorIcon` `#8b92a7` · `colorIconHover` `#3e4252` · `kpColorIconSecondary` `#6a728a` · `kpColorIconBrand` `#e63621`
- `kpColorIconSolidLight` `#ffffff` · `kpColorIconSolidDark` `#3e4252`

**Background**
- `colorBgBase` / `colorBgContainer` / `colorBgElevated` / `kpColorBgHeader` `#ffffff`
- `colorBgLayout` `#eaeef6` (sec/2) · `kpColorBgContainerSecondary` `#f4f6fb` (sec/1)
- `kpColorBgContainerSolidDark` / `kpColorBgLayoutSolidDark` `#1d202b` (sec/11)
- `colorBgSolid` `#2c313f` (sec/10) · hover `#3e4252` · active `#353a48` · `colorBgSpotlight` `#3e4252`
- `kpColorBgContainerPrimary` `#e63621`
- `colorBgMask` `#00000073` · `kpColorBgMask2` `#0000004d` · `kpColorBgMask3` `#05070da6` · `kpColorBgContainerTransparent` `#ffffffb2`
- `colorBgContainerDisabled` = colorFillTertiary · `colorBgTextHover` = colorFillSecondary · `colorBgTextActive` = colorFill

**Border**
- `colorBorder` `#b9c0d0` (sec/4) · `colorBorderSecondary` `#d3d8e5` (sec/3) · `colorSplit` `#434a621f`
- `kpColorBorderBrand` `#e63621` · `kpColorBorderBrandHover` `#fc5e54` · `kpColorBorderTransparent` прозрачный

**Fill (полупрозрачные, база #434a62)**
- `colorFill` `#434a624d` (30%) · `colorFillSecondary` `#434a621f` (12%) · `colorFillTertiary` `#434a6214` (8%) · `colorFillQuaternary` `#434a620a` (4%)
- `colorFillAlter` = quaternary · `colorFillAlterSolid` `#fafafa` · `kpColorFillAlterSecondary` `#f5f7fbc2` · `colorFillContent` = secondary · `colorFillContentHover` = colorFill

**Статусы**

| | main | bg | bgHover | border | borderHover | hover | active | text |
|---|---|---|---|---|---|---|---|---|
| Success | `#52c41a` | `#f6ffed` | `#d9f7be` | `#b7eb8f` | `#95de64` | `#95de64` | `#389e0d` | `#52c41a` |
| Warning | `#faad14` | `#fffbe6` | `#fff1b8` | `#ffe58f` | `#ffd666` | `#ffd666` | `#d48806` | `#faad14` |
| Error | `#ff4d4f` | `#fff2f0` | `#fff1f0` | `#ffccc7` | `#ffa39e` | `#ff7875` | `#d9363e` | `#ff4d4f` |
| Info | `#1677ff` | `#e6f4ff` | `#bae0ff` | `#91caff` | `#69b1ff` | `#69b1ff` | `#0958d9` | `#1677ff` |

**Control**
- `controlItemBgActive` = colorPrimaryBg `#feedec` · `controlItemBgActiveHover` `#fddbd9` · `controlItemBgHover` = colorFillQuaternary
- `controlOutline` `#e636211a` · `colorErrorOutline` `#ff26060f` · `colorWarningOutline` `#ffd7051a`

Базовые палитры Ant (Blue, Cyan, Geekblue, Gold, Green, Lime, Magenta, Orange, Pink, Purple, Red, Volcano, Yellow — по 10 шагов) оставлены стандартными, см. JSON.

## Размеры (Large / Default / Compact)

**Size/Base**: XXS 4 · XS 8 · SM 12 · size 16 · MS 16 · MD 20/20/16 · LG 24/24/20 · XL 32/32/28 · XXL 48/40/32 · kpXXXL 80/72/40
**Size/Height**: controlHeight 40 · LG 56 · SM 32/32/28 · XS 24/20/20
**Line width**: lineWidth 1 · bold 2 · focus 4 · controlOutlineWidth 0
**Space**: margin*/padding* = алиасы на Size/Base (marginXS=8, margin=16, marginLG=24, marginXL=32, marginXXL=48/40/32, kpMarginXXXL=80/72/40)
**Padding content**: horizontal 16 · horizontalLG 24 · horizontalSM 16 · vertical 12 · verticalLG 16 · verticalSM 8 · controlPaddingHorizontal 12 · SM 8
**Border Radius**: XS 2 · SM 4 · borderRadius 8 · kpL 12 · LG 16 · kpXL 24/24/16 · kpXXL 32/32/24
**Screens**: XS 480 · SM 576 · MD 768 · LG 992 · XL 1200 · XXL 1600

**kpLayout**

| токен | Large | Default | Compact |
|---|---|---|---|
| kpGutterRow | 24 | 24 | 16 |
| kpColumn | 12 | 8 | 4 |
| kpLayoutMargin | 80 | 24 | 16 |
| kpLayoutMarginL | 189 | 141 | 16 |
| kpLayoutSectionMargin | 96 | 64 | 40 |
| kpLayoutSectionRowMargin | 64 | 40 | 32 |
| kpLayoutSectionRowMarginM | 32 | 32 | 24 |
| kpLayoutMainMargin | 40 | 40 | 40 |
| kpLayoutRowMaxWidthSmall | 628 | 444 | 328 |
| kpLayoutRowMaxWidthMedium | 846 | 678 | 328 |
| kpLayoutRowMaxWidthLarge | 1062 | 912 | 328 |

## Типографика (Large / Default / Compact)

- Шрифты: `fontFamily` **Halvar Mittelschrift** · `fontFamilyCode` Halvar Engschrift · `kpFontFamilyNumber` Halvar Breitschrift
- Веса: kpLight 300 · Normal 400 · Strong 500 · Bold 700
- fontSizeSM 12 / lh 20/18/16 · fontSize 14 / lh 22/22/19 · fontSizeLG 16 / lh 24/23/22 · fontSizeXL 20/18/18 · kpFontSizeXXL 24/22/19 · fontSizeIcon 20/20/16
- H1 40/34/30, lh 48/41/36 · H2 32/27/24, lh 38/32/29 · H3 24/20/20, lh 28/25/23 · H4 20/19/18, lh 23/22/20 · H5 20/17/16, lh 23/20/18
- kpParagraphSpacing 16

**Текстовые стили** (все Halvar Mittelschrift): Text SM 12/20, Text Base 14/22, Text LG 16/24 — каждый в вариантах Normal (Regular), Strong (Medium), Underline, Delete, Italic. Heading/1 40/48, /2 32/38, /3 24/28, /4 20/23, /5 20/23 — Medium.

## Тени (effect styles)

- `boxShadow` = `boxShadowSecondary`: 0 9 28 8 #0000000d; 0 3 6 -4 #0000001f; 0 6 16 0 #00000014
- `boxShadowTertiary`: 0 2 4 0 #00000005; 0 1 6 -1 #00000005; 0 1 2 0 #00000008
- Button: primaryShadow #e636211a · defaultShadow #434a620a · dangerShadow #ff26060f (все 0 0 0 0 — это outline)
- Input: activeShadow #e636211a · errorActiveShadow #ff26060f · warningActiveShadow #ffd7051a
- Switch/handleShadow 0 2 4 #00230b33

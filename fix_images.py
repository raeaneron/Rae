import re

with open(r'd:\web apps\Personal Website\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (r'const IMG_CASTLE = "data:image/webp;base64,[^"]+"', 'const IMG_CASTLE  = "Art/image (4).png"'),
    (r'const IMG_LIBRARY = "data:image/webp;base64,[^"]+"', 'const IMG_LIBRARY = "Art/image (6).png"'),
    (r'const IMG_FOREST = "data:image/webp;base64,[^"]+"', 'const IMG_FOREST  = "Art/image (7).png"'),
    (r'const IMG_ALLEY = "data:image/webp;base64,[^"]+"', 'const IMG_ALLEY   = "Art/image (8).png"'),
    (r'const IMG_PORTAL = "data:image/webp;base64,[^"]+"', 'const IMG_PORTAL  = "Art/image (9).png"'),
    (r'const IMG_WIZARD = "data:image/webp;base64,[^"]+"', 'const IMG_WIZARD  = "Art/image.png"'),
    (r'const IMG_RANGER = "data:image/webp;base64,[^"]+"', 'const IMG_RANGER  = "Art/image (1).png"'),
    (r'const IMG_ROGUE = "data:image/webp;base64,[^"]+"', 'const IMG_ROGUE   = "Art/image (2).png"'),
    (r'const IMG_BATMAN = "data:image/webp;base64,[^"]+"', 'const IMG_BATMAN  = "Art/image (3).png"'),
    (r'const IMG_CURLY = "data:image/webp;base64,[^"]+"', 'const IMG_CURLY   = "Art/Pixel Art Character with Curly Hair.png"'),
]

for pattern, replacement in replacements:
    content = re.sub(pattern, replacement, content)

with open(r'd:\web apps\Personal Website\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done! Total lines:', content.count('\n'))

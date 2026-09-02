#!/usr/bin/env python3
"""Gera proplan-science-system-standalone.html com todos os assets embutidos (data URI).
As fotos JPG são recomprimidas (máx. 1280 px, q78) só nesta versão; os originais em assets/ ficam intactos."""
import re, base64, os, mimetypes, io
from PIL import Image
src = open('index.html', encoding='utf-8').read()
def uri(p):
    if not os.path.exists(p): return None
    mt = mimetypes.guess_type(p)[0] or 'application/octet-stream'
    data = open(p, 'rb').read()
    if mt == 'image/jpeg':
        im = Image.open(p).convert('RGB'); im.thumbnail((1280, 1280))
        buf = io.BytesIO(); im.save(buf, 'JPEG', quality=78, optimize=True); data = buf.getvalue()
    return 'data:' + mt + ';base64,' + base64.b64encode(data).decode()
def attr(m):
    d = uri(m.group(2)); return m.group(0) if d is None else f'{m.group(1)}="{d}"'
def js(m):
    d = uri(m.group(1)); return m.group(0) if d is None else f"'{d}'"
out = re.sub(r'(src|href)="(assets/[^"]+)"', attr, src)
out = re.sub(r"'(assets/[^']+)'", js, out)
open('proplan-science-system-standalone.html', 'w', encoding='utf-8').write(out)
print('standalone', len(out) // 1024, 'KB')

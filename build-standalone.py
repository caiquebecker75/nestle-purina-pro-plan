#!/usr/bin/env python3
"""Gera proplan-science-system-standalone.html com todos os assets embutidos (data URI)."""
import re, base64, os, mimetypes
src = open('index.html', encoding='utf-8').read()
def uri(p):
    if not os.path.exists(p): return None
    mt = mimetypes.guess_type(p)[0] or 'application/octet-stream'
    return 'data:' + mt + ';base64,' + base64.b64encode(open(p, 'rb').read()).decode()
def attr(m):
    d = uri(m.group(2)); return m.group(0) if d is None else f'{m.group(1)}="{d}"'
def js(m):
    d = uri(m.group(1)); return m.group(0) if d is None else f"'{d}'"
out = re.sub(r'(src|href)="(assets/[^"]+)"', attr, src)
out = re.sub(r"'(assets/[^']+)'", js, out)
open('proplan-science-system-standalone.html', 'w', encoding='utf-8').write(out)
print('standalone', len(out) // 1024, 'KB')

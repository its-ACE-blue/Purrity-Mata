#!/usr/bin/env python3
"""Run once with internet: python get_offline_assets.py
Downloads MathJax 3 into vendor/mathjax/es5 and the Mali font into fonts/,
so Purrity Mata works fully offline afterwards."""
import io, json, os, re, tarfile, urllib.request
here = os.path.dirname(os.path.abspath(__file__))
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36'}
def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()

print('Downloading MathJax...')
meta = json.loads(get('https://registry.npmjs.org/mathjax/3.2.2'))
with tarfile.open(fileobj=io.BytesIO(get(meta['dist']['tarball']))) as t:
    for mem in t.getmembers():
        if mem.isfile() and mem.name.startswith('package/es5/'):
            dest = os.path.join(here, 'vendor', 'mathjax', mem.name[len('package/'):])
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, 'wb') as f: f.write(t.extractfile(mem).read())

print('Downloading Mali font...')
css = get('https://fonts.googleapis.com/css2?family=Mali:wght@400;500;600;700&display=swap').decode()
os.makedirs(os.path.join(here, 'fonts'), exist_ok=True)
def local(m):
    name = m.group(1).split('/')[-1]
    with open(os.path.join(here, 'fonts', name), 'wb') as f: f.write(get(m.group(1)))
    return 'url(%s)' % name
css = re.sub(r'url\((https://[^)]+)\)', local, css)
with open(os.path.join(here, 'fonts', 'mali.css'), 'w', encoding='utf-8') as f: f.write(css)
print('Done. Reload index.html.')

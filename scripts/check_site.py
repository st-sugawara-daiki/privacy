"""Check static links and fragments; --release rejects unresolved publication markers."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys

ROOT = Path(__file__).resolve().parents[1] / 'site'
class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.ids, self.links, self.blockers = set(), [], 0
        self.lang = self.viewport = False
        self.feed(source)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, 'duplicate id'
            self.ids.add(a['id'])
        self.blockers += 'data-publish-blocker' in a
        if tag == 'html': self.lang = a.get('lang') == 'ja'
        if tag == 'meta' and a.get('name') == 'viewport': self.viewport = True
        for key in ('href', 'src'):
            if key in a: self.links.append(a[key])

pages = {p.resolve(): Page(p.read_text()) for p in ROOT.rglob('*.html')}
errors = []
for path, page in pages.items():
    if not page.lang or not page.viewport: errors.append(f'{path}: missing lang/viewport')
    if '--release' in sys.argv and page.blockers: errors.append(f'{path}: {page.blockers} publication blockers')
    for href in page.links:
        url = urlsplit(href)
        if url.scheme or url.netloc: continue
        if url.path.startswith('/'):
            errors.append(f'{path}: absolute link breaks project Pages: {href}')
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        if target.is_dir(): target /= 'index.html'
        if not target.is_relative_to(ROOT) or not target.exists(): errors.append(f'{path}: broken link {href}')
        elif url.fragment and (target not in pages or unquote(url.fragment) not in pages[target].ids): errors.append(f'{path}: broken fragment {href}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'OK: {len(pages)} HTML pages; local links, fragments, Japanese language and viewport checked.')
print(f'Publication markers: {sum(p.blockers for p in pages.values())}')

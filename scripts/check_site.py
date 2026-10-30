from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

root = Path(__file__).resolve().parents[1] / "template"

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in {"src", "href"} and value:
                self.links.append(value)

parser = Links()
parser.feed((root / "index.html").read_text(encoding="utf-8-sig"))
errors = []
for link in parser.links:
    url = urlsplit(link)
    if url.scheme or url.netloc or not url.path:
        continue
    path = root / unquote(url.path)
    if not path.exists():
        errors.append(f"Missing local target: {link}")
    elif any(part not in {entry.name for entry in path.parent.iterdir()} for part in [path.name]):
        errors.append(f"Incorrect filename case: {link}")
if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)
print("Main-page local links and assets passed.")

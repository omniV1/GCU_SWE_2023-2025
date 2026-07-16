"""
Amazon Lab local server (NeetCode-style UI).

Run:
  cd SummerPractice/python/practice/amazon_lab
  python serve.py

Then open http://127.0.0.1:8765
"""

from __future__ import annotations

import json
import webbrowser
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
PORT = 8765


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self.path = "/static/index.html"
        return super().do_GET()

    def log_message(self, fmt: str, *args) -> None:
        print("[%s] %s" % (self.log_date_time_string(), fmt % args))


def main() -> None:
    problems = ROOT / "data" / "problems.json"
    if not problems.exists():
        print("problems.json missing — running seed_problems.py…")
        import seed_problems

        seed_problems.main()

    data = json.loads(problems.read_text(encoding="utf-8"))
    print(f"Amazon Lab — {data['meta']['count']} problems loaded (goal {data['meta']['goal']})")
    print(f"Open http://127.0.0.1:{PORT}")
    httpd = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    try:
        webbrowser.open(f"http://127.0.0.1:{PORT}")
    except Exception:
        pass
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()

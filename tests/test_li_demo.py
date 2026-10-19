from html.parser import HTMLParser
from pathlib import Path
import unittest


class ListParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.items = {"ul": 0, "ol": 0, "dt": 0, "dd": 0}

    def handle_starttag(self, tag, attrs):
        if tag == "li" and self.stack and self.stack[-1] in ("ul", "ol"):
            self.items[self.stack[-1]] += 1
        if tag in ("dt", "dd"):
            self.items[tag] += 1
        if tag in ("ul", "ol", "dl", "li", "dt", "dd"):
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()


class ChrysanthemumPageTest(unittest.TestCase):
    def test_page_contains_three_kinds_of_lists(self):
        page = Path(__file__).resolve().parents[1] / "character0/261019/liDemo copy.html"
        parser = ListParser()
        parser.feed(page.read_text(encoding="utf-8"))
        for kind, count in parser.items.items():
            with self.subTest(kind=kind):
                self.assertGreater(count, 0, f"缺少 {kind} 列表条目")
        self.assertEqual(parser.items["dt"], parser.items["dd"])


if __name__ == "__main__":
    unittest.main()

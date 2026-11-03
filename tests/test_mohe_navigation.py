from html.parser import HTMLParser
from pathlib import Path
import unittest


class PageParser(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.links = []
        self.images = []
        self.text = []
        self.current_link = None
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a":
            self.current_link = [attrs.get("href", ""), ""]
        if tag == "img":
            self.images.append(attrs)

    def handle_data(self, data):
        self.text.append(data)
        if self.current_link is not None:
            self.current_link[1] += data

    def handle_endtag(self, tag):
        if tag == "a" and self.current_link is not None:
            self.links.append(self.current_link)
            self.current_link = None


class MoheNavigationTest(unittest.TestCase):
    root = Path(__file__).resolve().parents[1] / "assignments/261103"

    def test_popular_mohe_links_to_detail_page(self):
        home = self.root / "MH/index.html"
        links = [href for href, text in PageParser(home).links if text.strip() == "墨荷"]
        self.assertEqual(len(links), 1)
        self.assertEqual((home.parent / links[0]).resolve(), self.root / "index.html")

    def test_both_return_links_lead_to_homepage(self):
        detail = self.root / "index.html"
        links = PageParser(detail).links
        for label in ("← 返回品种简介首页", "返回首页 · 查看品种简介"):
            with self.subTest(label=label):
                targets = [href for href, text in links if text.strip() == label]
                self.assertEqual(len(targets), 1)
                self.assertEqual((detail.parent / targets[0]).resolve(), self.root / "MH/index.html")

    def test_detail_has_reference_content_and_accessible_image(self):
        page = PageParser(self.root / "index.html")
        for heading in ("墨荷", "品种档案", "品种简介", "观赏提示"):
            self.assertIn(heading, "".join(page.text))
        self.assertEqual(len(page.images), 1)
        self.assertEqual(page.images[0]["src"], "https://images.unsplash.com/photo-1508610048659-a06b669e3321?w=600&h=400&fit=crop&auto=format")
        self.assertTrue(page.images[0].get("alt"))

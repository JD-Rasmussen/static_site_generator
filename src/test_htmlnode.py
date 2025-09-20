import unittest

from src.htmlnode import HTMLNode

#self, tag = None, value = None, children = None, props = None

class TestHTMLNode(unittest.TestCase):

    def test_props_None(self):
        node = HTMLNode(props = None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_something(self):
        node = HTMLNode(props = {"href": "https://google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com" target="_blank"')

    def test_repr_includes_fields(self):
        node = HTMLNode(tag="a", value="link", children=[], props={"href": "https://x.com"})
        self.assertEqual(repr(node), 'HTMLNode(tag=a, value=link, children=[], props={\'href\': \'https://x.com\'})')

if __name__ == "__main__":
    unittest.main()
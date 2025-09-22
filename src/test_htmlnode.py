import unittest

from src.htmlnode import HTMLNode, LeafNode

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


class TestLeafNode(unittest.TestCase):
    def test_leaf_plain_text(self):
        node = LeafNode("hello")
        self.assertEqual(node.to_html(), "hello")

    def test_leaf_p_tag(self):
        node = LeafNode("Hello, world!", tag="p")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_with_props(self):
        node = LeafNode("Click me!", tag="a", props={"href": "https://x.y", "target": "_blank"})
        html = node.to_html()
        self.assertTrue(html.startswith("<a "))
        self.assertIn('href="https://x.y"', html)
        self.assertIn('target="_blank"', html)
        self.assertTrue(html.endswith(">Click me!</a>"))

    def test_leaf_value_required(self):
        with self.assertRaises(ValueError):
            LeafNode(None, tag="p")
   


if __name__ == "__main__":
    unittest.main()
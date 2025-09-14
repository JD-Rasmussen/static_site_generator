import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("this is a url test", TextType.ITALIC)
        node2 = TextNode("this is a url test", TextType.ITALIC, "http://127.0.0.1:8888")
        self.assertNotEqual(node, node2)

    def test_neq2(self):
        node = TextNode("this is a textType test", TextType.ITALIC)
        node2 = TextNode("this is a textType test", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_neq3(self):
        node = TextNode("This is not a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()



import unittest

from src.extract_markdowns import extract_markdown_images, extract_markdown_links, markdown_to_blocks

class TestSplit_node_delimiter(unittest.TestCase):


    def test_images_multiple(self):
        text = "![a](u1) text ![b](u2)"
        self.assertListEqual([("a", "u1"), ("b", "u2")], extract_markdown_images(text))

    def test_images_none(self):
        text = "no images here"
        self.assertListEqual([], extract_markdown_images(text))

    def test_links_multiple(self):
        text = "[one](u1) and [two](u2)"
        self.assertListEqual([("one", "u1"), ("two", "u2")], extract_markdown_links(text))

    def test_links_ignore_images(self):
        text = "![pic](img.png) and [site](https://x.y)"
        self.assertListEqual([("pic", "img.png")], extract_markdown_images(text))
        self.assertListEqual([("site", "https://x.y")], extract_markdown_links(text))
    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )




import unittest

from src.markdown_to_html_node import markdown_to_html_node, strip_prefix_once

class Test_Markdown_to_html_node(unittest.TestCase):



    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading_h2(self):
        md = "## A title\n"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><h2>A title</h2></div>")

    def test_quote_simple(self):
        md = "> line one\n> line two\n"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><blockquote>line one line two</blockquote></div>")

    def test_unordered_list(self):
        md = "- a\n- b\n- c\n"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><ul><li>a</li><li>b</li><li>c</li></ul></div>")

    def test_ordered_list(self):
        md = "1. first\n2. second\n3. third\n"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><ol><li>first</li><li>second</li><li>third</li></ol></div>")


    def test_mixed_blocks(self):
        md = """# T
        
    - x
    - y

    > q
    """
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><h1>T</h1><ul><li>x</li><li>y</li></ul><blockquote>q</blockquote></div>",
        )

    def test_inline_in_heading_paragraph(self):
        md = "# hi **there**\n\nsome _it_ and `code`\n"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><h1>hi <b>there</b></h1><p>some <i>it</i> and <code>code</code></p></div>",
        )
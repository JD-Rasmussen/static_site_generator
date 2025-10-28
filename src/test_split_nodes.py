import unittest

from src.textnode import TextNode, TextType
from src.split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

class TestSplit_node_delimiter(unittest.TestCase):


    def test_No_Delimiter(self):
            node = TextNode("This is a text node", TextType.TEXT)
            split_node = split_nodes_delimiter([node], "`", TextType.CODE)
            self.assertEqual(split_node[0], node)
            self.assertEqual(len(split_node),1)
            self.assertEqual(split_node[0].text, "This is a text node")
            self.assertEqual(split_node[0].text_type, TextType.TEXT)
    
    def test_one_Delimiter(self):
        node = TextNode("This is a **bold** text node", TextType.TEXT)
        split_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(split_node),3)
        self.assertEqual(split_node[0].text, "This is a ")
        self.assertEqual(split_node[0].text_type, TextType.TEXT)
        self.assertEqual(split_node[1].text, "bold")
        self.assertEqual(split_node[1].text_type, TextType.BOLD)
        self.assertEqual(split_node[2].text, " text node")
        self.assertEqual(split_node[2].text_type, TextType.TEXT)

    def test_two_Delimiter(self):
        node = TextNode("This is an _italic_ text _node_ multi split", TextType.TEXT)
        split_node = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(len(split_node),5)
        self.assertEqual(split_node[0].text, "This is an ")
        self.assertEqual(split_node[0].text_type, TextType.TEXT)
        self.assertEqual(split_node[1].text, "italic")
        self.assertEqual(split_node[1].text_type, TextType.ITALIC)
        self.assertEqual(split_node[2].text, " text ")
        self.assertEqual(split_node[2].text_type, TextType.TEXT)
        self.assertEqual(split_node[3].text, "node")
        self.assertEqual(split_node[3].text_type, TextType.ITALIC)
        self.assertEqual(split_node[4].text, " multi split")
        self.assertEqual(split_node[4].text_type, TextType.TEXT)        

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_link(self):
        node = TextNode(
            "This is text with a [link](https://www.boot.dev) and another [second link](https://www.google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://www.google.com"
                ),
            ],
            new_nodes,
        )






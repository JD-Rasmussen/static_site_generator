

from src.htmlnode import HTMLNode, LeafNode, ParentNode
from src.textnode import TextNode, TextType
from src.textnode_to_htmlnode import text_node_to_html_node

[
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("bolded phrase", TextType.BOLD),
    TextNode(" in the middle", TextType.TEXT),
]


def split_nodes_delimiter(old_nodes, delimiter, text_type):
        
    for node in old_nodes:
        





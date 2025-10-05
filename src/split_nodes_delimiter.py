

from src.htmlnode import HTMLNode, LeafNode, ParentNode
from src.textnode import TextNode, TextType
from src.textnode_to_htmlnode import text_node_to_html_node

#[
#    TextNode("This is text with a ", TextType.TEXT),
#    TextNode("bolded phrase", TextType.BOLD),
#    TextNode(" in the middle", TextType.TEXT),
#]


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []    
    for node in old_nodes:
        if node.text_type == text_type.TEXT:
            before = TextNode("", text_type.TEXT, node.url)
            middle = TextNode("", text_type)
            after = TextNode("", text_type.TEXT, node.url)
            if delimiter in node.text:
                before.text, secondtext = node.text.split(delimiter, 1)
                result.append(before)
                    if delimiter not in secondtext:
                        raise Exception ("missing end delimiter")
                middle.text, after.text = secondtext.split(delimiter,1)   
                result.append(middle)
                result.append(after)
            else:
                result.append(node)








from src.textnode import TextNode, TextType
from src.htmlnode import HTMLNode, LeafNode, ParentNode
from scr.split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link



def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("input is not correct TextType")
    

    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value = text_node.text)   
        case TextType.BOLD:
            return LeafNode(tag = "b", value = text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag = "i", value = text_node.text)
        case TextType.CODE:
            return LeafNode(tag = "code", value = text_node.text)
        case TextType.LINK:
            return LeafNode(tag = "a", value = text_node.text, props ={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag = "img" , value = "", props= {"src": text_node.url, "alt": text_node.text} )#{"src": url, "alt": alt_text})



def text_to_textnodes(text):
    result = [text_node(text, text_type.TEXT)]
    result = split_nodes_delimiter(result, text_type)
    result = split_nodes_image(result)
    result = split_nodes_link(result)

    return result




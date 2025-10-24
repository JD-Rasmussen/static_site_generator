

from src.htmlnode import HTMLNode, LeafNode, ParentNode
from src.textnode import TextNode, TextType
from src.textnode_to_htmlnode import text_node_to_html_node
from src.extract_markdowns import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []    
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            if len(parts)% 2 == 0: 
                raise Exception("missing end delimiter")
            for i, part in enumerate(parts):
                if part == "": continue
                chosen_type = text_type if i % 2 == 1 else TextType.TEXT
                result.append(TextNode(part, chosen_type))
        else:
            result.append(node)
    return result


def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            extracted_parts = extract_markdown_links(node.text)
            for link_tuple in extracted_parts:
                parts[i] = link_tuple[].split(link_tuple[0])
        if len(parts)% 2 == 0: 
            raise Exception("missing end delimiter")
        for i, part in enumerate(parts):
            if part == "": continue
            chosen_type = text_type if i % 2 == 1 else TextType.TEXT
            result.append(TextNode(part, chosen_type))
        else:
            result.append(node)
    return result


def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        










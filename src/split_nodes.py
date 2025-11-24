

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
from textnode_to_htmlnode import text_node_to_html_node
from extract_markdowns import extract_markdown_images, extract_markdown_links


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
            current_raw_text = node.text
            for link_tuple in extracted_parts:
                full_link = f"[{link_tuple[0]}]({link_tuple[1]})"
                parts = current_raw_text.split(full_link, maxsplit=1)
                text_before_link = parts[0]
                text_after_link = parts[1]
                current_raw_text = text_after_link
                if text_before_link != "": 
                    new_node = TextNode(text_before_link, TextType.TEXT)
                    result.append(new_node)
                if full_link != "":
                    new_node = TextNode(link_tuple[0], TextType.LINK, link_tuple[1]) 
                    result.append(new_node)
            if current_raw_text != "": 
                new_node = TextNode(current_raw_text, TextType.TEXT)
                result.append(new_node)
        else:
            result.append(node)

    return result


def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            extracted_parts = extract_markdown_images(node.text)
            current_raw_text = node.text
            for image_tuple in extracted_parts:
                full_image = f"![{image_tuple[0]}]({image_tuple[1]})"
                parts = current_raw_text.split(full_image, maxsplit=1)
                text_before_image = parts[0]
                text_after_image = parts[1]
                current_raw_text = text_after_image
                if text_before_image != "": 
                    new_node = TextNode(text_before_image, TextType.TEXT)
                    result.append(new_node)
                if full_image != "":
                    new_node = TextNode(image_tuple[0], TextType.IMAGE, image_tuple[1]) 
                    result.append(new_node)
            if current_raw_text != "": 
                new_node = TextNode(current_raw_text, TextType.TEXT)
                result.append(new_node)
        else:
            result.append(node)
    return result
        

def text_to_textnodes(text):
    result = [TextNode(text, TextType.TEXT)]
    result = split_nodes_delimiter(result, "`", TextType.CODE)
    result = split_nodes_delimiter(result, "**", TextType.BOLD)
    result = split_nodes_delimiter(result, "_", TextType.ITALIC)
    result = split_nodes_image(result)
    result = split_nodes_link(result)

    return result   





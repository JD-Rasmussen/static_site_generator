
import src.extract_markdowns
import src.htmlnode
import src.htmlnode
import src.split_nodes
import src.textnode_to_htmlnode

def markdown_to_html_node(markdown):
    parts = markdown_to_blocks(markdown)

    for part in parts:
        nodetype        = block_to_block_type(part)
        if nodetype != BlockType.CODE:
            new_textnodes = text_to_textnodes(part)
            for i in len(new_textnodes):
                new_child_node[i] = text_node_to_html_node(new_textnodes[i]) 
        else:
            new_text = part[:]
            new_node = TextNode() 








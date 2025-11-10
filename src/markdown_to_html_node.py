
import src.extract_markdowns
import src.htmlnode
import src.htmlnode
import src.split_nodes
import src.textnode_to_htmlnode

def strip_prefix_once(s, prefix):
    return s[len(prefix):] if s.startswith(prefix) else s

def markdown_to_html_node(markdown):
    parts = markdown_to_blocks(markdown)
    result = []

    for part in parts:
        nodetype = block_to_block_type(part)

        if nodetype == BlockType.HEADING:
        
        elif nodetype == BlockType.QUOTE:
            lines = part.splitlines()  
            clean_lines = []
                for ln  in lines:
                    ln = ln.rstrip()
                    if not ln.strip():
                        continue
                    ln = strip_prefix_once(ln, "> ")
                    clean_lines.append(ln)
            inner_text = " ".join([ln.strip() for ln in clean_lines])
            

            tn_list = text_to_textnodes(inner_text)
            inline_children = [text_node_to_html_node(tn) for tn in tn_list]
            blockquote_node = ParentNode("blockquote", inline_children)
            result.append(blockquote_node)

        elif nodetype == BlockType.UNORDERED_LIST:

        elif nodetype == BlockType.ORDERED_LIST:

        elif nodetype == BlockType.PARAGRAPH:
            lines = part.splitlines()  
            clean_lines = [ln.strip() for ln in lines if ln.strip() != ""]
            inner_text = " ".join(clean_lines)

            tn_list = text_to_textnodes(inner_text)
            inline_children = [text_node_to_html_node(tn) for tn in tn_list]
            p_node = ParentNode("p", inline_children)
            result.append(p_node)

        elif nodetype == BlockType.CODE:
            lines = part.splitlines()   
            inner_code = "\n".join(lines[1:-1]) + "\n"

            code_leaf = text_node_to_html_node(TextNode(inner_code, TextType.TEXT))
            code_node = ParentNode("code", [code_leaf])
            pre_node = ParentNode("pre", [code_node])
            result.append(pre_node)

    return ParentNode("div", result)







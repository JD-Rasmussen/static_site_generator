from extract_markdowns import markdown_to_blocks 
from block_type import block_to_block_type, BlockType
from split_nodes import text_to_textnodes
from htmlnode import ParentNode
from textnode import TextNode, TextType
from textnode_to_htmlnode import text_node_to_html_node
import textwrap

def strip_prefix_once(s, prefix):
    return s[len(prefix):] if s.startswith(prefix) else s

def markdown_to_html_node(markdown):
    parts = markdown_to_blocks(markdown)
    result = []
    for part in parts:
        nodetype = block_to_block_type(part)

        if nodetype == BlockType.HEADING:
            first = part.splitlines()[0].lstrip()
            level = 0
            while level < len(first) and level < 6 and first[level] == '#':
                level += 1
            tag = f"h{level}"

            text = first[level:].lstrip()
            tn_list = text_to_textnodes(text)
            inline_children = [text_node_to_html_node(tn) for tn in tn_list]
            result.append(ParentNode(tag, inline_children))
            
        elif nodetype == BlockType.QUOTE:
            lines = [l for l in part.splitlines() if l.strip()]
            cleaned = []
            for l in lines:
                t = l.lstrip()
                if t.startswith(">"):
                    t = t[1:].lstrip()
                cleaned.append(t)
            text = " ".join(cleaned)
            children = [text_node_to_html_node(tn) for tn in text_to_textnodes(text)]
            result.append(ParentNode("blockquote", children))

        elif nodetype == BlockType.UNORDERED_LIST:
            lines = part.splitlines()
            li_nodes = []
            for ln in lines:
                if not ln.strip():
                    continue
                ln = ln.lstrip()  # allow indented bullets
                ln = strip_prefix_once(ln, "- ")
                ln = strip_prefix_once(ln, "* ")
                item_text = ln.strip()
                if not item_text:
                    continue
                tn_list = text_to_textnodes(item_text)
                inline_children = [text_node_to_html_node(tn) for tn in tn_list]
                li_nodes.append(ParentNode("li", inline_children))
            result.append(ParentNode("ul", li_nodes))

        elif nodetype == BlockType.ORDERED_LIST:
            li_nodes = []
            for ln in part.splitlines():
                ln = ln.rstrip()
                if not ln.strip():
                    continue
                #detect N prefix
                i = 0
                while i < len(ln) and ln[i].isdigit():
                    i += 1
                if i > 0 and i +1 < len(ln) and ln[i] == '.' and ln[i+1] == ' ':
                    prefix = ln[:i+2]
                    ln = strip_prefix_once(ln, prefix)
                
                item_text = ln.strip()
                if not item_text:
                    continue
                
                tn_list = text_to_textnodes(item_text)
                inline_children = [text_node_to_html_node(tn) for tn in tn_list]
                li_nodes.append(ParentNode("li", inline_children))
            result.append(ParentNode("ol", li_nodes))



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
            raw = "\n".join(lines[1:-1]) + "\n"
            inner_code = textwrap.dedent(raw)

            code_leaf = text_node_to_html_node(TextNode(inner_code, TextType.TEXT))
            code_node = ParentNode("code", [code_leaf])
            pre_node = ParentNode("pre", [code_node])
            result.append(pre_node)

    return ParentNode("div", result)







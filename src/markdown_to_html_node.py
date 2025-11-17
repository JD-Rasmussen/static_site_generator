from src.markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from src.inline_markdown import text_to_textnodes
from src.htmlnode import ParentNode
from src.textnode import TextNode, TextType
from src.inline_markdown import text_node_to_html_node

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
            lines = part.splitlines()
            li_nodes = []
            for ln  in lines:
                ln = ln.rstrip()
                if not ln.strip():
                    continue
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
            inner_code = "\n".join(lines[1:-1]) + "\n"

            code_leaf = text_node_to_html_node(TextNode(inner_code, TextType.TEXT))
            code_node = ParentNode("code", [code_leaf])
            pre_node = ParentNode("pre", [code_node])
            result.append(pre_node)

    return ParentNode("div", result)







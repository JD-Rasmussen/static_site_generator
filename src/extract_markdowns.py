import re
import textwrap


def extract_markdown_images(text):
    result = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return result



def extract_markdown_links(text):
    result = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return result


def markdown_to_blocks(md):
    md = textwrap.dedent(md)
    blocks, cur = [], []
    in_code = False
    for line in md.splitlines():
        if not in_code:
            if line.strip().startswith("```"):
                in_code = True
                if cur:
                    blocks.append("\n".join(cur)); cur = []
                cur.append(line)
            elif line.strip() == "":
                if cur:
                    blocks.append("\n".join(cur)); cur = []
            else:
                cur.append(line)
        else:
            cur.append(line)
            if line.strip() == "```":
                blocks.append("\n".join(cur)); cur = []
                in_code = False
    if cur:
        blocks.append("\n".join(cur))
    return blocks


def extract_title(markdown):
    md = textwrap.dedent(markdown)
    title = ""
    for line in md.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("# ") and not stripped.startswith("## "):
            title = stripped[2:].strip()
            break
    if title == "":
        raise Exception("no header found")
    
    return title
            









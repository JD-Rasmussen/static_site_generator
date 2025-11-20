from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH       = "paragraph"
    HEADING         = "heading"
    CODE            = "code"
    QUOTE           = "quote"
    UNORDERED_LIST  = "unordered_list"
    ORDERED_LIST    = "ordered_list"


def block_to_block_type(markdown):
    lines = markdown.splitlines()
    # trim leading/trailing empty lines only
    while lines and lines[0].strip() == "": lines.pop(0)
    while lines and lines[-1].strip() == "": lines.pop()
    if not lines: return BlockType.PARAGRAPH

    if lines[0].lstrip().startswith("```") and lines[-1].strip() == "```":
        return BlockType.CODE

    if re.match(r'#{1,6}\s', lines[0].lstrip()):
        return BlockType.HEADING

    nonempty = [l for l in lines if l.strip()]

    if all(l.lstrip().startswith(">") for l in nonempty):
        return BlockType.QUOTE

    if all(l.lstrip().startswith("- ") or l.lstrip().startswith("* ") for l in nonempty):
        return BlockType.UNORDERED_LIST

    if all(l.lstrip().startswith(f"{i}. ") for i, l in enumerate(nonempty, start=1)):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPHSS
from enum import Enum
import re
from extract_markdowns import markdown_to_blocks

class BlockType(Enum):
    PARAGRAPH       = "paragraph"
    HEADING         = "heading"
    CODE            = "code"
    QUOTE           = "quote"
    UNORDERED_LIST  = "unordered list"
    ORDERED_LIST    = "ordered list"



def block_to_block_type(markdown):
    lines = markdown.split("\n")
    if not lines:
        return BlockType.PARAGRAPH

    if lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE

    elif re.match(r'#{1,6}\s', lines[0]):
        return BlockType.HEADING

    elif all(i.startswith(">") for i in lines):
        return BlockType.QUOTE
    
    elif all(i.startswith("- ") for i in lines):
        return BlockType.UNORDERED_LIST
    
    elif all(line.startswith(f"{i}. ") for i, line in enumerate(lines, start=1)):
        return BlockType.ORDERED_LIST

    else:
        return BlockType.PARAGRAPH
























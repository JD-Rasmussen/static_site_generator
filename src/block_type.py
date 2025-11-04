from enum import Enum



class BlockType(Enum):
    PARAGRAPH       = "paragraph"
    HEADING         = "heading"
    CODE            = "code"
    QUOTE           = "quote"
    UNORDERED_LIST  = "unordered list"
    ORDERED_LIST    = "ordered list"



def block_to_block_type(markdown):

    heading = markdow.split("#", maxsplit=1)




    return block_type























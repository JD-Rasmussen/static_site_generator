import unittest

from block_type import BlockType, block_to_block_type

class Testblock_to_block_type(unittest.TestCase):
    
    def test_block_type_heading(self):
        md = "# Title"
        assert block_to_block_type(md) == BlockType.HEADING
    
    def test_block_type_code(self):
        md = "```py\nx = 1\n```"
        assert block_to_block_type(md) == BlockType.CODE

    def test_block_type_quote(self):
        md = "> a\n> b"
        assert block_to_block_type(md) == BlockType.QUOTE
   
    def test_block_type_unordered_list(self):
        md = "- a\n- b"
        assert block_to_block_type(md) == BlockType.UNORDERED_LIST
    # python
    def test_block_type_ordered_list(self):
        md = "1. a\n2. b\n3. c"
        assert block_to_block_type(md) == BlockType.ORDERED_LIST

    def test_block_type_paragraph(self):
        md = "just some text"
        assert block_to_block_type(md) == BlockType.PARAGRAPH



















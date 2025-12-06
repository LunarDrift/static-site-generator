import unittest
from markdown_blocks import BlockType, markdown_to_blocks, block_to_blocktype


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        block = "This is a simple paragraph with **bold** and _italic_ text."
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)

    def test_heading(self):
        block = "### This is a level 3 heading"
        self.assertEqual(block_to_blocktype(block), BlockType.HEADING)

    def test_code_block(self):
        block = """```
        def hello_world():
            print("Hello, world!")
        ```
        """
        self.assertEqual(block_to_blocktype(block), BlockType.CODE)
    
    def test_quote_block(self):
        block = """> This is a quote.
> It spans multiple lines.
> Still part of the quote."""
        self.assertEqual(block_to_blocktype(block), BlockType.QUOTE)

    def test_unordered_list(self):
        block = """- Item one
- Item two
- Item three"""
        self.assertEqual(block_to_blocktype(block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = """1. First item
2. Second item
3. Third item"""
        self.assertEqual(block_to_blocktype(block), BlockType.ORDERED_LIST)



if __name__ == "__main__":
    unittest.main()

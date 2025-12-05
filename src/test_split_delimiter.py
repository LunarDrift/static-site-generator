import unittest
from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitDelimiterNodes(unittest.TestCase):
    def test_split_bold(self):
        old_nodes = [TextNode("This is **bold** text", TextType.BOLD)]
        delimiter = "**"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        expected_nodes = [
            TextNode("This is ", TextType.BOLD),
            TextNode("**", TextType.BOLD),
            TextNode("bold", TextType.BOLD),
            TextNode("**", TextType.BOLD),
            TextNode(" text", TextType.BOLD)
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_no_delimiter(self):
        old_nodes = [TextNode("This is normal text", TextType.TEXT)]
        delimiter = "**"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(new_nodes, old_nodes)

    def test_invalid_syntax(self):
        old_nodes = [TextNode("This is bold text", TextType.BOLD)]
        delimiter = "**"
        text_type = TextType.BOLD
        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, delimiter, text_type)

if __name__ == "__main__":
    unittest.main()
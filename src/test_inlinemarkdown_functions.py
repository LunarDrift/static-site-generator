import unittest
from inlinemarkdown_functions import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    extract_markdown_images,
    extract_markdown_links,
    text_to_textnodes,
)
from textnode import TextNode, TextType


class TestInlineMarkdownFunctions(unittest.TestCase):
    # ----- Split Nodes Tests -----
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

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.TEXT),
            ],
            new_nodes,
        )

    # ----- Image Tests -----
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_no_images(self):
        matches = extract_markdown_images("This is text without images.")
        self.assertListEqual([], matches)

    def test_multiple_images(self):
        text = "Here is an image ![img1](http://example.com/img1.png) and another ![img2](http://example.com/img2.png)."
        expected = [("img1", "http://example.com/img1.png"), ("img2", "http://example.com/img2.png")]
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)


    # ----- Link Tests -----
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )

    # ----- Text to TextNodes Tests -----
    def test_text_to_textnodes(self):
        text = "This is a simple text."
        nodes = text_to_textnodes(text)
        expected_nodes = [TextNode("This is a simple text.", TextType.TEXT)]
        self.assertEqual(nodes, expected_nodes)
    
    def test_text_to_textnodes_empty(self):
        text = ""
        nodes = text_to_textnodes(text)
        expected_nodes = [TextNode("", TextType.TEXT)]
        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes_special_characters(self):
        text = "Hello, World! @#&*()"
        nodes = text_to_textnodes(text)
        expected_nodes = [TextNode("Hello, World! @#&*()", TextType.TEXT)]
        self.assertEqual(nodes, expected_nodes)



if __name__ == "__main__":
    unittest.main()
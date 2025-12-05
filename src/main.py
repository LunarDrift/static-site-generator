from textnode import TextType, TextNode


def main():
    node = TextNode(
        text="This is some anchor text",
        text_type=TextType.LINK.value,
        url="https://www.boot.dev"
)

    print(node)

main()
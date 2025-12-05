from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type:
            new_nodes.append(node)
            continue
        if delimiter not in node.text:
            raise ValueError("Invalid Markdown syntax")
        parts = node.text.split(delimiter)
        for i, part in enumerate(parts):
            if part:
                new_nodes.append(TextNode(part, node.text_type, node.url))
            if i < len(parts) - 1:
                new_nodes.append(TextNode(delimiter, text_type))
    return new_nodes
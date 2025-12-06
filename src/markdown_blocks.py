from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    """Takes a raw Markdown string (representing a full document) as input and returns a list of 'block' strings."""
    cleaned = []
    blocks = markdown.split('\n\n')
    for block in blocks:
        block = block.strip()
        if block:
            cleaned.append(block)
    return cleaned


def block_to_blocktype(block):
    """Takes a single block of markdown text as input and returns the BlockType representing the type of block it is."""
    # Split lines for multi-line checks
    lines = block.split("\n")
    
    # Check if heading
    if block.startswith("#"):
        # Count the num of '#' at the start
        i = 0
        while i < len(block) and block[i] == "#":
            i += 1
        # Heading must have 1-6 '#' and a space after
        if 1 <= i <= 6 and block[i] == " ":
            return BlockType.HEADING
    
    # Check if code block; Must start and end with 3 backticks
    non_empty_lines = [line for line in lines if line.strip() != '']
    if non_empty_lines[0].strip() == "```" and non_empty_lines[-1].strip() == "```":
        return BlockType.CODE
    

    # Check if quote block; Every line must start with '>'
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    # Check if unordered list; Every line must start with '- '
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    # Check if ordered list; Every line must start with a number followed by '. '. Number must start at 1 and increment by 1 for each line
    num = 1
    is_ordered_list = True
    for line in lines:
        if line.startswith(f"{num}. "):
            num += 1
        else:
            is_ordered_list = False
            break
    if is_ordered_list and len(lines) > 0:
        return BlockType.ORDERED_LIST
    # If none of above conditions met, block is a normal paragraph
    return BlockType.PARAGRAPH
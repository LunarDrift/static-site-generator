class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # Every data member is optional and defaults to None
        self.tag = tag  # a string representing the HTML tag name ("p", "a", "h1", etc)
        self.value = value  # string representing the value of the HTML tag (eg. text inside the paragraph)
        self.children = children  # list of the HTMLNode objects representing the children of this node
        self.props = props  # a dict of key/value pairs representing the attributes of the HTML tag

    
    def to_html(self):
        """Child classes will override this method to render
        themselves as HTML."""
        raise NotImplementedError
    

    def props_to_html(self):
        """Returns a formatted string representing the HTML attributes of the node."""
        if self.props is None:
            return ""
        props_html = ""
        for key, value in self.props.items():
            props_html += f' {key}="{value}"'
        return props_html
    

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        # All leaf nodes must have a value
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        
        # If there is no tag, return the value as raw text
        if self.tag is None:
            return self.value
        
        # Build attributes string (eg. ' href="https://example.com"')
        props_str = ""
        if self.props:
            props_parts = []
            for key,val in self.props.items():
                props_parts.append(f'{key}="{val}"')
            props_str = " " + " ".join(props_parts)

        # Wrap the value inside the HTML tag
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

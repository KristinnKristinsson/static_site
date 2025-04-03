import re

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise Exception(NotImplementedError)
    
    def props_to_html(self):
        the_props_string = ""
        if self.props == None:
            return the_props_string
        for key, value in self.props.items():
            the_props_string += f' {key}="{value}"'
        return the_props_string
    
    
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("missing value")
        if self.tag == None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.props == other.props
    
class ParentNode(HTMLNode):
    
    def __init__(self, tag, children, props=None):
        if children == None:
            raise ValueError("missing children")
        if tag == None:
            raise ValueError("missing tags")
        super().__init__(tag, None, children, props)

    def to_html(self):
        
        if not isinstance(self.tag, str) or self.tag == "":
            raise ValueError("missing tags")
        if not isinstance(self.children, list) or self.children == None:
            raise ValueError("missing children")
        result = f"<{self.tag}>"
        for child in self.children:
            result += f"{child.to_html()}"
        result += f"</{self.tag}>"
        return result
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
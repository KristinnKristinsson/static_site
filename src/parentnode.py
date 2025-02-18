from htmlnode import HTMLNode
from leafnode import LeafNode

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
from htmlnode import HTMLNode
#from textnode import TextNode, TextType

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        #self.value = value
        
        
    def to_html(self):
        
        if self.value == None:
            raise ValueError("missing value")
        if self.tag == None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
   
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.props == other.props
from htmlnode import HTMLNode
import re
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
    
    def markdown_to_blocks(text):
        if not isinstance(text, str):
            raise ValueError("Not a string object")
        result_block = []
        text = text.strip("\n")
        split_block = re.split(r"\n\n", text)
        for block in split_block:
            mini_blocks = re.split(r"  *", block)
            block = " ".join(mini_blocks).replace('\n ', '\n')
            result_block.append(block.strip())
        return result_block

    
   
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.props == other.props
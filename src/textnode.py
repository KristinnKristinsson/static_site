from enum import Enum
from htmlnode import LeafNode
import re

class TextType(Enum):
    NORMAL_TEXT = "normal"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case text_node.text_type.NORMAL_TEXT:
                return LeafNode(None, text_node.text)
            case text_node.text_type.BOLD_TEXT:
                return LeafNode("b", text_node.text)
            case text_node.text_type.ITALIC_TEXT:
                return LeafNode("i", text_node.text)
            case text_node.text_type.CODE:
                return LeafNode("code", text_node.text)
            case text_node.text_type.LINKS:
                return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
            case text_node.text_type.IMAGES:
                return LeafNode("img", text_node.text, {"src": f"{text_node.url}"})
        raise Exception("Non-compatible text type.")

    def __eq__(self, other):
       return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    

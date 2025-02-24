from enum import Enum
from leafnode import LeafNode
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
    
    def split_nodes_delimiter(self, text, result_list=[]):
        if self.text_type != TextType.NORMAL_TEXT:
            raise Exception("Not a valid format for text.")
        if text == "":
            result_list.clear()
            return result_list
        lst_text = list(text)
        if lst_text[0] == "**" or "*" or "`":
            if lst_text[0:2] == ['*','*']:
                split_text = text.split("**", maxsplit=2)
                result = TextNode(f"{split_text.pop(1)}", TextType.BOLD_TEXT)
                feedback_text = TextNode("".join(split_text), TextType.NORMAL_TEXT)
                feedback_text.split_nodes_delimiter(feedback_text.text)
                result_list.insert(0, result)
                return result_list
            if "*" == lst_text[0]:
                split_text = text.split("*", maxsplit=2)
                result = TextNode(f"{split_text.pop(1)}", TextType.ITALIC_TEXT)
                feedback_text = TextNode("".join(split_text), TextType.NORMAL_TEXT)
                feedback_text.split_nodes_delimiter(feedback_text.text)
                result_list.insert(0, result)
                return result_list
            if "`" == lst_text[0]:
                split_text = text.split("`", maxsplit=2)
                result = TextNode(f"{split_text.pop(1)}", TextType.CODE)
                feedback_text = TextNode("".join(split_text), TextType.NORMAL_TEXT)
                feedback_text.split_nodes_delimiter(feedback_text.text)
                result_list.insert(0, result)
                return result_list
            else:
                for i in range(0, len(lst_text)):
                    if lst_text[i:i+2] == ['*','*']:
                        split_text = text.split("**", maxsplit=2)
                        result = TextNode(f"{split_text.pop(0)}", TextType.NORMAL_TEXT)
                        result2 = TextNode(f"{split_text.pop(0)}", TextType.BOLD_TEXT)
                        feedback_text = TextNode("".join(split_text), TextType.NORMAL_TEXT)
                        feedback_text.split_nodes_delimiter(feedback_text.text)
                        result_list.insert(0, result2), result_list.insert(0, result)
                        return result_list
                    if lst_text[i] == "*":
                        split_text = text.split("*", maxsplit=2)
                        result = TextNode(f"{split_text.pop(0)}", TextType.NORMAL_TEXT)
                        result2 = TextNode(f"{split_text.pop(0)}", TextType.ITALIC_TEXT)
                        feedback_text = TextNode("".join(split_text), TextType.NORMAL_TEXT)
                        feedback_text.split_nodes_delimiter(feedback_text.text)
                        result_list.insert(0, result2), result_list.insert(0, result)
                        return result_list
                    if lst_text[i] == "`":
                        split_text = text.split("`", maxsplit=2)
                        result = TextNode(f"{split_text.pop(0)}", TextType.NORMAL_TEXT)
                        result2 = TextNode(f"{split_text.pop(0)}", TextType.CODE)
                        feedback_text = TextNode("".join(split_text), TextType.NORMAL_TEXT)
                        feedback_text.split_nodes_delimiter(feedback_text.text)
                        result_list.insert(0, result2), result_list.insert(0, result)
                        return result_list
                result =  TextNode(f"{text}", TextType.NORMAL_TEXT)
                text = ""
                feedback_text = TextNode(text, TextType.NORMAL_TEXT)
                feedback_text.split_nodes_delimiter(feedback_text.text)
                result_list.insert(0, result)
                return result_list
                    


        
        #Return a TextNode in the right order.
        #Return them in order
        #split them depending on the 

    def extract_markdown_images(text):
        if not isinstance(text, str):
            raise ValueError("Not a string.")
        list_of_imgs = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
        return list_of_imgs
    def extract_markdown_links(text):
        if not isinstance(text, str):
            raise ValueError("Not a string.")
        list_of_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
        return list_of_links

    def __eq__(self, other):
       return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    

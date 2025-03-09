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
        if text == "": #base case
            result_list.clear()
            return result_list
        filter_text = filter(None, re.split(r'(\*{2}|\*|\`|!|\[)', text, maxsplit=1)) #Check for bold, italic, code text. Split two because both sides
        split_text = list(filter_text) 
        if len(split_text) > 1:                                                  #Make sure there is text to split
                if split_text[0] == "":
                    split_text.pop(0)                                             #of the text
        if split_text[0] == "**" or split_text[0] == "*" or split_text[0] == "`":
            filter_text = filter(None, re.split(r'(\*{2}|\*|\`)', text, maxsplit=2))
            split_text = list(filter_text) 
            if split_text[0] == "**":
                result = TextNode(f"{split_text.pop(1)}", TextType.BOLD_TEXT)
                split_text.pop(0)
                split_text.pop(0)
                feedback_text = TextNode("".join(split_text), TextType.NORMAL_TEXT)
                feedback_text.split_nodes_delimiter(feedback_text.text)
                result_list.insert(0, result)
                return result_list
            elif split_text[0] == "*":
                result = TextNode(f"{split_text.pop(1)}", TextType.ITALIC_TEXT)
                split_text.pop(0)
                split_text.pop(0)
                feedback_text = TextNode("".join(split_text), TextType.NORMAL_TEXT)
                feedback_text.split_nodes_delimiter(feedback_text.text)
                result_list.insert(0, result)
                return result_list
            elif split_text[0] == "`":
                result = TextNode(f"{split_text.pop(1)}", TextType.CODE)
                split_text.pop(0)
                split_text.pop(0)
                feedback_text = TextNode("".join(split_text), TextType.NORMAL_TEXT)
                feedback_text.split_nodes_delimiter(feedback_text.text)
                result_list.insert(0, result)
                return result_list 
        elif split_text[0] == "!" or split_text[0] == "[":
            if split_text[0] == "!":
                image = TextNode.extract_markdown_images("".join(split_text))
                result = TextNode(f"{image[0][0]}", TextType.IMAGES, f"{image[0][1]}")
                split_text.pop(0)
                popped_text = re.split(rf'\[{image[0][0]}\]\({image[0][1]}\)', "".join(split_text), maxsplit=1)
                popped_text.pop(0)
                feedback_text = TextNode("".join(popped_text), TextType.NORMAL_TEXT)
                feedback_text.split_nodes_delimiter(feedback_text.text)                    
                result_list.insert(0, result)
                return result_list
            elif split_text[0] == "[":
                link = TextNode.extract_markdown_links("".join(split_text))
                result = TextNode(f"{link[0][0]}", TextType.LINKS, f"{link[0][1]}")
                popped_text = re.split(rf'\[{link[0][0]}\]\({link[0][1]}\)', "".join(split_text), maxsplit=1)
                feedback_text = TextNode("".join(popped_text), TextType.NORMAL_TEXT)
                feedback_text.split_nodes_delimiter(feedback_text.text)
                result_list.insert(0, result)
                return result_list
        else:
            result = TextNode(f"{split_text.pop(0)}", TextType.NORMAL_TEXT)
            feedback_text = TextNode("".join(split_text), TextType.NORMAL_TEXT)
            feedback_text.split_nodes_delimiter(feedback_text.text)
            result_list.insert(0, result)
            return result_list

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

    def split_nodes_image(node):
        listed = []
        list_of_imgs = TextNode.extract_markdown_images(node.text)
        for img in list_of_imgs:
            listed.append(TextNode(f"{img[0]}", TextType.IMAGES, f"{img[1]}"))
        return listed

    def __eq__(self, other):
       return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    

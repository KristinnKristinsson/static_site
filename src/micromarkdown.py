import re
from textnode import TextNode, TextType

def split_nodes_delimiter(text, result_list=[]):
    if not isinstance(text, str):
        raise Exception("Not valid format")
    if text == "": #base case
        result_list.clear()
        return result_list
    filter_text = filter(None, re.split(r'(\*{2}|\*|\`|!|\[)', text, maxsplit=1))
    split_text = list(filter_text) 
    if len(split_text) > 1:
            if split_text[0] == "":
                split_text.pop(0)
    if split_text[0] == "**" or split_text[0] == "*" or split_text[0] == "`":
        filter_text = filter(None, re.split(r'(\*{2}|\*|\`)', text, maxsplit=2))
        split_text = list(filter_text) 
        if split_text[0] == "**":
            result = TextNode(f"{split_text.pop(1)}", TextType.BOLD_TEXT)
            split_text.pop(0)
            split_text.pop(0)
            feedback_text = "".join(split_text)
            split_nodes_delimiter(feedback_text)
            result_list.insert(0, result)
            return result_list
        elif split_text[0] == "*":
            result = TextNode(f"{split_text.pop(1)}", TextType.ITALIC_TEXT)
            split_text.pop(0)
            split_text.pop(0)
            feedback_text = "".join(split_text)
            split_nodes_delimiter(feedback_text)
            result_list.insert(0, result)
            return result_list
        elif split_text[0] == "`":
            result = TextNode(f"{split_text.pop(1)}", TextType.CODE)
            split_text.pop(0)
            split_text.pop(0)
            feedback_text = "".join(split_text)
            split_nodes_delimiter(feedback_text)
            result_list.insert(0, result)
            return result_list 
    elif split_text[0] == "!" or split_text[0] == "[":
        if split_text[0] == "!":
            image = extract_markdown_images("".join(split_text))
            result = TextNode(f"{image[0][0]}", TextType.IMAGES, f"{image[0][1]}")
            split_text.pop(0)
            popped_text = re.split(rf'\[{image[0][0]}\]\({image[0][1]}\)', "".join(split_text), maxsplit=1)
            popped_text.pop(0)
            feedback_text = "".join(popped_text)
            split_nodes_delimiter(feedback_text)                    
            result_list.insert(0, result)
            return result_list
        elif split_text[0] == "[":
            link = extract_markdown_links("".join(split_text))
            result = TextNode(f"{link[0][0]}", TextType.LINKS, f"{link[0][1]}")
            popped_text = re.split(rf'\[{link[0][0]}\]\({link[0][1]}\)', "".join(split_text), maxsplit=1)
            feedback_text = "".join(popped_text)
            split_nodes_delimiter(feedback_text)
            result_list.insert(0, result)
            return result_list
    else:
        result = TextNode(f"{split_text.pop(0)}", TextType.NORMAL_TEXT)
        feedback_text = "".join(split_text)
        split_nodes_delimiter(feedback_text)
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
    list_of_imgs = extract_markdown_images(node.text)
    for img in list_of_imgs:
        listed.append(TextNode(f"{img[0]}", TextType.IMAGES, f"{img[1]}"))
    return listed
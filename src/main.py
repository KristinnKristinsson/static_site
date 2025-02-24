from textnode import TextNode
from textnode import TextType
from parentnode import ParentNode

def main():
    text = TextNode("This", TextType.NORMAL_TEXT)
    TextNode.extract_markdown_images(text)
        
    TextNode.extract_markdown_links(text)


main()

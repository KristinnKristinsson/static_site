from textnode import TextNode
from textnode import TextType

def main():
    print("hello world")
    #print(list(TextNode))
    text = TextNode(text="Mama", text_type=TextType.BOLD_TEXT, url="https://www.hi.com")
    print(text)


main()

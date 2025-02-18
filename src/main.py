from textnode import TextNode
from textnode import TextType
from parentnode import ParentNode

def main():
    print("hello world")
    #print(list(TextNode))
    text = TextNode("Mama", TextType.BOLD_TEXT)
    #node = ParentNode("p", None, None)
    leaf = TextNode.text_node_to_html_node(text)
    node8 = TextNode("what", TextType.NORMAL_TEXT)
    print(node8)
    print(leaf)
    
    print(text)


main()

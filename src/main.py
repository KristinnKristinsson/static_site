
#from textnode import TextType
from parentnode import ParentNode
from textnode import TextNode, TextType

def main():
    node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL_TEXT)
    node2 = TextNode("*Just* **one** word.", TextType.NORMAL_TEXT)
    result2 = node2.split_nodes_delimiter(node2.text)
    print(result2)

    #node = TextNode("*Lets* start [linking](https://linkit.se) with this **beautiful** link to another ![people dancing](src/image/sh) image of `std.out(printf'hello')` what the? **Who** are **you my little friend**", TextType.NORMAL_TEXT)
    result = node.split_nodes_delimiter(node.text)
    #print(result)


main()

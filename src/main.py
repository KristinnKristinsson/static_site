
#from textnode import TextType
from textnode import TextNode, TextType
import macromarkdown
import mdtohtml
from htmlnode import HTMLNode
import re
from static_to_public import static_to_public

def main():
    static_to_public()
    

main()

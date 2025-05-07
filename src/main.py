
#from textnode import TextType
from textnode import TextNode, TextType
import macromarkdown
import micromarkdown
import mdtohtml
from htmlnode import HTMLNode
import re, sys
from static_to_public import static_to_public, generate_page, create_content

def main():
    static_to_public()
    create_content()
    
    

main()


#from textnode import TextType
from textnode import TextNode, TextType
import macromarkdown
import mdtohtml
from htmlnode import HTMLNode
import re

def main():
    
    md ="""
            ### The *italians do like* this kind of text

            anything **else** than the first one

            1. Because `this time` I think it is different
            2. I mean I think you really like meee

            5. Because this time I think it is different
            9. I mean I think you really like mee
            6. eheeee eeeeeeheeeeeee


             ```
             where we get what we want
             and we **want** to get paid
             but it feels so bad
             to be so sad 
             ```

             Lets just write some stupid text
             that has a couple of new lines
             and I'm sure its fine

             > and what we have here
             > is a little bit of quotes
             > to get us started

             > but mixing things
             - up should not
             2. work

             #### Just to keep it going

             "What will happen now?"


             - except
             - when
             - we list it.


             DO YOU FEEL ME *OR* do you **feel** me' 
             I'm getting tired of this. 
        """
    results = mdtohtml.markdown_to_html_node(md)
    print(results)


main()

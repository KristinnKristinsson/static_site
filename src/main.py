
#from textnode import TextType
from parentnode import ParentNode
from textnode import TextNode, TextType
from leafnode import LeafNode

def main():
    md = """
            The *italians do like* this kind of text


            where we get what we want
            and we want to get paid
            but it feels so bad
            to be so sad


            -except
            -when
            -we list it.


            DO YOU FEEL ME *OR* do you **feel** me

            I'm getting tired of this.
        """
    result = LeafNode.markdown_to_blocks(md)
    print(result)


main()

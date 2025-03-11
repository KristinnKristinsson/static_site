import unittest

from leafnode import LeafNode
#from textnode import TextNode, TextType


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("a","This is a text node", {"href": "https://this.is/a/test"})
        node2 = LeafNode("p", "This is a text node", None)
        node3 = LeafNode(None, "A text")
        result = node.to_html()
        result2 = node2.to_html()
        result3 = node3.to_html()
        self.assertEqual(result, '<a href="https://this.is/a/test">This is a text node</a>')
        self.assertEqual(result2, '<p>This is a text node</p>')
        self.assertEqual(result3, "A text")
    
    def test_ValueError(self):
        node4 = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node4.to_html()
    def test_markdown_to_blocks(self):
        md = """
            This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = LeafNode.markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        md2 = """
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
        blocks = LeafNode.markdown_to_blocks(md2)
        self.assertEqual(
            blocks,
            ['The *italians do like* this kind of text', 
             'where we get what we want\nand we want to get paid\nbut it feels so bad\nto be so sad', 
             '-except\n-when\n-we list it.', 
             'DO YOU FEEL ME *OR* do you **feel** me', 
             "I'm getting tired of this."],
        )

    def test_error_markdown(self):
        md = LeafNode("p", None)
        with self.assertRaises(ValueError):
            md.markdown_to_blocks()

    


if __name__ == "__main__":
    unittest.main()

import unittest

from textnode import TextNode, TextType
import re


class TestTextNode(unittest.TestCase):
    maxDiff = None
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
    
    def test_noteq(self):
        node3 = TextNode("This is not a text node", TextType.ITALIC_TEXT, "whatisthis")
        node4 = TextNode("This was but is not longer a textNode", TextType.NORMAL_TEXT)
        self.assertNotEqual(node3, node4)

    def test_almosteq(self):
        node5 = TextNode("Any", TextType.ITALIC_TEXT, None)
        node6 = TextNode("Any", TextType.BOLD_TEXT, "None")
        node7 = TextNode("Almost", TextType.ITALIC_TEXT, None)
        self.assertNotEqual(node5, node6, node7)
    
    def test_isnone(self):
        node8 = TextNode("what", TextType.NORMAL_TEXT)
        node9 = TextNode("Weeee", TextType.BOLD_TEXT, None)

    def test_convert(self):
        testTN = TextNode("Important", TextType.BOLD_TEXT)
        testLN = TextNode.text_node_to_html_node(testTN)
        result = testLN.to_html()
        self.assertEqual(result, "<b>Important</b>")
        testTN2 = TextNode("Not Important", TextType.NORMAL_TEXT)
        testLN2 = TextNode.text_node_to_html_node(testTN2)
        result2 = testLN2.to_html()
        self.assertEqual(result2, "Not Important")
        testTN3 = TextNode("link", TextType.LINKS, "https://link.me/now")
        testLN3 = TextNode.text_node_to_html_node(testTN3)
        result3 = testLN3.to_html()
        self.assertEqual(result3, '<a href="https://link.me/now">link</a>')
        testTN4 = TextNode("got milk?", TextType.IMAGES, "./someplace/pc/milk.jpg")
        testLN4 = TextNode.text_node_to_html_node(testTN4)
        result4 = testLN4.to_html()
        self.assertEqual(result4, '<img src="./someplace/pc/milk.jpg">got milk?</img>')

    
if __name__ == "__main__":
    unittest.main()

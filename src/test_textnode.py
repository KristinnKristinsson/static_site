import unittest

from textnode import TextNode, TextType
from leafnode import LeafNode


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

    def test_splitNodesDelimiter(self):
        node = TextNode("*hi*", TextType.NORMAL_TEXT)
        result = node.split_nodes_delimiter(node.text)
        self.assertEqual(f"{result}", "[TextNode(hi, italic, None)]")
        node2 = TextNode("*Just* **one** word.", TextType.NORMAL_TEXT)
        result2 = node2.split_nodes_delimiter(node2.text)
        self.assertEqual(f"{result2}", "[TextNode(Just, italic, None), TextNode( , normal, None), TextNode(one, bold, None), TextNode( word., normal, None)]")
        node3 = TextNode("What a *beautiful*, most **magnificent** morning", TextType.NORMAL_TEXT)
        result3 = node3.split_nodes_delimiter(node3.text)
        self.assertEqual(f"{result3}", "[TextNode(What a , normal, None), "
                         + "TextNode(beautiful, italic, None), "
                         + "TextNode(, most , normal, None), "
                         + "TextNode(magnificent, bold, None), "
                         + "TextNode( morning, normal, None)]")
        node4 = TextNode("a beautiful sunshine `this is a sun` that **shines** with it's "
                        + "*rays* on the **beautiful serene pond** as the *swans gracefully go by* in the evening.", TextType.NORMAL_TEXT)
        result4 = node4.split_nodes_delimiter(node4.text)
        self.assertEqual(f"{result4}", "[TextNode(a beautiful sunshine , normal, None), "
                         + "TextNode(this is a sun, code, None), "
                         + "TextNode( that , normal, None), "
                         + "TextNode(shines, bold, None), "
                         + "TextNode( with it's , normal, None), "
                         + "TextNode(rays, italic, None), "
                         + "TextNode( on the , normal, None), "
                         + "TextNode(beautiful serene pond, bold, None), "
                         + "TextNode( as the , normal, None), "
                         + "TextNode(swans gracefully go by, italic, None), "
                         + "TextNode( in the evening., normal, None)]")
    def test_err(self):
        node = TextNode("here is the text", TextType.BOLD_TEXT)
        with self.assertRaises(Exception):
            node.split_nodes_delimiter(node.text)

if __name__ == "__main__":
    unittest.main()

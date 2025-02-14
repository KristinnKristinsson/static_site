import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()

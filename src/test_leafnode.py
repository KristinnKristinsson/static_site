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
    
    


if __name__ == "__main__":
    unittest.main()

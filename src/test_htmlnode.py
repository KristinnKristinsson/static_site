import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_rep(self):
        node1 = HTMLNode("p", "This is a string a paragraph really", None, None)
        node2 = HTMLNode("a", "Click me", None, {"href": "https://a.link"})
        self.assertNotEqual(node1, node2)
    
    def test_props(self):
        node3 = HTMLNode("a", "click me", None, {"href": "https://a.link"})
        node4 = HTMLNode("area", None, None, {"shape": "poly", "coords": "129,0,260,95,129,138"})
        node5 = HTMLNode("p", "just text", None, None)
        result = node3.props_to_html()
        result2 = node4.props_to_html()
        result3 = node5.props_to_html()
        self.assertEqual(result, ' href="https://a.link"')
        self.assertEqual(result2, ' shape="poly" coords="129,0,260,95,129,138"')
        self.assertEqual(result3, "")
    
    def test_iseq(self):
        node6 = HTMLNode("p", "same text")
        node7 = HTMLNode("p", "same text")
        node8 = HTMLNode("p", "same text", None, None)
        node9 = HTMLNode("p", "same text", None)
        self.assertEqual(node6, node7)
        self.assertEqual(node6, node8)
        self.assertEqual(node9, node8)

if __name__ == "__main__":
    unittest.main()

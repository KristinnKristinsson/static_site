import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        result = node.to_html()
        self.assertEqual(result, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_error(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", None)
            node.to_html()
        with self.assertRaises(ValueError):
            node3 = ParentNode("", [LeafNode("i", "italic text"),],)
            node3.to_html()
        with self.assertRaises(ValueError):
            node2 = ParentNode("p", "{'dic': 'nope'}")
            node2.to_html()
        
    def test_more(self):
        with self.assertRaises(ValueError):
            node = ParentNode("h2", [
            ParentNode("b", "Bold text"),
            ],)  
            node.to_html()
    def test_muliPar(self):          
        node2 = ParentNode("h2", [
        ParentNode("b", [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),],),
        ],)        
        result = node2.to_html()
        self.assertEqual(result, "<h2><b><b>Bold text</b>Normal text</b></h2>")
        
        


if __name__ == "__main__":
    unittest.main()

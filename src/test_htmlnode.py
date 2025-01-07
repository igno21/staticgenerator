import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "value", None, {"target": "_blank"})
        self.assertEqual(str(node), "HTMLNode(p, value, None, {'target': '_blank'})")

    def test_to_html(self):
        node = HTMLNode("p", "value", None, {"target": "_blank"})
        with self.assertRaises(NotImplementedError):
            print(node.to_html())

    def test_props_to_html(self):
        node = HTMLNode("p", "value", None, {"target": "_blank"})
        html = node.props_to_html()
        self.assertEqual(html, " target='_blank'")


class TestLeafNode(unittest.TestCase):
    def test_p(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf.to_html(), "<p>This is a paragraph of text.</p>")

    def test_a(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            leaf.to_html(), "<a href='https://www.google.com'>Click me!</a>"
        )

    def test_leaf_not_equal(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertNotEqual(leaf, leaf2)

    def test_leaf_equal(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        leaf2 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf, leaf2)


class TestParentNode(unittest.TestCase):
    def test_p(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_double_p(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node2 = ParentNode(
            "p",
            [
                node,
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            node2.to_html(),
            "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", [])
            node.to_html()

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()

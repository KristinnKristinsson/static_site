from htmlnode import ParentNode, HTMLNode, LeafNode
from textnode import TextNode
import macromarkdown
import micromarkdown


def markdown_to_html_node(markdown, lst_html_nodes = []):
    lst_html_nodes.clear()

    lst_texts = []
    blocks = macromarkdown.markdown_to_blocks(markdown)
    for i in range(0, len(blocks)):
        which_type = macromarkdown.block_to_block_type(blocks[i])
        txts = micromarkdown.split_nodes_delimiter(blocks[i])
        for text_nodes in txts:
            leaves = TextNode.text_node_to_html_node(text_nodes)
            lst_texts.append(leaves)
        the_parent = ParentNode(which_type.value, lst_texts)
        the_parent.to_html()

        lst_html_nodes.append(the_parent)
    return lst_html_nodes
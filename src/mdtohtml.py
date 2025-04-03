from htmlnode import ParentNode, HTMLNode, LeafNode
from textnode import TextNode
import macromarkdown
import micromarkdown
import re



def markdown_to_html_node(markdown, lst_html_nodes = []):
    lst_html_nodes.clear()

    lst_texts = []
    blocks = macromarkdown.markdown_to_blocks(markdown)
    for i in range(0, len(blocks)):
        lst_texts.clear()
        which_type, header_int = macromarkdown.block_to_block_type(blocks[i])
        blocks[i] = blocks[i].replace("``", "")
        blocks[i] = re.sub(r"^(#+)", "", blocks[i])
        if which_type.value == "ol":
            blocks[i] = re.sub(r"(\d). ", r"<li>\1. ", blocks[i])
            blocks[i] = re.sub(r"\n", "</li>\n", blocks[i])
            blocks[i] = blocks[i]+"</li>\n" 
        if which_type.value == "ul":
            blocks[i] = re.sub(r"- ", "<li>- ", blocks[i])
            blocks[i] = re.sub(r"\n", r"</li>\n", blocks[i])
            blocks[i] = blocks[i]+"</li>\n"
        
        txts = micromarkdown.split_nodes_delimiter(blocks[i])
        for text_nodes in txts:
            leaves = TextNode.text_node_to_html_node(text_nodes)
            lst_texts.append(leaves)
        if header_int != 0:
            the_parent = ParentNode(which_type.value+f"{header_int}", lst_texts)

        else:
            the_parent = ParentNode(which_type.value, lst_texts)
        the_parent_node = the_parent.to_html()

        lst_html_nodes.append(the_parent_node)
    str_html_node = "\n".join(lst_html_nodes)
    html_node_div = "<div>"+str_html_node+"</div>"
    return html_node_div
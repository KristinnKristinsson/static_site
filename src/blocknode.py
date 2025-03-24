#from htmlnode import HTMLNode
from enum import Enum
import re


class BlockType(Enum):
        PARAGRAPH = "paragraph"
        HEADING = "heading"
        CODE = "code"
        QUOTE = "quote"
        UNORDERED_LIST = "unordered list"
        ORDERED_LIST = "ordered list"

def markdown_to_blocks(text):
    if not isinstance(text, str):
        raise ValueError("Not a string object")
    result_block = []
    text = text.strip("\n")
    split_block = re.split(r"\n\n", text)
    for block in split_block:
        mini_blocks = re.split(r"  *", block)
        block = " ".join(mini_blocks).replace('\n ', '\n')
        result_block.append(block.strip())
    return result_block

def block_to_block_type(block):
    print(len(block))
    print(block)
    if re.search(r'(#)\1* (s?)(.*)', block, flags=re.DOTALL) != None:
        if re.search(r'(#)\1* (s?)(.*)', block, flags=re.DOTALL).span()[1] == len(block):
            return BlockType.HEADING
    elif re.search(r'```(s?)(.*)```', block, flags=re.DOTALL) != None:
        if re.search(r'```(s?)(.*)```', block, flags=re.DOTALL).span()[1] == len(block):
            return BlockType.CODE
    elif re.search(r'(> (.*)\n)(> (.*))', block, flags=re.DOTALL) != None: 
        if re.search(r'(> (.*)\n)(> (.*))', block, flags=re.DOTALL | re.MULTILINE).span()[1] == len(block):
            return BlockType.QUOTE
    elif re.search(r'(- (.*)\n)(- (.*))', block, flags=re.DOTALL) != None: 
        if re.search(r'(- (.*)\n)(- (.*))', block, flags=re.DOTALL).span()[1] == len(block):
            return BlockType.UNORDERED_LIST
    elif re.search(fr'(1. (.*))', block, flags=re.DOTALL ) != None: 
        digit = 0
        if re.search(fr'({digit+1}. (.*))', block, flags=re.DOTALL ).span()[1] == len(block):
            return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    raise Exception("Non-compatible text type.")


    
   
    
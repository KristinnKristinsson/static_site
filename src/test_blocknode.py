import unittest

import macromarkdown

class Testmacromarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
            This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = macromarkdown.markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        md2 = """
            The *italians do like* this kind of text


            where we get what we want
            and we want to get paid
            but it feels so bad
            to be so sad


            -except
            -when
            -we list it.


            DO YOU FEEL ME *OR* do you **feel** me

            I'm getting tired of this.
        """
        blocks = macromarkdown.markdown_to_blocks(md2)
        self.assertEqual(
            blocks,
            ['The *italians do like* this kind of text', 
             'where we get what we want\nand we want to get paid\nbut it feels so bad\nto be so sad', 
             '-except\n-when\n-we list it.', 
             'DO YOU FEEL ME *OR* do you **feel** me', 
             "I'm getting tired of this."],
        )

    def test_blocks_to_blocktype(self):
        md ="""
            ### The *italians do like* this kind of text


            1. Because this time I think it is different
            2. I mean I think you really like mee
            3. eheeee eeeeeeheeeeeee


             ```
             where we get what we want
             and we want to get paid
             but it feels so bad
             to be so sad 
             ```

             Lets just write some stupid text
             that has a couple of new lines
             and I'm sure its fine

             > and what we have here
             > is a little bit of quotes
             > to get us started

             > but mixing things
             - up should not
             2. work

             #### Just to keep it going

             "What will happen now?"


             - except
             - when
             - we list it.


             DO YOU FEEL ME *OR* do you **feel** me' 
             I'm getting tired of this. 

             5. Because this time I think it is different
             9. I mean I think you really like mee
             6. eheeee eeeeeeheeeeeee
        """
        blocks = macromarkdown.markdown_to_blocks(md)
        result = macromarkdown.block_to_block_type(blocks[0])
        self.assertEqual(f"{result}", "BlockType.HEADING")
        result2 = macromarkdown.block_to_block_type(blocks[1])
        self.assertEqual(f"{result2}", "BlockType.ORDERED_LIST")
        result3 = macromarkdown.block_to_block_type(blocks[2])
        self.assertEqual(f"{result3}", "BlockType.CODE")
        result4 = macromarkdown.block_to_block_type(blocks[3])
        self.assertEqual(f"{result4}", "BlockType.PARAGRAPH")
        result5 = macromarkdown.block_to_block_type(blocks[4])
        self.assertEqual(f"{result5}", "BlockType.QUOTE")
        result6 = macromarkdown.block_to_block_type(blocks[5])
        self.assertEqual(f"{result6}", "BlockType.PARAGRAPH")
        result7 = macromarkdown.block_to_block_type(blocks[6])
        self.assertEqual(f"{result7}", "BlockType.HEADING")
        result8 = macromarkdown.block_to_block_type(blocks[7])
        self.assertEqual(f"{result8}", "BlockType.PARAGRAPH")
        result9 = macromarkdown.block_to_block_type(blocks[8])
        self.assertEqual(f"{result9}", "BlockType.UNORDERED_LIST")
        result10 = macromarkdown.block_to_block_type(blocks[9])
        self.assertEqual(f"{result10}", "BlockType.PARAGRAPH")
        result11 = macromarkdown.block_to_block_type(blocks[10])
        self.assertEqual(f"{result11}", "BlockType.PARAGRAPH")
    def test_error_markdown(self):
        md = 5555555
        with self.assertRaises(ValueError):
            macromarkdown.markdown_to_blocks(md)
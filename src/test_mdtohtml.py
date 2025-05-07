import unittest

import mdtohtml

class TestMdToHtml(unittest.TestCase):
    maxDiff = None
    def test_different_types(self):
        md = "this is just normal text"
        md2 = "this is a text with **bold text** and *italic text* and `code`"
        md3 = "```A given code\n Should look like\n this```"
        md4 = "- an unordered list\n - should look like\n - this"
        md5 = "1. and an ordered list\n 2. should look like\n 3. this."
        md6 = "> everybody \n> likes \n> Raymond"
        md7 = "### Don't forget a header as well"
        md8 = "> *is* **this** the real life\n > *is* **this** just `fantasy`"
        md9 = "###### the *smallest* of the **headers** should be made"
        result = mdtohtml.markdown_to_html_node(md)
        result2 = mdtohtml.markdown_to_html_node(md2)
        result3 = mdtohtml.markdown_to_html_node(md3)
        result4 = mdtohtml.markdown_to_html_node(md4)
        result5 = mdtohtml.markdown_to_html_node(md5)
        result6 = mdtohtml.markdown_to_html_node(md6)
        result7 = mdtohtml.markdown_to_html_node(md7)
        result8 = mdtohtml.markdown_to_html_node(md8)
        result9 = mdtohtml.markdown_to_html_node(md9)
        self.assertEqual(result, "<div><p>this is just normal text</p></div>")
        self.assertEqual(result2, "<div><p>this is a text with <b>bold text</b> and <i>italic text</i> and <code>code</code></p></div>")
        self.assertEqual(result3, "<div><pre><code>A given code\nShould look like\nthis</code></pre></div>")
        self.assertEqual(result4, "<div><ul><li> an unordered list</li>\n<li> should look like</li>\n<li> this</li>\n</ul></div>")
        self.assertEqual(result5, "<div><ol><li> and an ordered list</li>\n<li> should look like</li>\n<li> this.</li>\n</ol></div>")
        self.assertEqual(result6, "<div><blockquote>> everybody \n> likes \n> Raymond</blockquote></div>")
        self.assertEqual(result7, "<div><h3> Don't forget a header as well</h3></div>")
        self.assertEqual(result8, "<div><blockquote>> <i>is</i> <b>this</b> the real life\n> <i>is</i> <b>this</b> just <code>fantasy</code></blockquote></div>")
        self.assertEqual(result9, "<div><h6> the <i>smallest</i> of the <b>headers</b> should be made</h6></div>")
    
    def test_all_together(self):
        md = """
            ### The *italians do like* this kind of text

            anything **else** than the first one

            1. Because `this time` I think it is different
            2. I mean I think you really like meee

            5. Because this time I think it is different
            9. I mean I think you really like mee
            6. eheeee eeeeeeheeeeeee


            ```
            where we get what we want
            and we **want** to get paid
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
        """
        result = mdtohtml.markdown_to_html_node(md)
        self.assertEqual(result, 
"""<div><h3> The <i>italians do like</i> this kind of text</h3>
<p>anything <b>else</b> than the first one</p>
<ol><li> Because <code>this time</code> I think it is different</li>
<li> I mean I think you really like meee</li>
</ol>
<p>5. Because this time I think it is different
9. I mean I think you really like mee
6. eheeee eeeeeeheeeeeee</p>
<pre><code>
where we get what we want
and we </code>want<b> to get paid
but it feels so bad
to be so sad 
</b></pre>
<p>Lets just write some stupid text
that has a couple of new lines
and I'm sure its fine</p>
<blockquote>> and what we have here
> is a little bit of quotes
> to get us started</blockquote>
<p>> but mixing things
- up should not
2. work</p>
<h4> Just to keep it going</h4>
<p>"What will happen now?"</p>
<ul><li> except</li>
<li> when</li>
<li> we list it.</li>
</ul>
<p>DO YOU FEEL ME <i>OR</i> do you <b>feel</b> me' 
I'm getting tired of this.</p></div>""")
        
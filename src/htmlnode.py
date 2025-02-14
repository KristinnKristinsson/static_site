class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise Exception(NotImplementedError)
    
    def props_to_html(self):
        the_props_string = ""
        if self.props == None:
            return the_props_string
        for key, value in self.props.items():
            the_props_string += f' {key}="{value}"'
        return the_props_string
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

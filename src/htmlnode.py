

class HTMLNode:

    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        result = ""
        for key in self.props:
            result +=f' {key}="{self.props[key]}"'

        return result

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):

    def __init__(self, value, tag = None, props = None):
        if value is None:
            raise ValueError("LeafNode error value missing")
        super().__init__(tag = tag, value = value, children = None, props = props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode error value missing")
        if self.tag == None:
            return self.value
        else return '<{self.tag}[{self.props}]>{self.value}</{self.tag}> '

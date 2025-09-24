

class HTMLNode:

    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        result = ""
        for key in self.props:
            result +=f' {key}="{self.props[key]}"'

        return result

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):

    def __init__(self, tag = None, value = None, props = None):
        if value is None:
            raise ValueError("LeafNode error value missing")
        super().__init__(tag = tag, value = value, children = None, props = props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode error value missing")
        if self.tag is None:
            return self.value
        
        attrs = self.props_to_html()
        return f'<{self.tag}{attrs}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    
    def __init__(self, tag, children, props = None):
        if tag is None:
            raise ValueError("ParentNode error tag missing")
        if children is None:
            raise ValueError("ParentNode error children missing")
        super().__init__(tag = tag, children = children, props = props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode error tag missing")
        if self.children is None:
            raise ValueError("ParentNode error children missing")
            
        inner = ""
        for child in self.children:
            inner += child.to_html()

        attrs = self._props_to_html() if hasattr(self, "_props_to_html") else ""
        return f"<{self.tag}{attrs}>{inner}</{self.tag}>"
        









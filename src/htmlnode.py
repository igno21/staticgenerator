from typing import List, Optional


class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: Optional[List["HTMLNode"]] | None = None,
        props: dict | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
        if (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.children
        ):
            return True
        else:
            return False

    def get_children_len(self) -> int:
        if self.children is not None:
            # Inside this block, the type checker knows self.children is List[HTMLNode]
            return len(self.children)
        else:
            return 0

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html = ""
        if self.props:
            for key, value in self.props.items():
                html += f" {key}='{value}'"
        return html


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: List["HTMLNode"], props: dict | None = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("tag is empty")
        if self.children is None or super().get_children_len() <= 0:
            raise ValueError("children is missing")

        html = f"<{self.tag}{super().props_to_html()}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        props: dict | None = None,
    ):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError()
        if not self.tag:
            return f"{self.value}"
        return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"

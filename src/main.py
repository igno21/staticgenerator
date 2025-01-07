from textnode import TextNode, TextType


def main():
    print("hello world")
    node = TextNode("this is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)


if __name__ == "__main__":
    main()

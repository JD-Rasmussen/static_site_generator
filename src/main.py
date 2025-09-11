
from textnode import TextNode, TextType

def main():
    node = TextNode(text='some anchor',text_type=TextType.LINK, url='http://localhost')
    print(node)

if __name__ == "__main__":
    main()


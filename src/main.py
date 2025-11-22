
from copystatic import copy_files_recursive
from textnode import TextNode, TextType

def main():
    node = TextNode(text='some anchor',text_type=TextType.LINK, url='http://localhost')
    print(node)

    copy_files_recursive("static/", "public/")



if __name__ == "__main__":
    main()


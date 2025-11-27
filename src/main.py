
from copystatic import copy_files_recursive
from textnode import TextNode, TextType
from generatepage import generate_page, generate_pages_recursive

def main():
    node = TextNode(text='some anchor',text_type=TextType.LINK, url='http://localhost')
    print(node)

    
    copy_files_recursive("static/", "public/")

    generate_pages_recursive(from_path ="content/" , dest_path = "public/" , template_path = "template.html" )

if __name__ == "__main__":
    main()


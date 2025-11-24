
from copystatic import copy_files_recursive
from textnode import TextNode, TextType
from generatepage import generate_page

def main():
    node = TextNode(text='some anchor',text_type=TextType.LINK, url='http://localhost')
    print(node)

    
    copy_files_recursive("static/", "public/")

    generate_page(from_path ="content/index.md" , dest_path = "public/index.html" , template_path = "template.html" )

if __name__ == "__main__":
    main()


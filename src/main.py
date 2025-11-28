
from copystatic import copy_files_recursive
from textnode import TextNode, TextType
from generatepage import generate_page, generate_pages_recursive
import sys

def main():

    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    
    if not basepath.startswith("/"):
        basepath = "/" + basepath
    if not basepath.endswith("/"):
        basepath = basepath + "/"


    
    copy_files_recursive("static/", "docs/")

    generate_pages_recursive(
        from_path ="content" , 
        template_path = "template.html", 
        dest_path = "docs" , 
        basepath=basepath )

if __name__ == "__main__":
    main()


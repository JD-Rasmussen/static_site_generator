
from copystatic import copy_files_recursive
from textnode import TextNode, TextType
from generatepage import generate_page, generate_pages_recursive
import sys

def main():

 #   sys.argv()

  #  node = TextNode(text='some anchor',text_type=TextType.LINK, url='http://localhost')
  #  print(node)

    
    copy_files_recursive("static/", "public/")

    generate_pages_recursive(from_path ="content" , template_path = "template.html", dest_path = "public" )

if __name__ == "__main__":
    main()


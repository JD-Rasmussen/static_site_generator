
import os
from markdown_to_html_node import markdown_to_html_node
from extract_markdowns import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown file
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    # Read template file
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    # Extract title
    title = extract_title(markdown_content)

    # Replace placeholders
    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    final_html = final_html.replace('href="/', f'href="{basepath}/')
    final_html = final_html.replace('src="/',  f'src="{basepath}/')

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write final HTML to file
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)



def generate_pages_recursive(from_path, template_path, dest_path, basepath):

    for root, _, files in os.walk(from_path):
        for fname in files:
            if not fname.lower().endswith(".md"):
                continue

            src_path = os.path.join(root, fname)
            rel_path = os.path.relpath(src_path, from_path)            # e.g., "blog/post.md"
            rel_no_ext, _ = os.path.splitext(rel_path)                # e.g., "blog/post"
            dest_dir = os.path.join(dest_path, rel_no_ext + ".html")  # e.g., "public/blog/post.html"

            # Ensure destination directory exists before writing
            os.makedirs(os.path.dirname(dest_dir), exist_ok=True)

            # Reuse your existing single-file generator
            generate_page(src_path, template_path, dest_dir, basepath)



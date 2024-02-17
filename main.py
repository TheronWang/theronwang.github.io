# This is a sample Python script.
import os
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.toc import TocExtension

from bs4 import BeautifulSoup

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def markdown_to_html(md_file_path):
    # Load Markdown file
    with open(md_file_path, 'r') as f:
        text = f.read()

    # Convert Markdown to HTML with math support
    extensions = ['fenced_code',
                  'meta',
                  CodeHiliteExtension(),
                  TocExtension(permalink=True)]
    
    html = markdown.markdown(text, extensions=extensions)
    return html


def insert_into_html(html_file_path, html_content_to_insert, div_id, output_html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')

    target_div = soup.find('div', id=div_id)
    if target_div:
        target_div.append(BeautifulSoup(html_content_to_insert, 'html.parser'))

    with open(output_html_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(str(soup))


def render_blog_html():
    md_blogs_fold = "blogs_md"
    for md_file in os.listdir(md_blogs_fold):
        md_file_path = os.path.join(md_blogs_fold, md_file)
        # Get html content from markdown file
        html_content_from_md = markdown_to_html(md_file_path)
        output_html_file_path = "blogs/" + md_file[:-3] + ".html"
        html_file_path = "blogs/template.html"
        div_id = "markdownContent"
        insert_into_html(html_file_path, html_content_from_md, div_id, output_html_file_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    render_blog_html()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

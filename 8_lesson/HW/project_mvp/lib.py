from model import blogs

def view_blogs(blogs):
    for number,blog in enumerate(blogs,1):
        print(f"{number}) {blog.title}")

def get_blog_number(blogs):
    view_blogs(blogs)
    number = input("Оберіть номер блогу:")
    if number.isdigit() and 0 < int(number) <= len(blogs):
        return int(number) - 1

def get_blog(blogs):
    blog_number = get_blog_number(blogs)
    if blog_number is not None:
        return blogs[blog_number]

def hr():
    print("="*45)

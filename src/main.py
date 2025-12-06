import os
import shutil

from copystatic import copy_contents
from gencontent import generate_pages_recursively

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    # Delete anything in the public directory
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    # Copy all static files from static to public
    print("Copying static directory to public directory...")
    copy_contents(dir_path_static, dir_path_public)
    print("Done!")
    # Generate a page from content/index.md using template.html and write it to public/index.html
    print("Generating content...")
    generate_pages_recursively(dir_path_content, template_path, dir_path_public)
    print("Done!")

main()
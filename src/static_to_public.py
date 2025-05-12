import os, shutil, re, sys
import macromarkdown
import micromarkdown
from mdtohtml import markdown_to_html_node

def find_obj_dir():
    return "./docs"

def find_start_dir():
    return "../static_site/static"

def find_target_dir(basepath = "/"):
    try:
        sys.argv[1]
        if len(sys.argv) > 1:
            basepath = sys.argv[1]
    except IndexError:
        pass
    return basepath

def find_template():
    return "../static_site/template.html"

def find_content():
    return "../static_site/content"

def delete_public(target):
   if os.path.exists(target):
      for entry in os.listdir(target):
         full_path = os.path.join(target, entry)
         if os.path.isdir(full_path):
               shutil.rmtree(full_path)
         else:
               os.remove(full_path)

def paste_public(source, start, target):
   os.makedirs(target, exist_ok=True)

   for item in source:
      if isinstance(item, dict):
         for folder_name, nested_contents in item.items():
               new_source = os.path.join(start, folder_name)
               new_target = os.path.join(target, folder_name)
               paste_public(nested_contents, new_source, new_target)
      else:
         # It's a file
         src_file = os.path.join(start, item)
         dst_file = os.path.join(target, item)
         shutil.copy2(src_file, dst_file)


def navigate_static(start_dir):
    contents = []

    for entry in os.listdir(start_dir):
        full_path = os.path.join(start_dir, entry)
        if os.path.isdir(full_path):
            # Recurse into subfolder and store as {folder_name: contents}
            contents.append({entry: navigate_static(full_path)})
        else:
            # Append file name directly
            contents.append(entry)

    return contents



def paste_public_content(source, start, target, template_path, basepath):
    os.makedirs(target, exist_ok=True)

    for item in source:
        if isinstance(item, dict):
            for folder_name, nested_contents in item.items():
                new_source = os.path.join(start, folder_name)
                new_target = os.path.join(target, folder_name)
                paste_public_content(nested_contents, new_source, new_target, template_path, basepath)
        else:
            # It's a file
            generate_page(start + "/" + item, template_path, target, basepath)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating a webpage from {from_path} to {dest_path} using {template_path}\n Please hold...")
    finalized_article = ""
    md_path = open(from_path)
    md_content = md_path.read()
    temp_path = open(template_path)
    temp_content = temp_path.read()
    html_finalized = markdown_to_html_node(md_content)
    header = micromarkdown.extract_title(md_content)
    rpls_content = re.sub("{{ Content }}", html_finalized, temp_content)
    rpls_paths = re.sub("{{ basepath }}", basepath, rpls_content)
    finalized_article = re.sub("{{ Title }}", header, rpls_paths)
    name_of_file = re.findall(r"\w+.\w+$", from_path)
    the_path = re.sub(r"\w+.\w+", "", from_path)
    the_file = re.sub(".md", ".html", name_of_file[0] )
    save_path = os.path.join(dest_path, the_file)

    with open(save_path, "w") as f:
            f.write(finalized_article)

def create_content():
    from_path = find_content()
    template_path = find_template()
    basepath = find_target_dir()
    dest_path = find_obj_dir()
    structure = navigate_static(from_path)
    paste_public_content(structure, from_path, dest_path, template_path, basepath)
    # paste_public(structure, from_path, dest_path)

def static_to_public():
   obj_dir = find_obj_dir()
   start = find_start_dir()
   target = find_target_dir()
   source = navigate_static(start)
   delete_public(obj_dir)
   paste_public(source, start, obj_dir)
   



    # header_page = ""
    # content_md = ""
    # finalized_article = ""

    # with open(from_path, "w") as md_file:
    #     header_page = micromarkdown.extract_title(md_file)
    #     content_md = markdown_to_html_node(md_file)

        
    
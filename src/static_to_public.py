import os, shutil, re

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

def find_start_dir():
    return "../static_site/static"

def find_target_dir():
    return "../static_site/public"
    

def static_to_public():
   start = find_start_dir()
   target = find_target_dir()
   source = navigate_static(start)
   delete_public(target)
   paste_public(source, start, target)
   
   # Could be easy... easy like Python libraries, yeeeeah.
   # folder = "../static_site/public"
   # for filename in os.listdir(folder):
   #    file_path = os.path.join(folder, filename)
   #    try:
   #       if os.path.isfile(file_path) or os.path.islink(file_path):
   #             os.unlink(file_path)
   #       elif os.path.isdir(file_path):
   #             shutil.rmtree(file_path)
   #    except Exception as e:
   #       print('Failed to delete %s. Reason: %s' % (file_path, e))
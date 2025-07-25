import os
from config import *

def get_file_content(working_directory, file_path):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS) 
            file_content_string_capped = file_content_string + f'[...File "{file_path}" truncated at 10000 characters]'

            if len(f.read()) > MAX_CHARS:
                return file_content_string_capped
            return file_content_string
        
    except:
        return "Error: Error reading file!"
    
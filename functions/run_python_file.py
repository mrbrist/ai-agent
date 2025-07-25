import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        if len(args) > 0:
            complete = subprocess.run(["uv", "run", full_path, " ".join(args)], timeout=30, stdout=True, stderr=True)
            return f"STDOUT: {complete.stdout}\nSTDERR: {complete.stderr}"
        complete = subprocess.run(["uv", "run", full_path], timeout=30, stdout=True, stderr=True)
        return f"STDOUT: {complete.stdout}\nSTDERR: {complete.stderr}"

    except Exception as e:
        return f"Error: executing Python file: {e}"
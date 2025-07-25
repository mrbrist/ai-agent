from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file

from google import genai
types = genai.types

funcs = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
    "write_file": write_file
}

def call_function(function_call_part, verbose=False):
    func_name = function_call_part.name
    func_args = function_call_part.args

    if verbose:
        print(f"Calling function: {func_name}({func_args})")
    else:
        print(f" - Calling function: {func_name}")

    if func_name in funcs:
        response = funcs[func_name]("./calculator", **func_args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=func_name,
                    response={"result": response},
                )
            ],
        )
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=func_name,
                    response={"error": f"Unknown function: {func_name}"},
                )
            ],
        )
    

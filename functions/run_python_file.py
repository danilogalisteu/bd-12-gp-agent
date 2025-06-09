import os
import subprocess


def run_python_file(working_directory, file_path):
    wd = os.path.abspath(working_directory)
    if not os.path.isdir(wd):
        return f'Error: "{wd}" is not a directory'

    fp = os.path.abspath(os.path.join(working_directory, file_path))
    if not os.path.exists(fp):
        return f'Error: File "{file_path}" not found.'
    elif not os.path.isfile(fp):
        return f'Error: File "{file_path}" is not a regular file.'

    if not fp.startswith(wd):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not fp.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        res = subprocess.run(
            ["python3", fp],
            check=True,
            capture_output=True,
            text=True,
            cwd=wd,
            timeout=30,
        )
        out = ""
        if res.stdout:
            out += f"STDOUT:\n{res.stdout}\n"
        if res.stderr:
            out += f"STDERR:\n{res.stderr}\n"
        if res.returncode != 0:
            out += f"Process exited with code {res.returncode}"
        if not out:
            out = "No output produced.\n"
        return out
    except Exception as e:
        return f"Error: executing Python file: {e}"

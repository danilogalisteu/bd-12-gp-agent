import os


def write_file(working_directory, file_path, content):
    wd = os.path.abspath(working_directory)
    if not os.path.isdir(wd):
        return f'Error: "{wd}" is not a directory'

    fp = os.path.abspath(os.path.join(working_directory, file_path))
    if not fp.startswith(wd):
        return f'Error: Cannot write "{fp}" as it is outside the permitted working directory'

    try:
        with open(fp, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{fp}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"

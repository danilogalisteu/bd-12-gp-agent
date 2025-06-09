import os

MAX_CHARS = 10001


def get_file_content(working_directory, file_path):
    wd = os.path.abspath(working_directory)
    if not os.path.isdir(wd):
        return f'Error: "{wd}" is not a directory'

    fp = os.path.abspath(os.path.join(working_directory, file_path))
    if not os.path.isfile(fp):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    if not fp.startswith(wd):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    try:
        with open(fp, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) == MAX_CHARS:
                file_content_string = file_content_string[:MAX_CHARS-1] + f'[...File "{fp}" truncated at 10000 characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {e}"

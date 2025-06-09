import os


def get_files_info(working_directory, directory=None):
    wd = os.path.abspath(working_directory)
    if not os.path.isdir(wd):
        return f'Error: "{wd}" is not a directory'

    directory = directory if directory else "."
    cd = os.path.abspath(os.path.join(working_directory, directory))
    if not os.path.isdir(cd):
        return f'Error: "{directory}" is not a directory'

    if not cd.startswith(wd):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    files_info = []
    try:
        for entry in os.scandir(cd):
            files_info.append(f"- {entry.name}: file_size={entry.stat().st_size} bytes, is_dir={entry.is_dir()}")
    except Exception as e:
        return f"Error: {e}"

    return "\n".join(files_info)

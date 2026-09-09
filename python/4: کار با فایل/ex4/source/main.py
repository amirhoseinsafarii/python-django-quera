import os


def explore(extension: str, directory_path: str) -> dict[str, int]:
    result = {}
    for root, dirs, files in os.walk(directory_path):
        count = 0
        for file in files:
            name, ext = os.path.splitext(file)
            if extension.lower() == ext.lstrip(".").lower():
                count += 1
        if count > 0:
            result[root] = count

    return result

from os import walk, path
from file_entry import FileEntry


def get_file_entries_list(arg: str):
    file_entries_list: FileEntry = []
    for root, dirs, files in walk(arg, topdown=True):
        for name in files:
            file_path = path.join(root, name)
            file_name = name
            filename, file_extension = path.splitext(name)
            file_extension = file_extension.replace('.', '')
            file_size = path.getsize(file_path)
            file_entry = FileEntry(file_path, file_name, file_extension, file_size)
            file_entries_list.append(file_entry)
    return file_entries_list


def get_files_same_size(file_entries_list: list, is_descending: bool, file_format: str) -> dict:
    same_size_files = {}
    file_entries_list = sorted(file_entries_list, key=lambda entry: entry.file_size, reverse=is_descending)
    if file_format:
        file_entries_list = list(filter(lambda x: x.file_extension == file_format, file_entries_list))
    for file_entry in file_entries_list:
        if file_entry.file_size not in same_size_files:
            same_size_files[file_entry.file_size] = [file_entry]
        else:
            same_size_files[file_entry.file_size].append(file_entry)
    same_size_files = {x: y for x, y in same_size_files.items() if len(y) > 1}
    return same_size_files


def print_same_size_files(same_size_files):
    for key, values in same_size_files.items():
        print(f'{key} bytes')
        for value in values:
            print(value.file_path)
        print()

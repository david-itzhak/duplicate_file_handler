import hashlib
from file_entry import FileEntry


def calculate_file_entry_hash(file_entry: FileEntry):
    with open(file_entry.file_path, 'rb') as calculated_file:
        hash_object = hashlib.md5(calculated_file.read())
        hash_hexdigest: str = hash_object.hexdigest()
        file_entry.set_file_hash(hash_hexdigest)
    return hash_hexdigest, file_entry


def get_files_size_hash_dict(same_size_files: dict):
    files_size_hash_duplicates: dict = {}
    for file_size, file_entrys in same_size_files.items():
        for file_entry in file_entrys:
            calculate_file_entry_hash(file_entry)
    for size, hash_list in FileEntry.size_hash_dict.items():
        files_size_hash_duplicates[size] = {}
        for hash_ in hash_list:
            if len(FileEntry.file_hash_dict[hash_]) > 1:
                files_size_hash_duplicates[size][hash_] = FileEntry.file_hash_dict[hash_]
    return files_size_hash_duplicates


def print_files_size_hash_duplicates(files_size_hash_duplicates):
    current_index = 1
    for size, hash_group in files_size_hash_duplicates.items():
        print(f'{size} bytes')
        for hash_string, group in hash_group.items():
            print(f'Hash: {hash_string}')
            for file_entry in group:
                file_entry.set_current_index(current_index)
                print(f'{current_index}. {file_entry.file_path}')
                current_index += 1
        print()

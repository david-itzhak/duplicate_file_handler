from os import remove
from file_entry import FileEntry


def delete_files(files_indexes_to_delete):
    total_deleted_bytes = 0
    for index in files_indexes_to_delete:
        remove(FileEntry.current_index_dict[index].file_path)
        total_deleted_bytes += FileEntry.current_index_dict[index].file_size
    return total_deleted_bytes

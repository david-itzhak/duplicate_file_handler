from args_utils import get_dir_fom_args
from user_input_utils import get_user_preferences, get_user_choice_to_check_duplicates
from file_entries_utils import get_file_entries_list, get_files_same_size, print_same_size_files
from hash_utils import get_files_size_hash_dict, print_files_size_hash_duplicates
from file_entry import FileEntry


def main():
    arg = get_dir_fom_args()
    if arg is None:
        return
    file_format, is_descending = get_user_preferences()
    file_entries_list: FileEntry = get_file_entries_list(arg)
    same_size_files: dict = get_files_same_size(file_entries_list, is_descending, file_format)
    print_same_size_files(same_size_files)
    do_check_duplicate: bool = get_user_choice_to_check_duplicates()
    if do_check_duplicate:
        files_size_hash_duplicates: dict = get_files_size_hash_dict(same_size_files)
    print_files_size_hash_duplicates(files_size_hash_duplicates)


if __name__ == '__main__':
    main()


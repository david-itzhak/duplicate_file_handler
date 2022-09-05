from file_entry import FileEntry

def get_file_format_from_user():
    return input('Enter file format:\n')


def get_sorting_order_by_size():
    print('Size sorting options:', '1. Descending', '2. Ascending', sep='\n')
    while (order_option_number := input("Enter a sorting option:\n")) not in ('1', '2'):
        print('Wrong option\n')
    return order_option_number == '1'


def get_user_preferences():
    file_format: str = get_file_format_from_user()
    is_descending: bool = get_sorting_order_by_size()
    return file_format, is_descending


def get_user_choice_to_check_duplicates():
    while (check_for_duplicates := input('Check for duplicates?\n')) not in ('yes', 'no'):
        print('Wrong option')
    return check_for_duplicates == 'yes'


def get_user_choice_to_delete():
    while (check_for_duplicates := input('Delete files?\n')) not in ('yes', 'no'):
        print('Wrong option')
    return check_for_duplicates == 'yes'


def get_files_indexes_to_delete() -> list:
    while True:
        indexes_list_str = input('Enter file numbers to delete:\n').split()
        if indexes_list_str and all([item.isdigit() for item in indexes_list_str]):
            indexes_list = [int(x) for x in indexes_list_str]
            if all([item in FileEntry.current_index_dict for item in indexes_list]):
                return indexes_list
        print('Wrong format')
        continue

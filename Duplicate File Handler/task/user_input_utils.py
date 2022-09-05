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

from sys import argv


def get_dir_fom_args():
    if len(argv) > 1:
        return argv[1]
    else:
        print('Directory is not specified')
        return None

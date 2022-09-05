class FileEntry:
    size_hash_dict: dict = {}
    file_hash_dict: dict = {}
    current_index_dict: dict = {}

    def __init__(self, file_path, file_name, file_extension, file_size):
        self.file_path = file_path
        self.file_name = file_name
        self.file_extension = file_extension
        self.file_size = file_size
        self.file_hash = None
        self.current_index = None

    def __repr__(self):
        return f'''
file_path: {self.file_path}
file_name: {self.file_name}
file_extension: {self.file_extension}
file_size: {self.file_size}'''

    def set_file_hash(self, file_hash):
        self.file_hash = file_hash
        if file_hash in FileEntry.file_hash_dict:
            FileEntry.file_hash_dict[file_hash].append(self)
        else:
            FileEntry.file_hash_dict[file_hash] = [self]
        if self.file_size in FileEntry.size_hash_dict:
            FileEntry.size_hash_dict[self.file_size].append(file_hash)
        else:
            FileEntry.size_hash_dict[self.file_size] = [file_hash]

    def set_current_index(self, current_index):
        self.current_index = current_index
        FileEntry.current_index_dict[current_index] = self



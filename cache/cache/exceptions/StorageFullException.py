class StorageFullException(Exception):
    def __init__(self, massage: str):
        super(StorageFullException, self).__init__(massage)

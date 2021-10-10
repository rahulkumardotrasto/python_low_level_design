class NotFoundException(Exception):
    def __init__(self, massage: str):
        super(NotFoundException, self).__init__(massage)

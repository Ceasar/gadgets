

class swap(object):
    def __init__(self, filename):
        self.filename = filename
        self.swap = None

    def __enter__(self, mode='w'):
        self.swap = open(self.filename + '~', mode)

    def __exit__(self):
        self.swap.close()
        shutil.copyfile(self.swap.name, self.filename)
        os.remove(self.copy.name)

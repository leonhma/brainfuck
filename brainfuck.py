# pylama:ignore=C901
from sys import argv


# stolen from stackoverflow
class ilist(list):
    def __init__(self, r=None, dft=None):
        if r is None:
            r = []
        list.__init__(self, r)
        self.dft = dft

    def _ensure_length(self, n):
        maxindex = n
        if isinstance(maxindex, slice):
            maxindex = maxindex.indices(len(self))[1]
        while len(self) <= maxindex:
            self.append(self.dft)

    def __getitem__(self, n):
        self._ensure_length(n)
        return super(ilist, self).__getitem__(n)

    def __setitem__(self, n, val):
        self._ensure_length(n)
        return super(ilist, self).__setitem__(n, val)


cells = ilist(dft=0)
i = 0


def parse_chars(str):
    global cells, i
    progress = 0
    for str_i, char in enumerate(str):
        if progress > str_i:
            continue
        if char == '+':
            cells[i] += 1
            if cells[i] == 256:
                cells[i] = 0
        elif char == '-':
            cells[i] -= 1
            if cells[i] == -1:
                cells[i] = 255
        elif char == '<':
            i -= 1
            i = 0 if i < 0 else i
        elif char == '>':
            i += 1
        elif char == ',':
            inpt = input('user input: ')
            inpt = inpt if inpt != '' else '_'
            cells[i] = ord(inpt[:1])
        elif char == '.':
            print(chr(cells[i]), end='')
        elif char == '[':
            loop = str[str_i+1:str.index(']', str_i+1)]
            parse_chars(loop)
            while(cells[i] != 0):
                parse_chars(loop)
            progress += len(loop)
        progress += 1


with open(argv[1], 'r') as f:
    parse_chars(f.read())

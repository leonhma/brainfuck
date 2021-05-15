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
inputqueue = ''


def scanfor(string, check, closing, frm):
    nestedlevel = 0
    for end, char in enumerate(string[frm:]):
        if char == check:
            nestedlevel += 1
        elif char == closing and nestedlevel == 0:
            break
        elif char == closing:
            nestedlevel -= 1
    return string[frm:frm+end]


def parse_chars(string):
    global cells, i, inputqueue
    progress = 0
    for str_i, char in enumerate(string):
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
            if(len(inputqueue) == 0):
                inpt = ''
                while(inpt == ''):
                    inpt = input('user input: ')
                inputqueue += inpt
            inputqueue, inpt2 = inputqueue[1:], inputqueue[0]
            cells[i] = ord(inpt2)
        elif char == '.':
            print(chr(cells[i]), end='')
        elif char == '[':
            loop = scanfor(string, '[', ']', str_i+1)
            while(cells[i] != 0):
                parse_chars(loop)
            progress += len(loop)+1
        elif char == ']':
            loop = scanfor(string, ']', '[', str_i+1)
            while(cells[i] != 0):
                parse_chars(loop)
            progress += len(loop)+1
        progress += 1


with open(argv[1], 'r') as f:
    parse_chars(f.read())

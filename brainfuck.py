from sys import argv


cells = [0] * 100
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
            while(cells[i] != 0):
                parse_chars(loop)
            progress += len(loop)
        progress += 1


with open(argv[1], 'r') as f:
    parse_chars(f.read())

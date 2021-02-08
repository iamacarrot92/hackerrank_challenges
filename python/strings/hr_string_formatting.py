def print_formatted(number):
    width = len(bin(number).replace('0b',''))

    for x in range(1,number + 1):
        n = str(x).rjust(width, ' ')
        o = oct(x).replace('0o','').rjust(width,' ')
        h = hex(x).replace('0x','').upper().rjust(width,' ')
        b = bin(x).replace('0b','').rjust(width,' ')

        print(n, o, h, b)

n = int(input())
print_formatted(n)


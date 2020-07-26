
def print_formatted(number):
    decimal_number = 0
    octal_number = 0
    hexadecimal_number = 0
    binary_number = 0

    max_width = len(bin(number).lstrip('-0b'))

    for i in range (1, number + 1):
        decimal_number = str(i).rjust(max_width)
        octal_number = str(oct(i)).lstrip('-0o').rjust(max_width)
        hexadecimal_number = str(hex(i)).lstrip('0x').upper().rjust(max_width)
        binary_number = str(bin(i)).lstrip('-0b').rjust(max_width)

        print('{} {} {} {}'.format(decimal_number, octal_number, hexadecimal_number, binary_number))

print_formatted(10)
def symbol_to_binary(number, bits):
    binary = '{0:b}'.format(int(number))
    return '{0}{1}'.format('0' * (bits - len(binary)), binary)

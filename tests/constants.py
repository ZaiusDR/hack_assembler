CODE = [
    '@0',
    'D=M',
    '@INFINITE_LOOP',
    'D;JLE',
    '@counter',
    'M=D',
    '@SCREEN',
    'D=A',
    '@address',
    'M=D',
    '(LOOP)',
    '@address',
    'A=M',
    'M=-1',
    '@address',
    'D=M',
    '@32',
    'D=D+A',
    '@address',
    'M=D',
    '@counter',
    'MD=M-1',
    '@LOOP',
    'D;JGT',
    '(INFINITE_LOOP)',
    '@INFINITE_LOOP',
    '0;JMP']

INSTRUCTIONS = ('''0000000000000000
1111110000010000
0000000000010111
1110001100000110
0000000000010000
1110001100001000
0100000000000000
1110110000010000
0000000000010001
1110001100001000
0000000000010001
1111110000100000
1110111010001000
0000000000010001
1111110000010000
0000000000100000
1110000010010000
0000000000010001
1110001100001000
0000000000010000
1111110010011000
0000000000001010
1110001100000001
0000000000010111
1110101010000111''')
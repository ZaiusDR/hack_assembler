from hackassembler import constants
from hackassembler import instructions


def test_instruction_instruction_type():
    assert instructions.Instruction.instruction_type('@A_instr') == 'A'
    assert instructions.Instruction.instruction_type('notA_instr') == 'C'


def test_a_instruction__parse():
    symbol_line = '@R1'
    reference_line = '@100'
    label_line = '@LABEL'
    variable_line = '@variable'

    # Predefined
    instruction = instructions.AInstruction(symbol_line)
    return_symbol = instruction._parse()
    assert instruction.type == constants.A_PREDEF_SYMBOL
    assert instruction.parsed_instruction == '1'
    assert not return_symbol

    # Direct address reference
    instruction = instructions.AInstruction(reference_line)
    return_symbol = instruction._parse()
    assert instruction.type == constants.A_REFERENCE
    assert instruction.parsed_instruction == '100'
    assert not return_symbol

    # Label
    instruction = instructions.AInstruction(label_line)
    return_symbol = instruction._parse()
    assert instruction.type == constants.A_SYMBOL
    assert not instruction.parsed_instruction
    assert return_symbol == 'LABEL'

    # Variable
    instruction = instructions.AInstruction(variable_line)
    return_symbol = instruction._parse()
    assert instruction.type == constants.A_SYMBOL
    assert not instruction.parsed_instruction
    assert return_symbol == 'variable'


def test_a_instruction_translate():
    symbol_line = '@R5'
    variable_line = '@variable'

    instruction = instructions.AInstruction(symbol_line)
    assert instruction.translate() == '0000000000000101'

    instruction = instructions.AInstruction(variable_line)
    assert instruction.translate() == 'variable'


def test_c_instruction__parse():
    d_equals_zero = 'D=0'
    m_equals_not_d = 'M=!D'
    m_and_d_equals_a_plus_one = 'MD=A+1'
    a_equals_not_m_jgt = 'A=!M;JGT'
    not_a_jle = '!A;JLE'

    instruction = instructions.CInstruction(d_equals_zero)
    instruction._parse()

    assert instruction.a_bit == '0'
    assert instruction.comp == '0'
    assert instruction.dest == 'D'
    assert not instruction.jmp

    instruction = instructions.CInstruction(m_equals_not_d)
    instruction._parse()

    assert instruction.a_bit == '0'
    assert instruction.comp == '!D'
    assert instruction.dest == 'M'
    assert not instruction.jmp

    instruction = instructions.CInstruction(m_and_d_equals_a_plus_one)
    instruction._parse()

    assert instruction.a_bit == '0'
    assert instruction.comp == 'A+1'
    assert instruction.dest == 'MD'
    assert not instruction.jmp

    instruction = instructions.CInstruction(a_equals_not_m_jgt)
    instruction._parse()

    assert instruction.a_bit == '1'
    assert instruction.comp == '!M'
    assert instruction.dest == 'A'
    assert instruction.jmp == 'JGT'

    instruction = instructions.CInstruction(not_a_jle)
    instruction._parse()

    assert instruction.a_bit == '0'
    assert instruction.comp == '!A'
    assert not instruction.dest
    assert instruction.jmp == 'JLE'


def test_c_instruction_translate():
    d_equals_zero = 'D=0'
    m_equals_not_d = 'M=!D'
    m_and_d_equals_a_plus_one = 'MD=A+1'
    a_equals_not_m_jgt = 'A=!M;JGT'
    not_a_jle = '!A;JLE'

    instruction = instructions.CInstruction(d_equals_zero)
    assert instruction.translate() == '1110101010010000'

    instruction = instructions.CInstruction(m_equals_not_d)
    assert instruction.translate() == '1110001101001000'

    instruction = instructions.CInstruction(m_and_d_equals_a_plus_one)
    assert instruction.translate() == '1110110111011000'

    instruction = instructions.CInstruction(a_equals_not_m_jgt)
    assert instruction.translate() == '1111110001100001'

    instruction = instructions.CInstruction(not_a_jle)
    assert instruction.translate() == '1110110001000110'


def test_c_instruction__get_dest_number():
    instruction = instructions.CInstruction('fake_instruction')
    instruction.dest = 'MD'
    assert instruction._get_dest_number() == 3

    instruction = instructions.CInstruction('fake_instruction')
    instruction.dest = 'AD'
    assert instruction._get_dest_number() == 6

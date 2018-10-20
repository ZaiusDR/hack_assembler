import abc

from hackassembler import constants
from hackassembler import helpers


class Instruction(abc.ABC):
    def __init__(self, instruction):
        self.instruction = instruction.strip()
        super().__init__()

    @abc.abstractmethod
    def _parse(self):
        pass

    @abc.abstractmethod
    def translate(self):
        pass

    @classmethod
    def instruction_type(self, instruction):
        if instruction.startswith('@'):
            return 'A'
        return 'C'


class AInstruction(Instruction):
    def __init__(self, instruction):
        self.type = None
        self.parsed_instruction = None
        super().__init__(instruction)

    def _parse(self):
        symbol_name = self.instruction.split('@')[1]
        if symbol_name in constants.PREDEF_SYMBOLS.keys():
            self.parsed_instruction = constants.PREDEF_SYMBOLS.get(symbol_name)
            self.type = constants.A_PREDEF_SYMBOL
        elif symbol_name.isdigit():
            self.parsed_instruction = symbol_name
            self.type = constants.A_REFERENCE
        else:
            self.type = constants.A_SYMBOL
            return symbol_name

    def translate(self):
        symbol_name = self._parse()
        if self.type in [constants.A_PREDEF_SYMBOL, constants.A_REFERENCE]:
            return '{0}{1}'.format(
                constants.A_PREFIX,
                helpers.symbol_to_binary(self.parsed_instruction, bits=15)
            )
        return symbol_name


class CInstruction(Instruction):
    def __init__(self, instruction):
        self.a_bit = '0'
        self.comp = None
        self.dest = None
        self.jmp = None
        super().__init__(instruction)

    def _parse(self):
        if '=' in self.instruction and ';' in self.instruction:
            self.comp = self.instruction.split('=')[1].split(';')[0]
            self.dest = self.instruction.split('=')[0]
            self.jmp = self.instruction.split(';')[1]
        elif '=' in self.instruction:
            self.dest, self.comp = self.instruction.split('=')
        elif ';' in self.instruction:
            self.comp, self.jmp = self.instruction.split(';')

        if 'M' in self.comp:
            self.a_bit = '1'

    def translate(self):
        self._parse()
        comp_bin = constants.COMPS[self.comp]
        if self.dest:
            dest_bin = helpers.symbol_to_binary(self._get_dest_number(), 3)
        else:
            dest_bin = '000'
        if self.jmp:
            jmp_bin = constants.JUMP[self.jmp]
        else:
            jmp_bin = '000'

        return '111{0}{1}{2}{3}'.format(
            self.a_bit, comp_bin, dest_bin, jmp_bin
        )

    def _get_dest_number(self):
        dest_num = 0
        if 'M' in self.dest:
            dest_num = dest_num + constants.DESTS['M']
        if 'D' in self.dest:
            dest_num = dest_num + constants.DESTS['D']
        if 'A' in self.dest:
            dest_num = dest_num + constants.DESTS['A']

        return dest_num

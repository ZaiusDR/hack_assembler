from hackassembler import constants
from hackassembler import helpers
from hackassembler import instructions


class Compiler():
    instruction_types = {
        'A': instructions.AInstruction,
        'C': instructions.CInstruction
    }

    def __init__(self, src_file):
        self.src_file = src_file
        self.labels = {}
        self.variables = {}
        self.variables_count = 0
        self.instructions = []
        self.code = []

    def compile(self):
        self._get_cleaned_code()
        self._get_loop_labels()

        line_num = 0
        for line in self.code:
            if line.startswith('('):
                continue

            instruction_class = self.instruction_types.get(
                instructions.Instruction.instruction_type(line)
            )
            instruction = instruction_class(line)
            translation = instruction.translate()
            if not translation.isdigit():
                if translation in self.labels.keys():
                    self.instructions.append(self.labels[translation])
                else:
                    if translation not in self.variables.keys():
                        self._set_new_variable(translation)
                    self.instructions.append(self.variables[translation])
            else:
                self.instructions.append(translation)
            line_num += 1

        self._write_to_file()

    def _write_to_file(self):
        with open(self.src_file.replace('.asm', '.hack'), 'w') as f:
            for instruction in self.instructions:
                f.write('{0}\n'.format(instruction))

    def _get_cleaned_code(self):
        with open(self.src_file) as f:
            for raw_line in f.readlines():
                line = self._clean_line(raw_line)
                if line == '':
                    continue
                self.code.append(line)

    def _clean_line(self, line):
        if '//' in line:
            line = line.split('//')[0]
        return line.strip()

    def _get_loop_labels(self):
        line_num = 0
        for line in self.code:
            if line.startswith('('):
                label = line.replace('(', '').replace(')', '')
                address = helpers.symbol_to_binary(line_num, bits=16)
                self.labels.update({label: address})
            else:
                line_num += 1

    def _set_new_variable(self, variable):
        address = helpers.symbol_to_binary(
            constants.VARS_START + self.variables_count, bits=16
        )
        self.variables.update({variable: address})
        self.variables_count += 1

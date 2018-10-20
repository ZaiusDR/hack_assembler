from unittest import mock

import constants
from hackassembler import compiler


def test__clean_line():
    comment_line = '  FAKE=INSTRUCTION   // Fake comment\n'
    only_comment_line = '// Fake comment\n'

    test_compiler = compiler.Compiler('fake_src')
    assert test_compiler._clean_line(comment_line) == 'FAKE=INSTRUCTION'
    assert test_compiler._clean_line(only_comment_line) == ''


def test__get_loop_labels():
    test_compiler = compiler.Compiler('fake_file')

    test_compiler.code = ['(LABEL1)', 'Fake_instruction', '(LABEL2)']
    test_compiler._get_loop_labels()
    expected_dict = {
        'LABEL1': '0000000000000000',
        'LABEL2': '0000000000000001'
    }
    assert test_compiler.labels == expected_dict


def test__set_new_variable():
    test_compiler = compiler.Compiler('fake_file')

    test_compiler._set_new_variable('variable1')
    expected_dict = {'variable1': '0000000000010000'}
    assert test_compiler.variables == expected_dict
    assert test_compiler.variables_count == 1

    test_compiler._set_new_variable('variable2')
    expected_dict = {
        'variable1': '0000000000010000',
        'variable2': '0000000000010001'
    }
    assert test_compiler.variables == expected_dict
    assert test_compiler.variables_count == 2


@mock.patch.object(compiler.Compiler, '_write_to_file')
@mock.patch.object(compiler.Compiler, '_get_cleaned_code')
def test_compile(get_cleaned_code_mock, write_to_file_mock):
    test_compiler = compiler.Compiler('fake_file')
    test_compiler.code = constants.CODE
    test_compiler.compile()

    get_cleaned_code_mock.assert_called_once()
    write_to_file_mock.assert_called_once()

    assert '\n'.join(test_compiler.instructions) == constants.INSTRUCTIONS

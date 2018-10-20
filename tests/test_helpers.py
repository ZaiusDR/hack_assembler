from hackassembler import helpers


def test_symbol_to_binary():
    assert helpers.symbol_to_binary('1', 4) == '0001'
    assert helpers.symbol_to_binary('512', 15) == '000001000000000'

from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import encrypt,decrypt,crack

def test_version():
    assert __version__ == '0.1.0'

def test_encrypt():
    actual = encrypt('Wow a dark and stormy night.',3)
    expected = 'Zrz d gdun dqg vwrupb qljkw.'
    assert actual == expected

def test_decrypt():
    actual = decrypt('Zrz d gdun dqg vwrupb qljkw.',3)
    expected = 'Wow a dark and stormy night.'
    assert actual == expected

def test_crack():
    actual = crack('Zrz d gdun dqg vwrupb qljkw.')
    expected = 'Wow a dark and stormy night.'
    assert actual == expected

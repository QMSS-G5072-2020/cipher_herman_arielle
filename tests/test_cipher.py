import pytest

def cipher(text, shift, encrypt=True):
    # add assert statement
    assert not isinstance(shift, str), 'please enter numeric value for shift'
    
    alphabet = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

def test_cipher_one_word():
    actual = cipher("foobar", 1, encrypt=True)
    expected = "gppcbs"
    assert actual == expected

def test_cipher_neg_shift():
    actual = cipher("foobar", -1, encrypt=True)
    expected = "ennaZq"
    assert actual == expected

def test_cipher_not_alphabet():
    actual = cipher("foobar1", 1, encrypt=True)
    expected = "gppcbs1"
    assert actual == expected

def test_cipher_assert_shift_string():
    with pytest.raises(AssertionError):
        cipher("foobar", "one", encrypt=True)


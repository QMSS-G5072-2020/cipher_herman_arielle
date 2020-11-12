def cipher(text, shift, encrypt=True):
        """ 
        Encrypts and decrypts text.
        
        Parameters
        __________
        text: text string to be encrypted or decrypted.
            A text string, which can be a word or a phrase.
        shift: the number of letters each letter of the text string is shifted along the alphabet.
            A postive or negative integer.
        encrypt: Boolean which selects to encrypt (True) or decrypt (False).
            True or False
        
        Returns
        --------
        A text string

        Examples
        ---------
        >>> from cipher_aeh2196 import cipher_aeh2196
        >>> text = "foo bar"
        >>> shift = 1
        >>> cipher(text, shift, encrypt=True)
        'gpp cbs'
        """
        
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


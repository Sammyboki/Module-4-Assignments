'''Module 3: Individual Programming Assignment 1
Thinking Like a Programmer
This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.
    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "
    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 
    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    def shift_letter(letter,shift):
        order = alphabet.index(letter)
        print(letter)

        final_place = order + shift
        if final_place <= 25:
            alphabet[final_place]= letter
            print(alphabet)
        elif final_place > 25:
            final_place = final_place - 26
            alphabet[final_place]= letter
            print(alphabet)

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    new_message = []
    new_str = ''
    def caesar_cipher(message, shift):
        message_list = list(message)
        amount = len(message_list)
        i = 0
        for i in range(len(message_list)):
            if message_list[i] == " ":
                new_message.extend([" "])
                i += 1
            
            elif message_list[i] != " ":
                new_place = alphabet.index(message[i]) - shift
                new_letter = alphabet[new_place]
                new_message.extend([new_letter])
                i += 1
           
        new_str = ''.join(map(str,new_message))
        print (new_str)

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.
    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.
    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    def shift_by_letter(letter, letter_shift):
    
        order = alphabet.index(letter)
        shift = alphabet.index(letter_shift)
  
        final_place = order + shift
        if final_place <= 25:
            alphabet[final_place]= letter
            print(alphabet)
        elif final_place > 25:
            final_place = final_place - 26
            alphabet[final_place]= letter
            print(alphabet)

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.
    Example:
    vigenere_cipher("A C", "KEY") -> "K A"
    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    def vigenere_cipher(message, key):
        key_list = []
        length = len(message)
        if len(key) == length:
            key_list = list(key)
        else:
            for i in range(length):
                key_list.append(key[i%len(key)])
                i += 1
        key_string = ''.join(map(str,key_list))        
        print (key_string)
    
        message_list = list(message)
        new_message_list = []
        new_message =""
        for j in range(len(message_list)):
            if message_list[j] == " ":
                new_message_list.append(' ')
            
            else:
                movement = alphabet.index(message_list[j]) + alphabet.index(key_list[j])
                if movement >= 26:
                    movement -= 26
                    new_message_list.append(alphabet[movement])
                
                else:
                    new_message_list.append(alphabet[movement])
        
            new_message = ''.join(map(str,new_message_list))
    
        print (message)
        print (new_message)
        

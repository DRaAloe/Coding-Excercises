alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 5
shifted_alphabet = alphabet[shift:]
translation_table = str.maketrans(alphabet, shifted_alphabet)
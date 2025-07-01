"""
Задача 4.
Autokey Decoder


"""

import string

def positive_mod(a: int, b: int) -> int:
    b = abs(b)
    return a % b

def idx(letter: str) -> int:
    return ord(letter.upper()) - ord('A')

def number_to_letter(n: int) -> str:
    if n < 0 or n > 26:
        return "*"
    return chr(ord('A') + n)

def to_idxs(message : str) -> list:
    output = []
    for letter in message:
        code = idx(letter)
        if code >=0 and code <= 26:
            output.append(code)
        else: output.append(-1)
    return output

def to_text(codes : list):
    output = ""
    for code in codes:
        output += number_to_letter(code)
    return output

def is_recovered(text : str):
    for letter in text:
        if letter == "*": return False
    return True

def recover_digits(keystr, textstr, cipherstr):
    key = to_idxs(keystr)
    text = to_idxs(textstr)
    cipher = to_idxs(cipherstr)

    tlen = len(text)

    autokey = []
    for code in key:
        if len(autokey) >= tlen: break
        autokey.append(code)
    for code in text:
        if len(autokey) >= tlen: break
        autokey.append(code)

    for i in range(tlen):
        if autokey[i] == -1 and text[i] != -1:
            autokey[i] = positive_mod(cipher[i] - text[i], 26)
        if autokey[i] != -1 and text[i] == -1:
            text[i] = positive_mod(cipher[i] - autokey[i], 26)

    new_key = autokey[0:len(key)]
    new_text = autokey[len(key):] + text[tlen - len(key):]

    new_keystr = to_text(new_key)
    new_textstr = to_text(new_text)

    if new_keystr == keystr and new_textstr == textstr:
        return new_keystr, new_textstr
    
    return recover_digits(new_keystr, new_textstr, cipherstr)


def main():
    cipher = "GXILBGLQQJAIPWBMRKAZBWYKKKUCRKG"
    includes = "GESTURE"
    key_length = 6


    attempts = len(cipher) - len(includes) + 1

    for i in range(attempts):
        key = ''.join(["*" for _ in range(key_length)])
        text = ["*" for _ in range(len(cipher))]
        for j in range(i, i + len(includes)):
            text[j] = includes[j - i]
        text = ''.join(text)
        key, text = recover_digits(key, text, cipher)

        if is_recovered(key) and is_recovered(text):
            print("KEY:", key)
            print("TEXT:", text, "\n")
    
    
if __name__ == "__main__":
    main()

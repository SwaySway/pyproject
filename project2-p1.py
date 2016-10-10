import random
chars = 'abcdefghijklmnopqrstuvwxyz'


def key_gen():
    return sorted(chars, key=lambda k: random.random())


def substitution_encrypt(key, text):
    return ''.join(key[a] for a in text)


def substitution_decrypt(key, cipher):
    return ''.join(key[a] for a in cipher)


def error():
    print("Error!")


def encryption(*texts, key='bpzhgocvjdqswkimlutneryaxf', tag='E'):
    response = ""

    if tag == 'E':
        key = dict(zip(chars, key))
        for text in texts:
            response += substitution_encrypt(key, text)+" "
    elif tag == 'D':
        key = dict(zip(key, chars))
        for text in texts:
            response += substitution_decrypt(key, text)+" "
    else:
        error()
    return response


def main():

    result1 = encryption("flow", "substitutioncipher")
    print(result1)
    decrypt1 = encryption(result1.split()[0], result1.split()[1], tag='D')
    print(decrypt1+'\n')

    # generate new key
    new_key = key_gen()
    print("With a random generated key " + str(new_key))
    result2 = encryption("flow", "substitutioncipher", key=new_key)
    print(result2)
    decrypt2 = encryption(result2.split()[0], result2.split()[1], key=new_key, tag='D')
    print(decrypt2+'\n')

    print("Decrypting the following statements \"osiy\", \"obzy\", \"doedlugvusu\"")
    result3 = encryption("osiy", "obzy", "doedlugvusu", tag='D')
    print(result3)
    encrypt = encryption(result3.split()[0], result3.split()[1], result3.split()[2])
    print(encrypt)


if __name__ == "__main__":
    main()

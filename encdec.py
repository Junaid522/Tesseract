#!/usr/bin/python3
"""
Codename: Metatron
"""
import argparse
import base64
import os
import sys
from random import shuffle, randint, choice
from string import ascii_letters, digits

__author__ = 'sriram'
__version__ = "1.0"


class Metatron:
    """Metatron
    """
    __string = ascii_letters + digits + '!.-& ='
    __cipher_letters = ''
    __pad = list('?%!$#+!(@}:') + list(digits)

    def __crypt(self, plaintext, shift: int, stealth: bool = True) -> str:
        """
        :param plaintext: text to crypt/decrypt
        :param shift: a number
        :param stealth: if true then crypt, if false then decrypt
        :return: crypt/decrypt string
        """
        alphabet = ascii_letters
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        table = str.maketrans(alphabet, shifted_alphabet) if stealth else str.maketrans(shifted_alphabet, alphabet)
        return plaintext.translate(table)

    def __covert(self, key: str) -> str:
        """4 layers of defence
        :param key: text to covert
        :return: covert'ed text
        """
        shift = randint(15, 32)  # create a random shift
        k = self.__crypt(key, shift)  # cipher key with shift
        # pad the shift value (for deciphering)
        k = f'{k}{choice(self.__pad)}{shift}'
        k = k[::-1]  # reverse the key
        k = base64.b85encode(k.encode()).decode()  # b85encode
        # return the new cryptic key for storing
        # which will be used for decryption
        return k

    def __overt(self, key: str) -> str or None:
        """4 layers of defence
        :param key: text to overt
        :return: overt'ed text
        """
        try:
            key = base64.b85decode(key).decode()  # b85decode
            k = key[::-1]  # reverse the key
            shift = int(k[-2:])  # get the shift value
            k = k[:-3]  # get actual cryptic key
            k = self.__crypt(k, shift, False)  # decrypt key
        except:
            return None
        # return the original key for
        # encryption/decryption of message
        return k

    def cipher(self, text: str, key: str) -> str:
        """Cipher the given text
        :param text: text to cipher
        :param key: a key to use for ciphering
        :return: cipher'ed text
        """
        key = self.__overt(key)  # decode the key first
        if not key:
            return "Could not Encrypt - Result of Bad Key"
        try:
            trans = str.maketrans(self.__string, key)
        except:
            return "Could not Encrypt - Result of Bad Key"
        return text.translate(trans)

    def decipher(self, text: str, key: str) -> str:
        """Decipher the given text
        :param text: text to decipher
        :param key: a key to use to deciphering
        :return: decipher'ed text
        """
        key = self.__overt(key)  # decode the key first
        if not key:
            return "Could not Encrypt - Result of Bad Key"
        try:
            trans = str.maketrans(key, self.__string)
        except:
            return "Could not Decrypt - Result of Bad Key"
        return text.translate(trans)

    @property
    def cipher_key(self) -> str:
        """New cipher key on every call of this Getter
        Note: Generally this Getter is used to ONLY get a new cipher key 
        which inturn will be used for ciphering any text
        """
        self.__cipher_letters = list(self.__string)
        shuffle(self.__cipher_letters)
        self.__cipher_letters = ''.join(self.__cipher_letters)

        self.__cipher_letters = self.__covert(self.__cipher_letters)
        return self.__cipher_letters


def read_file(filename: str):
    """Return contents of only a valid text file
    """
    try:
        with open(filename, 'tr') as f:
            contents = f.read()
            return contents
    except:
        # not a text file
        return None


def write_file(contents: str, filename: str):
    with open(filename, 'tw') as f:
        f.write(contents)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cipher/Decipher messages/files!")
    parser.add_argument("-e", "--encrypt", dest="enc", action="store_true", default=True, help="Encrypt message!")
    parser.add_argument("-d", "--decrypt", dest="dec", action="store_true", default=False, help="Decrypt message!")
    parser.add_argument("-k", "--key", dest="key", default=None, help="Key to decrypt the message!")
    parser.add_argument("-n", "--new-key", dest="new_key", action="store_true", default=False,
                        help="Get a new key cipher/decipher to use!")
    parser.add_argument("-m", "--msg", dest="msg", default="Defend the World!", help="Message to encrypt!")
    parser.add_argument("-f", "--file", dest="file", help="File to encrypt!")

    args = parser.parse_args()
    plain_text = args.msg
    filename = args.file
    filecontents = None

    # instantiate metatron
    mt = Metatron() 

    # Get the actual key to be stored in DB & 
    # be used for ciphering and deciphering 
    # text in & out of DB
    ckey = None

    # arguments verification
    if args.new_key:
        print(f"Your key is (without quotes): '{mt.cipher_key}'")
        sys.exit(0)

    if args.dec:
        args.enc = False
        if not plain_text and not args.file:
            print(parser.print_help())
            sys.exit('Decrypt chosen, no message/file to decrypt!')
        if not args.key:
            print(parser.print_help())
            sys.exit('Decrypt chosen, no decryption key provided!')
        else:
            ckey = args.key

    if args.enc:
        if not plain_text and not args.file:
            print(parser.print_help())
            sys.exit('Encrypt chosen, no message/file to encrypt!')
        ckey = args.key or mt.cipher_key
    
    if filename:
        if not os.path.exists:
            sys.exit('File does not exist!')
        filecontents = read_file(filename)
        if not filecontents:
            sys.exit('Seems like file is not text file')
        plain_text = None
        new_filename = f"{os.path.splitext(filename)[0]}.{'enc' if args.enc else 'dec'}"

    print(f"decryption key used (without quotes''): '{ckey}'")
    print(f"Original {'text' if plain_text else 'file'}: {plain_text or filename}")
    if args.enc:
        # encryption
        if plain_text:
            ctext = mt.cipher(plain_text, ckey)
            print(f"ciphered text: {ctext}")
        elif args.file and filecontents:
            ctext = mt.cipher(filecontents, ckey)
            write_file(ctext, new_filename)
            print(f"Encrypted file is written into {new_filename}")

    if args.dec:
        # decryption
        if plain_text:
            dtext = mt.decipher(plain_text, ckey)
            print(f"deciphered text: {dtext}")
        elif args.file and filecontents:
            dtext = mt.decipher(filecontents, ckey)
            write_file(dtext, new_filename)
            print(f"Decrypted file is written into {new_filename}")

    print('')

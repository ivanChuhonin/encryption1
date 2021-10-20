def encrypt_caesar(plaintext: str, shift: int = 3):  # -> str:
    """
        Encrypts plaintext using a Caesar cipher.

        >>> encrypt_caesar("PYTHON")
        'SBWKRQ'
        >>> encrypt_caesar("python")
        'sbwkrq'
        >>> encrypt_caesar("Python3.6")
        'Sbwkrq3.6'
        >>> encrypt_caesar("")
        ''
    """
    tmp = [ord(c) for c in plaintext]
    A = []
    for i in tmp:
        if i in range(65, 91) or i in range(97, 123):
            if i > 90 - shift and i < 97:
                i = 64 - (90 - i)
            elif i > 122 - shift:
                i = 96 - (122 - i)
            i += shift
        A.append(i)
    result = [chr(c) for c in A]
    return ''.join(result)


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
        Decrypts a ciphertext using a Caesar cipher.

        >>> decrypt_caesar("SBWKRQ")
        'PYTHON'
        >>> decrypt_caesar("sbwkrq")
        'python'
        >>> decrypt_caesar("Sbwkrq3.6")
        'Python3.6'
        >>> decrypt_caesar("")
        ''
    """
    tmp = [ord(c) for c in ciphertext]
    A = []
    for i in tmp:
        if i in range(65, 91) or i in range(97, 123):
            if i < 65 + shift:
                i = 90 + (i - 64)
            elif i > 90 and i < 97 + shift:
                i = 122 + (i - 96)
            i -= shift
        A.append(i)
    result = [chr(c) for c in A]
    return ''.join(result)


def encrypt_vigenere_full(plaintext: str, keyword: str) -> str:
    base = 128 - 32
    l = len(plaintext)
    lk = len(keyword)
    repeatN = l // lk
    remainder = l % lk
    fullKey = keyword * repeatN + keyword[: remainder]
    result = []
    for idx, val in enumerate(plaintext):
        key = ord(plaintext[idx]) + ord(fullKey[idx])
        result.append(chr(key % base + 32))
    return ''.join(result)


def decrypt_vigenere_full(ciphertext: str, keyword: str) -> str:
    base = 128 - 32
    l = len(ciphertext)
    lk = len(keyword)
    repeatN = l // lk
    remainder = l % lk
    fullKey = keyword * repeatN + keyword[: remainder]
    result = []
    for idx, val in enumerate(ciphertext):
        key = ord(ciphertext[idx]) - 32 - ord(fullKey[idx]) + base
        result.append(chr(key % base))
    return ''.join(result)

dictA = [chr(i) for i in range(65, 91)]
dicta = [chr(i) for i in range(97, 123)]
dict = dictA + dicta

def findIdx(c):
    return dict.index(c)

def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    base = 52
    l = len(plaintext)
    lk = len(keyword)
    repeatN = l // lk
    remainder = l % lk
    fullKey = keyword * repeatN + keyword[: remainder]
    result = []
    for idx, val in enumerate(plaintext):
        key = findIdx(plaintext[idx]) + findIdx(fullKey[idx])
        result.append(dict[(key % base)])
    return ''.join(result)


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    base = 52
    l = len(ciphertext)
    lk = len(keyword)
    repeatN = l // lk
    remainder = l % lk
    fullKey = keyword * repeatN + keyword[: remainder]
    result = []
    for idx, val in enumerate(ciphertext):
        key = findIdx(ciphertext[idx]) - findIdx(fullKey[idx]) + base
        result.append(dict[(key % base)])
    return ''.join(result)

if __name__ == '__main__':
    # x = encrypt_caesar('1@ABCDabcdUuWXYZwxyz')
    x = encrypt_caesar('pYThoN3.8')
    print(x)
    print(decrypt_caesar(x))

    y = encrypt_vigenere('ATTACKATDAWN', 'LEMON')
    print(y)
    print(decrypt_vigenere(y, 'LEMON'))

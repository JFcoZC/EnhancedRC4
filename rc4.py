import time

def KSA(key):
    keylength = len(key)

    S = list(range(256))

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]  # swap

    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap

        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key):
    S = KSA(key)
    return PRGA(S)


if __name__ == '__main__':

    key = [chr(27), chr(89), chr(90), chr(12), chr(15)]
    plaintext = 'Eso es todo amigos'

    t1 = time.clock()
    def convert_key(s):
        return [ord(c) for c in s]
    key = convert_key(key)

    keystream = RC4(key)
     
    import sys
    for c in plaintext:
        sys.stdout.write("%02X" % (ord(c) ^ keystream.__next__()))
    print
    tf = time.clock()
    print("Execution time:", (tf-t1))
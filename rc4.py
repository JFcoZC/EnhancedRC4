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

    key = [27, 89, 90, 12, 15]
    plaintext = 'Lorem ipsum dolor sit amet, vix in alterum repudiandae, usu solum utinam perfecto an. Cum et tota eripuit denique, ad veri nostro aperiam pro. Per id impetus appellantur, vix verear aliquid signiferumque an, ne mea erant tempor erroribus. Perfecto referrentur consequuntur et his, sea ea case copiosae deterruisset, purto populo indoctum te qui. Sea delicata constituto ut, at ius assueverit consectetuer, discere oportere ex usu. Sint iusto ea ius. Reformidans concludaturque id mea, ne sea malorum legendos erroribus, id melius eleifend urbanitas sit. No sea ferri invenire intellegebat, meis neglegentur usu ex. Singulis torquatos pri ut. Nemore eruditi placerat at.'

    t1 = time.clock()
    def convert_key(k):
        s=[]
        for number in k:
            s.append(chr(number))
        return [ord(c) for c in s]
    key = convert_key(key)

    keystream = RC4(key)
     
    import sys
    for c in plaintext:
        sys.stdout.write("%02X" % (ord(c) ^ keystream.__next__()))
    print
    tf = time.clock()
    print("Execution time:", (tf-t1))
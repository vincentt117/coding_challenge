# From daily CodeSignal challenge: https://app.codesignal.com/challenge/s2Sjkmsv9DhMoKJ8W

def substitutionCipherDecryption(contents, signature, encryptedSignature):
    mapped_plain_text = set()
    cipher_to_plain = {}
    for ind, char in enumerate(encryptedSignature):
        cipher_to_plain[ord(char)] = ord(signature[ind])
        mapped_plain_text.add(ord(signature[ind]))
    plain_alpha_ind = 97
    cipher_alpha_ind = 97
    while cipher_alpha_ind < 123:
        while plain_alpha_ind in mapped_plain_text:
            plain_alpha_ind += 1
        if cipher_alpha_ind not in cipher_to_plain:
            cipher_to_plain[cipher_alpha_ind] = plain_alpha_ind
            mapped_plain_text.add(plain_alpha_ind)
        cipher_alpha_ind += 1
    decoded_list = []
    for let in contents:
        decoded_list.append(chr(cipher_to_plain[ord(let)]))
    return ''.join(decoded_list)
    


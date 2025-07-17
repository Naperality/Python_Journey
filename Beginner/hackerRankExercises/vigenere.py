def vigenere(str,key,direction = 1):
    result = ''
    key_index = 0
    for letter in str:
        if letter.isalpha():
            base = ord('A') if letter.isupper() else ord('a')
            offset = ord(key[key_index % len(key)].lower()) - ord('a')
            key_index += 1
            shift = (ord(letter) - base + offset * direction) % 26
            result += chr(base + shift)
        else:
            result += letter
    return result

print(vigenere('Hello World!', 'Python'))
print(vigenere('Wcesc Jdpek!', 'Python', -1))
            
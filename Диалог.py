ru_alphabet = []
for i in range(ord('А'), ord('Я') + 1):
    ru_alphabet.append(chr(i))
used_letters = []
def dialog_user():
    flag = True
    print(ru_alphabet)    
    while flag:
        letter = input('Введите букву русского алфавита: ').upper()
        if letter not in ru_alphabet:
            print('Это не буква русского алфавита! Еше раз')
            continue
        elif letter in used_letters:
            print(f'Вы уже использовали букву {letter}')
            continue
        else:
            used_letters.append(letter)
            ru_alphabet.remove(letter)
            flag = False
    print(used_letters)
    print(ru_alphabet)
    return letter
        
print(dialog_user())

play()
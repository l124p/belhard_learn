# Кодирование сообщения кодом Морзе

def code_morze(message):
    morze = {'A': '.-', 'B': '-...', 'C': '-.-', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
             'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
             'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
             'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
             '6': '-....', '7': '--...', '8': '---..', '9': '----.'
             }
    message_code = ''
    for i in message:
        if i == ' ':
            message_code += ' '
        else:
            try:
                message_code += morze.get(i.upper())
            except:
                return 'Ошибка шифрования, неизвестный  символ: ' + str(i)
    return message_code


print(code_morze(input('Введите сообщение: ')))

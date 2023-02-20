# Словарь количества символов в тексте

text = input("Enter text: ")
dic = {i: text.count(i) for i in text }
print(dic)

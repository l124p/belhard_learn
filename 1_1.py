# Заменить пробелы в предложении на '-'.
import re
str_hw = input("Enter string:")
print(str_hw.replace(' ', '-'))
print(re.sub(r' ', r'-', str_hw))

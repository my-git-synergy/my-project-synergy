num = 46275
ten_thousands = (num//10000)             # десятки тысяч
thousands = ((num % 10000)//1000)        # тысячи
hundreds = ((num % 1000)//100)           # тысячи
dozen = ((num % 100)//10)                # десятки
unit = (num % 10)                        # единицы

print(float(((dozen**unit)*hundreds)/(ten_thousands - thousands)))

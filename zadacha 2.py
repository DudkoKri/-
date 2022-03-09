#Задача 2: Напишите программы создания файла добавления в него записей,
# удаления записей, исправления записей, вывода содержимого файла на экран
# (все описать в функциях)

def Sozd(K):
    with open('exam.txt', 'w', encoding='utf-8') as K:
        K.write('1, 9, 3, Hello, No, Yes, 23')
    return K
def Dobavl(b):
    with open('exam.txt', 'a', encoding='utf-8') as K:
    b = K.write('100')
    return b
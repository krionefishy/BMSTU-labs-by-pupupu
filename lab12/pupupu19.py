# Лабораторная работа 12 
# Подготовил: Кошеваров Дмитрий
# Назначение программы: работа с текстовыми данными
import functions
import os



def clean_console():
    os.system("cls")
text = ["Использование меню предполагает, что пользователь может самостоятельно и",
            "многократно выбирать, какой из функций, заложенных в программе, ему",
            "воспользоваться. Это означает, что пронумерованный список всех действий",
            "должен быть выведен на экран в виде меню, а также должно быть оформлено",
            "приглашение ввода, предлагающее пользователю выбрать какой-либо пункт.",
            "После выполнения действия снова должно отображаться меню и приглашение",
            "ввода. Можно выводить меню не после каждого действия, а через 3-5 действий,",
            "но так, чтобы оно не пропадало за границы экрана. В меню должна быть",
            "предусмотрена возможность завершения программы.",
            "ppp123*1/123*2p"]
print("Ваш текст:")
# вывод текста в консоль
functions.show_file(text)
print()
# вывод списка комманд
functions.menu()
    # ввод данных 
n = input("Введите номер команды из меню: ")
    
while n != "8":
    flag = False
    match n:
        case "1":# текст сдвигаем влево
            functions.text_to_left(text)
            functions.show_file(text) 
        case "2":# текст сдвигаем вправо
            functions.text_to_right(text)
            functions.show_file(text)
        case "3":# текст по ширине
            functions.align_text_width(text)
            functions.show_file(text)
        case "4":# удаление слова
            word = input("Введите слово, которое надо удалить: ")
            functions.delete_current(text, word)
            functions.show_file(text)
        case "5":# замена слова 
            word1 = input("Введите слово, которое надо заменить: ")
            word2 = input("Введите слово, на которое надо заменить: ")
            functions.replace_current(text, word1, word2)
            functions.show_file(text)
        case "6":# вычисление выражения внутри текста
            functions.caclulate_from_string(text)    
            functions.show_file(text)
        case "7":# удаление самого частого слова
            print("Текст до изменения:")
            print()
            functions.show_file(text)
            print()
            word = functions.find_and_delete_current(text) 
            print(f"Слово которое нужно удалить - {word}")
            print()
            print("Измененный текст")
            print()
            functions.show_file(text)
        case _:
            print("ПУПУПУ, такой команды нет")
            n = input("Бу, испугался? Это я, разработчик,\n\
давай смотреть друг на друга, пока ты не введешь число из списка: ")
            flag = True
        
    functions.menu()
    if not flag: # докапываемся до пользователя, пока не введет норм команду
        n = input("Бу, испугался? Это я, разработчик,\n\
давай смотреть друг на друга, пока ты не введешь число из списка: ")

    clean_console()
else:
    print("(")      

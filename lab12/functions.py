from collections import Counter


def text_to_left(lines: list[str]):
    for i in range(len(lines)):
        lines[i] = " ".join(lines[i].split())
    
        

def text_to_right(lines: list[str]):
    mx = 0
    for i in lines:
        mx = max(mx, len(i))
            
    for i in range(len(lines)):
        lines[i] = " "*(mx - len(lines[i])) + lines[i]

                    
def align_text_width(lines: list[str]):
    mx = 0
    for i in lines:
        mx = max(mx, len(i))
            
    for i in range(len(lines)):
        n = len(lines[i].split())
        co = mx - sum([len(j) for j in lines[i].split()])
        if co == 0:
            res = lines[i]
        else:
            if n == 1:
                res = lines[i].strip()
            else:
                n -= 1
                res = (" "*(co // n)).join(lines[i].split())
                if co % n > 0:
                    res = res.replace(" ", " " * ((co % n) + 1), 1)
        lines[i] = res
    
    
def delete_current(lines: list[str], word: str):
    for i in range(len(lines)):
        lines[i] = " ".join([i for i in lines[i].split() if i.lower() != word.lower()])
    

def check_word(i: str, word1: str, word2: str):
    if i == word1 and word1[0] == word1[0].upper():
        return word2.capitalize()
    elif i == word1 and word1[0] == word1[0].lower():
        return word2
    else:
        return i
    
def replace_current(lines: list[str], word1: str, word2: str):
    if len(word1) == 0 or len(word2) == 0:
        return 
    
    for i in range(len(lines)):
        lines[i] = " ".join([check_word(i, word1, word2) for i in lines[i].split()])
        
        
def arithmetics(num1: float, num2: float, op) -> float:
    if op == "*":
        return num1 * num2
    
    if op == "/":
        return num1 / num2 

       
def calculus(line: str) -> str:
    if line.count("-") % 2 == 0:
        flag = True
    else:
        flag = False
    line = line.replace("-", "")
    if len(line) == 0:
        return ""
    if "/0" in line or "/*" in line or "*/" in line: 
        return "Балбес"
    
    while "//" in line or "**" in line:
        line = line.replace("**", "*")
        line = line.replace("//", "/")
    
    math_operations = [i for i in line if i == "*" or i == "/"]
    
    line = line.replace("*","/").split("/")
    if len(line) == 1:
        return line[0]
    res = int(line[0])
    for i in range(1,len(line)-1):
        res = arithmetics(res, int(line[i+1]), math_operations[i])
        if res == 0:
            return "0"
    if flag:
        return f"{res}"
    return f"-{res:.4g}"
        

def caclulate_from_string(lines: list[str]):
    start_of_numbers = 0
    flag = False
    end_of_numbers = 0
    
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            while " / " in lines[i] or " * " in lines[i]:
                lines[i] = lines[i].replace(" / ", "/")
                lines[i] = lines[i].replace(" * ", "*")
            if lines[i][j] in "-*/0123456789" and flag == False:
                flag = True
                start_of_numbers = j
            elif lines[i][j] in "-*/0123456789" and flag == True:
                end_of_numbers = j 
        
        result = calculus(lines[i][start_of_numbers:end_of_numbers+1])
        lines[i] = lines[i].replace(lines[i][start_of_numbers:end_of_numbers+1], result)




def find_and_delete_current(lines: list[str]):
    dct = {}
    for i in lines:
        i = i.split()
        for key, value in Counter(i).items():
            if key in dct:
                dct[key] += value 
            else:
                dct[key] = value
                
    word_to_delete = max(dct, key = lambda x: dct[x])
    newlines = [" ".join([i for i in j.split() if i != word_to_delete]) for j in lines]
    for i in range(len(lines)):
        lines[i] = newlines[i]
    
    return word_to_delete
        
def show_file(lines: list[str]):
    for i in lines:
        print(i)


def menu():
    print("Выберите действие: \n \
    1) Выровнять текст по левому краю \n \
    2) Выровнять текст по правому краю \n \
    3) Выровнять текст по ширине \n \
    4) Удалить все вхождения заданного слова \n \
    5) Замена одного слова другим во всем тексте \n \
    6) Вычисление арифметрических выражений \n \
    7) Задание по варианту \n \
    8) Завершить программу")
    print()
    
    
if __name__ == "__main__":
    #align_text_width("text.txt")
    #text_to_right("text.txt")
    '''find_and_delete_current(["пу пупу пупупу пу",
            "пупу пу пупу пупупу",
            "пупупу пупупу пупупу",
            "пупу",
            "пу пупупу пу пупу",
            "пупу пупу пупу пу"])'''
    filename = ["pupupupup",
           "ppp 123*1/123*2 p"]
    caclulate_from_string(filename)
    show_file(filename)
    pass
def counter(sent, letter):
    letter = letter.lower()
    return len([i for i in sent.split() if i.lower().startswith(letter)])


def get_num_of_words(text, letter):
    number_of_words = []
    current_sentence = ""
    for i in text:
        for j in i:
            if j == ".":
                number_of_words.append(counter(current_sentence, letter))
                current_sentence = ""
                
            else:
                current_sentence += j 
                
    return number_of_words.index(max(number_of_words))


def rewrite_sentences(text, index_of_sent):
    n = 0
    flag = True
    for i in range(len(text)):
        current_string = ""
        for j in text[i]:
            if j == ".":
                n += 1
                current_string += j
            if index_of_sent == n:
                flag = False 
                
            if j == "." and (not flag):
                flag = True
                continue    
            
            if flag:
                current_string += j
            else:
                current_string += ""
            
            
            
        text[i] = current_string.lstrip(".")
        

text = ['Его тело тоже менялось. Он всегда ', 
        'боялся обгореть, особенно потому 4+31-10 что ', 
        'был рыжим. Когда ему приходилось бывать ',
        'на солнце, он закутывался с ног до головы, ', 
        'надевал шляпу и никогда не забывал взять c зонтик ', 
        'из козьих шкур. Его кожа оставалась белой и ',
        'нежной, как у ощипанной курицы.']



rewrite_sentences(text, get_num_of_words(text, "о"))

for i in text:
    print(i)
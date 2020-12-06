import math
import string
#from math_v1 import*
from math_newCode import MathBot3, TaskToken
from string_number_v1 import translator, decads, digits


funcs_math = {'math': MathBot3, 'string-number': translator}


def returnOut(inputString):

    i = 0
    type_func = ""
    while inputString[i] != '|':
        type_func += inputString[i]
        i+=1
    string = inputString[i+1:]
    out = funcs_math[type_func](string)
    return out



def math_v4(taskString):
    tasks = []
    answers = []
    i = 0
    while i < len(taskString):
        if taskString[i] == '"':
            bounds = TaskToken(taskString, i+1, taskString[i])
            task = taskString[bounds[0]:bounds[1]] 
            i = bounds[1] #переход к индексу закрывающего разделителя
            if taskString[i] == ' ':
                i -= 1
            ans = returnOut(task)
            answers.append("\"" +ans+"\"")
            tasks.append(task)
        i += 1
            
    return " ".join(answers)



# inpt = input()
# print(math_v4(inpt))


def ToSymbolString(s):
    symbolStr = ''
    for i in range(len(s)):
        if s[i] != ' ':
            symbolStr += s[i]
    return symbolStr



def SolveTask(task):
    taskSymbol = ToSymbolString(task)
    ansArray = preoExpress(taskSymbol, len(taskSymbol))
    ans = AdaptOutput(ansArray)
    return ans



def TaskToken(taskString, startIndex, separator):
    for i in range(startIndex, len(taskString)):
        if taskString[i] == '"' and separator != '"':
            return TaskToken(taskString, i+1, '"')
        elif taskString[i] == separator:
            if i - startIndex == 0:
                return TaskToken(taskString, i+1, ' ')
            return [startIndex, i]
        


def DivTask(taskString):
    tasks = []
    answers = []
    i = 0
    while i < len(taskString):
        if taskString[i] == '"' or taskString[i] == ' ':
            bounds = TaskToken(taskString, i+1, taskString[i])
            task = taskString[bounds[0]:bounds[1]] 
            i = bounds[1] #переход к индексу закрывающего разделителя
            if taskString[i] == ' ':
                i -= 1
            ans = SolveTask(task)
            answers.append(ans)
            tasks.append(task)
        i += 1
            
    return answers           


def AdaptOutput(ansArray):
    if ansArray[1] == 0:
        return str(ansArray[0])
    elif ansArray[0] == 0:
        return str(ansArray[1])+'i'
    elif ansArray[1] < 0:
        return str(ansArray[0]) + str(ansArray[1]) + 'i'
    else:
        return str(ansArray[0]) + '+' + str(ansArray[1]) + 'i'
            
                 

def MathBot3(inputString):
    s = ' ' + inputString + ' "1"'
    output = DivTask(s)[:-1]
    return ' '.join(output)
    


#Working!!!

def mult(num1, num2):
    r = num1[0] * num2[0] - num1[1] * num2[1]
    im = num1[0] * num2[1] + num1[1] * num2[0]
    return [r, im]

def div(num, denom):
    r = int(num[0] / denom[0])
#     if r < 0 and num[0] % denom[0] != 0:
#         r = int(r) - 1
#     else:
#         r = int(r)
        
    im = int(num[1] / denom[0])
#     if im < 0 and num[1] % denom[0] != 0:
#         im = int(im) - 1
#     else:
#         im = int(im)
        
    return [r, im]

#Гарантируется, что мы не берём остаток от ДЕЛЕНИЯ НА комплексное
#И не берём остаток от ДЕЛЕНИЯ комплексного
def resid(num, denom):
    if denom[0] == 0:
        return 'Fail'
    elif num[0] < 0:
        res = abs(num[0])%denom[0] 
        return [-1*res, 0]
    return [num[0] % denom[0], 0]

def add(num1, num2):
    r = num1[0] + num2[0]
    im = num1[1] + num2[1]
    return [r, im]

def sub(num1, num2):
    r = num1[0] - num2[0]
    im = num1[1] - num2[1]
    return [r, im]

operations = {'+': add, '-': sub, '*': mult, '/': div, '%': resid}


#Working!!!

def slv_bracked(tarr):
    ans = [0, 0]
    tarr = [[0, 0], '+'] + tarr
    i = 3
    while i < len(tarr):
    #for i in range(3, len(tarr), 2):
        op = tarr[i]
        if op == '*' or op == '/' or op == '%':
            tarr[i+1] = operations[op](tarr[i-1], tarr[i+1])
            tarr = tarr[:i-1] + tarr[i+1:]
        else:
            i+=2
    for i in range(1, len(tarr), 2):
        op = tarr[i]
        ans = operations[op](ans, tarr[i+1])
    return ans    



#Must work...

def preoExpress(task, taskLen):
    i = 0
    if task[0] == '-':
        tarr = [[-1, 0], '*']
        i += 1
    elif task[0] == '(':
        tarr = [[1, 0], '*']
    else:
        tarr = [[0, 0], '+']
        
    while i < len(task):
    #for i in range (len(task)):
        el = task[i]
        
        if el == '(':
            if len(tarr[len(tarr) -1]) != 1:
                tarr.append('*')
            ans, delta = preoExpress(task[i+1:], taskLen - i - 1)
            i += delta + 2 #Возможно тут +2
            ans = slv_bracked(ans)
            tarr.append(ans)
        elif el == ')':
            return [tarr, i]
        elif el == 'i':
            i += 1
            if len(tarr[len(tarr) -1]) == 1:
                tarr.append([1, 0])
            #tarr.append(num)
            tarr.append('*')
            tarr.append([0, 1])
        elif (el == '-' or el == '+' or el == '*' 
            or el == '/' or el == '%'):
            i += 1
            #tarr.append(num)
            tarr.append(el)
            #tarr.append([0, 0])    
        else:
            if len(tarr[len(tarr) -1]) == 1:
                tarr.append([0, 0])
            elif i != 0 and task[i-1] == ')':
                tarr.append('*')
                tarr.append([0, 0])
            i += 1
            tarr[len(tarr) -1][0] = tarr[len(tarr) -1][0]*10 + int(el)
    #tarr.append(num)
    return slv_bracked(tarr)



PrinyatIslam = False
if PrinyatIslam:
    testString = '-15i/6'
    tStr = ' ' + testString + ' "3"'
    answers = DivTask(tStr)
    answers = answers[:-1]
    testAns = ' '.join(answers)
    print(testAns)


#ну как-то так вводится строка
inputString = str(input())
#и как-то так выходит ответ
outputAnswer = MathBot3(inputString)
#я конечно понимаю, что он должен ретёрниться, но он как бы и делает это
print(outputAnswer)

# inp = input()
# ans = 0
# ansarr = []
# while inp != 'no':
    
#     outpt = MathBot3(inp)
#     ans += int(outpt)
#     ansarr.append(int(outpt))
#     print(outpt)
#     inp = input()

# print(sum(ansarr))
# print(ans)



# test = input()

# preoExpress(test, len(test))


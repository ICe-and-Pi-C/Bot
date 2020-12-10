from OPD_Bot import*

test_case_math = [ ["1+2", "3"], ["1+3i", "1+3i"], ["(2+5i)*(2-5i)", "9"],
              ["1i+2i", "3i"], ["6i/(1-7)", "-i"], ["6i/-6", "-i"],
              ["5/7", "0"], ["5/-7", "0"], ["-5/7", "0"], ["-5/-7", "0"],
              ["5%7", "5"], ["5%(-7)", "5"], ["-5%7", "-5"], ["-5%(-7)", "-5"],
              ["19/7", "2"], ["19/-7", "-2"], ["-19/7", "-2"], ["-19/-7", "2"],
              ["19%7", "5"], ["19%(-7)", "5"], ["-19%7", "-5"], ["-19%(-7)", "-5"],
              [" 1   2", "1 2"], ["7/-7 27+5i-i 27+5i -i", "-1 27+4i 27+5i -i"],
              ["1 \"27 - 13\"  17(1+1)i  ", "1 14 34i"], ["(6*(2+4))  \"-7*(15-6)i\"  ", "36 -63i"],
              ["\"1\"  \"-2\"   \"7i\"  \"9\"   ", "1 -2 7i 9"] ]

test_case_statistics = [ ["median|83 12 63 91 -2 10 70 36 107", "63"],
                         ["max|99 99", "99"], 
                         ["firstmostfrequent|9 8 9 8 9 8 9 6 5", "9"],
                         ["min|5 -7 9 -100 1000 0", "-100"],
                         ["sum|5 4 1 -10 88 0 0 0 -38", "50"] ]

test_case_strNum = [ ["twenty-one million seventy-two thousand", "21072000"],
                     ["zero", "0"],
                     ["five billion seven", "5000000007"] ,
                     ["six hundred", "600"],
                     ["ten", "10"] ]

test_func = {'math': MathBot3,
             'statistics': statistics,
             'string-number': translator}

def start_test(test_case, func):
    for test in test_case:
        testString = test[0]
        true_ans = test[1]

        print("Тестируемая строка: ", testString)
        print("Правильный ответ: ", true_ans)

        ans = functions[func](testString)
        if ans == true_ans:
            print("Тест пройдён! Получен ответ: ", ans)
        else:
            print("Тест провален, был получен ответ: ", ans)
            break
    return "Всё!"

# start_test(test_case, math)

# Я написала тестировщика!!!

def Tester():
    print("Введите тип тестируемого задания")
    function = str(input())
    IsTesting = True
    if function == "shape":
        print("Мы ещё не написали эту функцию, эх...")
        IsTesting = False
    
    elif function == "determinant":
        print("Входные данные сломавси")
        IsTesting = False
    
    elif function == "inverse-matrix":
        print("Тут что-то сломалось внутри решающей функции")
        IsTesting = False
        
    elif not (function in functions):
        print("Чи шо?! Заданий такого типа нет")
        IsTesting = False
    
    if IsTesting:
        print("Введите тестируемую строку")
        inputString = input()
        print("Введите ответ, который должен получиться")
        trueOutput = input()
        getOutput = functions[function](inputString)
        if getOutput == trueOutput:
            print("Тест пройден! Мои поздравления!!!")
        else:
            print("Тест провалился... Это что, cypher?")
        print("Получен ответ:")
        print(getOutput)
    
    print("==================================================================\n")
    print("Продолжаем тестить? Введи \"yes\", если хочешь продолжить")
    IsNextTest = input()
    if IsNextTest == "yes":
        print("==================================================================\n\n")
        return Tester()
    
    return "Нет так нет, чё такой агрессивный то..."

#Tester()
import requests
import json
import math
import string
import time
import numpy as np
from datetime import datetime, date, time
#from sympy import *

#Импортирую коды функций в бот

from math_v1 import *
from determinant_v1 import *
from polinomial_root_v1 import*
from moment_v1 import*
from cypher_v1 import*
from statistics_v1 import*
from string_number_v1 import*
from inverse_matrix_v1 import*
from json_v1 import*
from math_random_v2 import math_v4

from tester_v1 import*


functions = {'math': MathBot3,
             'determinant': determinant,
             'polynomial-root': doPolynom,
             'moment': getMoment,
             'cypher': Cypher,
             'shape': 'Мы ещё не написали эту функцию',
             'statistics': statistics,
             'string-number': translator,
             'inverse-matrix': inverse,
             'json': json_task}




# team_token = '!bs1p2jp1DnVcq0mXzjmQUIH6TwKOX6'
# Round = 'projects-course-3'
# taskType = 'cypher'
# url = "https://task-challenge.azurewebsites.net/api/tasks/"

# n = 1
# while n != 0:
#     print("how many tasks to solve")
#     n = int(input())
#     for _ in range(n):
#         response = requests.post(url, params = {'secret': team_token, 'round': Round, 'type': taskType})
#         json_response = response.json()
#         print("You have a new task:")
#         print(f"TaskId:    {json_response['id']}")
#         print(f"TaskType:    {json_response['typeId']}")
#         print(f"Question:    {json_response['question']}")
#         task_type = json_response['typeId']
#         question = json_response['question']
#         task_id = json_response['id']
#         value = Cypher(question)
#         if (value == "Fail"):
#             break
#         print(f"Answer:    {value}")
#         answer = json.dumps({"answer": str(value)})
#         header = {'Content-Type':'application/json'}
#         response = requests.post(url + task_id, headers = header, params = {'secret': team_token}, data = answer)
#         json_response = response.json()
#         if json_response['status'] == 1:
#             print(f"Good work status was {json_response['status']}")
#             print("==================================================================\n\n")
#         else:
#             print(f"Err0r")
#             break


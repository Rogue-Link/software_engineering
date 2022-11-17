import random
import re
import string
class RandomElements:
    def random_int(x, y):
        x = int(x)
        y = int(y)
        return random.randint(x,y)
    def random_char():
        s=string.ascii_letters
        r = random.choice(s)
        return r
    def random_string(x, y):
        x = int(x)
        y = int(y)
        n = RandomElements.random_int(x,y)
        s = ""
        for i in range(0, n):
            s += RandomElements.random_char()
        return s
    def get_attack(type, n):
        type_list = []
        for item in type:
            type_list.append(re.findall(r"(int)\((\d+)\,(\d+)\)", item)) 
            type_list.append(re.findall(r"(char)", item)) 
            type_list.append(re.findall(r"(string)\((\d+)\,(\d+)\)", item)) 
        type_list = [ele for ele in type_list if ele != []]
        attack = []
        for i in range(0, n):
            list_1 = []
            for j in type_list:
                x = j[0]
                if x[0] == "int":
                    a = int(x[1])
                    b = int(x[2])
                    list_1.append(RandomElements.random_int(a, b))
                elif x[0] == "char":
                    list_1.append(RandomElements.random_char())
                elif x[0] == "string":
                    a = int(x[1])
                    b = int(x[2])
                    list_1.append(RandomElements.random_string(a, b))
                else :
                    print("error")
            attack.append(list_1)
        return attack


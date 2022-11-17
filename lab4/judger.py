import random
import string
import os
from sys import path_hooks
from runner import Runner
from outputter import Output
from inputter import Inputter
from random_elements import RandomElements
attack_times = 10
path = Inputter.gat_path()
files = os.listdir(path)
Output.init_output()
for file in files:
    print(file)
    if os.path.isdir(path + "/" +file):
        path_1 = path + "/" +file
        programs = os.listdir(path_1)
        with open(path_1 + "/" + 'stdin_format.txt', 'r') as f:
            type = f.readline()
            type = type.split(' ')
            attack_list = RandomElements.get_attack(type, attack_times)
        answer = {}
        for program_1 in programs:
            if program_1 == "put.txt" or program_1 == "stdin_format.txt" or program_1 == ".DS_Store":
                continue
            answer[program_1] = Runner.get_answer(program_1, attack_list, path_1)
            if os.path.exists(path_1 + "/" + "put.txt"):
                os.remove(path_1 + "/" + "put.txt")
        num = 0
        for program_1 in programs:
            num = num + 1
            if program_1 == "put.txt" or program_1 == "stdin_format.txt" or program_1 == ".DS_Store":
                continue
            for program_2 in programs[num:]:
                if program_2 == "put.txt" or program_2 == "stdin_format.txt" or program_2 == ".DS_Store" or program_1 == program_2:
                    continue
                a_list = answer[program_1]
                b_list = answer[program_2]
                path_2 = path_1.strip("./") + "/"
                gg = 0
                if len(b_list) != len(a_list):
                    Output.get_inequal_output(program_1, program_2, path_2)
                    gg = 1
                else:
                    for i in range(0, len(a_list)):
                        if a_list[i][0] != b_list[i][0] or a_list[i][0] != b_list[i][0]:
                            if gg == 0:
                                Output.get_inequal_output(program_1, program_2,path_2)
                            gg = 1
                            break
                    if gg == 0:
                        Output.get_equal_output(program_1, program_2,path_2)
Inputter.finish_program()



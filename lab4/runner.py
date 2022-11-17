import subprocess
import csv
class  Runner:
    def get_answer(file, attack_list, path):
        answer_list = []
        subprocess.run("g++ " + path + "/" + file, shell = True)
        for attack_row in attack_list:
            with open (path+"/"+"put.txt", 'w') as f:
                for i in attack_row:
                    f.write(str(i) + ' ')
            return_code = subprocess.run("cat " + path + "/" + "put.txt" + "|" + "./a.out > result.txt", shell = True)
            with open ("./result.txt", 'r') as f:
                reader = f.read()
            answer_row = []
            answer_row.append(reader)
            answer_row.append(return_code.returncode)
            answer_list.append(answer_row)
        return (answer_list)
        

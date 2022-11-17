import os
class Inputter:
    def gat_path():
        return './input'
    
    def finish_program():
        if os.path.exists("result.txt"):
            os.remove("result.txt")
        if os.path.exists("a.out"):
            os.remove("a.out")

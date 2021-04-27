import  SolveJson
import  GetCode
from stanfordkarel import *
filename = "2"
def main():
    """ Karel code goes here! """
    path = GetCode.search_path()
    exec("".join(path))

if __name__ == '__main__':

    #SolveJson.GetString(filename)
    #run_karel_program()
    print(GetCode.search_path(filename))

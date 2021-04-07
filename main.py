import  SolveJson
import  GetCode
from stanfordkarel import *

def main():
    """ Karel code goes here! """
    path = GetCode.search_path()
    exec("".join(path))

if __name__ == '__main__':

    filename = "2"
    #SolveJson.GetString(filename)
    run_karel_program()

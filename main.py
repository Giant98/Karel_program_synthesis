import  SolveJson
import  GetCode
from stanfordkarel import *

filename = "2"

def main():
    """ Karel code goes here! """
    path = GetCode.search_path(filename)
    exec("".join(path))

if __name__ == '__main__':

    #SolveJson.GetString(filename)
    #run_karel_program(filename_to_save="test2.w")
    print(GetCode.search_path(filename))

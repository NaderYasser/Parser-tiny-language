from functions import *
import re
import os


tokens = []

def vaild_next_char(i,n):
    if(i == n-1):
        return 0
    else:
        return 1

def classify(list_of_okens):
    return type

def get_tokens(line):
   # line = re.sub('[\s+]', '', line)
    state="start"

    token=""
    i=0
    char=line[i]


    no_valid_token = 0

    while(1):


        if(state=="start"):
            if (char==' '):
                i=i+1
                char = line[i]
                continue
            if isLetter(char):
                state="letter"
            elif isNumber(char):
                state = "number"
            elif isSpecial(char):
                state = "special"
            elif char=='{':
                state = "comment"
            else:
                no_valid_token = 1
        if state =="letter":
             while isLetter(char) or isNumber(char):
                 token += char
                 if (vaild_next_char(i, len(line))):
                     i = i + 1
                     char = line[i]
                     #no_valid_token = 0
                 else:
                     no_valid_token=1
                     break
             state = "acceptance"
        if state == "number":
            while isNumber(char):
                token += char
                if (vaild_next_char(i, len(line))):
                    i = i + 1
                    char = line[i]
                    #no_valid_token = 0
                else:
                    no_valid_token=1
                    break
            state = "acceptance"

        if state == "special":
            while isSpecial(char):
                token += char
                if (vaild_next_char(i, len(line))):
                    i = i + 1
                    char = line[i]
                    #no_valid_token = 0
                else:
                    no_valid_token = 1
                    break
            state = "acceptance"

        if state == "comment":
                while (char != '}'):
                    if (vaild_next_char(i, len(line))):
                        i = i + 1
                        char = line[i]
                     #   no_valid_token = 0
                    else:
                        no_valid_token=1
                        break
                state = "start"
                if (vaild_next_char(i, len(line))):
                    i = i + 1
                    char = line[i]

        if (state=="acceptance"):
            state = "start"
            tokens.append(token)
            token=""

        if ( no_valid_token and(not (vaild_next_char(i, len(line))))):
            break


def read_lines(filename):
    in_file = open(filename, "r")
    lines = in_file.readlines()

    for line in lines:
        get_tokens(line)
    in_file.close()





def main():
    read_lines('test.txt')
    list = classifier(tokens)
    text_file = open("Output.txt", "w")
    '''
    for key, values in list.items():
        print(key + "->", end =" ")
        for value in values:
            print(value + "," , end =" ")

        print("")
    '''
    for item in list:
        print(item)
        text_file.write(item)
        text_file.write("\n")

    text_file.close()

if __name__ == "__main__":
    main()

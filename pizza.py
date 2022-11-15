# Stacks of pizzas set in input.yaml as provided. You can make your own or change it. 
# the bottom of a stack in the leftv- it's the first element of the array.
# Ideas to improve: 
# - make a reversing option - right element of the array ia a bottom (.reverse())
# - make checking CLI args
# - make tests ( it can be performed in bash using input datafile just for fun)
# 
# Pay attention - if we have a stack with the first pizza with zero thickness I decide to avoid 
# double solution and have made a condition for it. Basically this task has two solutions in that 
# situation. 
# 
# Thank you, 
# Yuri Zholobov
# y.a.zholobov@gmail.com

import yaml, numbers, sys

def is_integer(name):    # finction for checking if all pizzas are integer 
    for i in range (0 , len(name["stacks"])):                   
        f = str(i+1)
        for j in range (0, len(name["stacks"][i]["stack_"+f])):
            if type(name["stacks"][i]["stack_"+f][j]) != int:
                print('Minimum one of your pizza is not integer')
                sys.exit() 

def set_input(input_filename):
    with open(input_filename) as infile : # open input file with set of stacks
         pizzas = yaml.load(infile, Loader=yaml.FullLoader) # define structure 
    return pizzas


if __name__ == "__main__":

    pizzas = set_input(sys.argv[1]) # define a set of stacks
    is_integer(pizzas) #checking if all pizzas are integer 
    
    ####################################### 
    
    for i in range (0 , len(pizzas["stacks"])):
        f = str(i+1) # convert int to string due to iteration by names
        level = 0    # define the base equal level 
        acc = 0      # an accumulator 

        if not ( pizzas["stacks"][i]["stack_"+f][0] == 0):  # if we have a pizza with 0 thickness in bottom we do not calculate levels
            pizzas["stacks"][i]["level_"+f] = [0]           # 
        else: pizzas["stacks"][i]["level_"+f] = []          # 
                                                         
        for j in range (0, len(pizzas["stacks"][i]["stack_"+f])): # make list of levels for each stack
            acc = acc + pizzas["stacks"][i]["stack_"+f][j]        # calculate next level
            pizzas["stacks"][i]["level_"+f].append(acc)           # add next level
        
        if i == 0:   # if it's first stack then it's equal itself
            union_level =  pizzas["stacks"][i]["level_"+f]        # set the crossing when only one stack
        else:        # go further to calculate crossings
            union_level = list( set(union_level) & set(pizzas["stacks"][i]["level_"+f]) ) # calculate the crossing with pre - itself
    
    ######################################
    
    max_equal_level = max(union_level)   # find max equal level
    print ('MAX equal level is --------->',max_equal_level) # output THE RESULT 
    print('------------')
    
    #######################################
    
    for i in range (0 , len(pizzas["stacks"])): # calculate number of pizzas to remove 
         f = str(i+1)                           # from each stack
         for j in range (0, len(pizzas["stacks"][i]["level_"+f])):
            if max_equal_level == pizzas["stacks"][i]["level_"+f][j]:
                print ('From', f ,'stack you must remove ', len(pizzas["stacks"][i]["level_"+f])-j-1 ,'pizzas' )
    print('------------')
    #######################################
    
    for i, v in enumerate(pizzas["stacks"]):                   # Output stacks
        print('Stack ',(i+1),'----', v["stack_"+str(i+1)])     # And levels 
        print('Levels ','-----', v["level_"+str(i+1)])          
        print('------------- ')                                 
    

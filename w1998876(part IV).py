#Initializing the variables
pass_credits_value=0
defer_credits_value=0
fail_credits_value=0
total = 0
repetition = "y"
list_1=[]
list_2=[]
list_3=[]
loop_count = 0
part_IV_dict= {}

#Input pass_credits
def pass_credits():
    credits_list = [0, 20, 40, 60, 80, 100, 120]
    while True:
        try:
            pass_credits_value = int(input("Please enter your total pass credits: "))
            if pass_credits_value in credits_list:
                break
            else:
                print("Out of range")
        except ValueError:
            print("Integer required")

    return pass_credits_value
    

#Input defer_credits
def defer_credits():
    credits_list = [0, 20, 40, 60, 80, 100, 120]
    while True:
        try:
            defer_credits_value = int(input("Please enter your total defer credits: "))
            if defer_credits_value in credits_list:
                break
            else:
                print("Out of range")
        except ValueError:
            print("Integer required")

    return defer_credits_value
   

#Input fail_credits
def fail_credits():
    credits_list = [0, 20, 40, 60, 80, 100, 120]
    while True:
        try:
            fail_credits_value = int(input("Please enter your total fail credits: "))
            if fail_credits_value in credits_list:
                break
            else:
                print("Out of range")
        except ValueError:
            print("Integer required")
    return fail_credits_value


#Determining the progression outcome based on pass and fail credits
def progression_outcome(pass_credits, fail_credits):
    

    if pass_credits == 120:
        print("Progress")
        list_1.append("Progress")
    

    elif pass_credits == 100:
        print("Progress (module trailer)")
        list_1.append("Progress (module trailer)")
        

    elif 0 <= fail_credits <= 60:
        print("Do not progress - module retriever")
        list_1.append("Module retriever")
       

    else:
        print("Exclude")
        list_1.append("Exclude")
       
def progression_credits_list(list_1, list_2):
    x = 0
    y = 3
    for i in list_1:
        credits = ', '.join(map(str, list_2[x:y]))
        print(i, " - " ,credits)
        y = y + 3
        x = x + 3

#Print the progression outcomes and their corresponding credits
def progression_outcome_dict(list_1,list_2,list_3):
    x=0
    y=3
    z=0
    for i in list_1:
        part_IV_dict[list_3[z]]=(str(i),"-",str(list_2[x:y]))
        y=y+3
        x=x+3
        z=z+1


#Create dictionary
    for a,b in part_IV_dict.items():
        values_str = ' '.join(map(str,b))
        print(f"{a}: {str(values_str).replace('[',' ').replace(']','')}",end = " ")
    

while repetition == "y":
    student_ID=input("Enter your Student ID:")
    list_3.append(student_ID)
    pass_credits_value = pass_credits()
    list_2.append(pass_credits_value)
    defer_credits_value = defer_credits()
    list_2.append(defer_credits_value)
    fail_credits_value = fail_credits()
    list_2.append(fail_credits_value)

    total = pass_credits_value + defer_credits_value + fail_credits_value

    if total != 120:
        print("Total incorrect")
    else:
        progression_outcome(pass_credits_value, fail_credits_value)

    repetition = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
    repetition = repetition.lower()
    loop_count += 1
if repetition == "q":
    progression_outcome_dict(list_1,list_2,list_3)
    



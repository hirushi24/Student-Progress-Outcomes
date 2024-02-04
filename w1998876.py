#Initializing the variables
pass_credits_value=0
defer_credits_value=0
fail_credits_value=0
total = 0
repetition = "y"
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
list_1=[]
list_2=[]
loop_count = 0


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
    global progress_count, trailer_count, retriever_count, exclude_count

    if pass_credits == 120:
        print("Progress")
        list_1.append("Progress")
        progress_count = progress_count + 1

    elif pass_credits == 100:
        print("Progress (module trailer)")
        list_1.append("Progress (module trailer)")
        trailer_count = trailer_count + 1

    elif 0 <= fail_credits <= 60:
        print("Do not progress - module retriever")
        list_1.append("Module retriever")
        retriever_count = retriever_count + 1

    else:
        print("Exclude")
        list_1.append("Exclude")
        exclude_count = exclude_count + 1
    return progress_count, trailer_count, retriever_count, exclude_count,list_1


#Print the progression outcomes and their corresponding credits
def progression_credits_list(list_1,list_2):
    x=0
    y=3
    for i in list_1:
        credits = ','.join(map(str,list_2[x:y]))
        print(i,"-",credits)
        y=y+3
        x=x+3

#Generates histogram
def histogram(repetition, progress_count, trailer_count, retriever_count, exclude_count):
    print("Histogram")
    print("Progress ", progress_count, ":", "*" * progress_count)
    print("Trailer  ", trailer_count, ":", "*" * trailer_count)
    print("Retriever", retriever_count, ":", "*" * retriever_count)
    print("Exclude  ", exclude_count, ":", "*" * exclude_count)


#Creating the text file
def textfile(list_1,list_2):
    f = open("readme.txt", "w") 
    f.write("Part III-:\n\n")
    z=0
    

#Printing the progression status along with the progression data inside the text file
    for t in list_1:
        f.write(str(t) + " - " + str(list_2[z]) + ",")
        f.write(str(list_2[z+1])+ ",")
        f.write(str(list_2[z+2] ))
        f.write("\n")
        z += 3
    f.close()

while repetition == "y":
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
    histogram(repetition, progress_count, trailer_count, retriever_count, exclude_count)
    print("\n\n Part II :\n")
    progression_credits_list(list_1,list_2)
    textfile(list_1,list_2)

another_set = "y"   #Variable to validate the loop

#Empty Lists to store and reuse data
progress = []
module_trailer = []
module_retriever = []
exclude = []

#Start of program to get inputs
while another_set == "y":
    pass_marks = input("Enter Your total PASS Credits: ")
    try:
        pass_marks = int(pass_marks)
    except ValueError:
        print("Integer Required\n")
        pass_marks = int(input("Enter Your total PASS Credits: "))
    if not(pass_marks in (0,20,40,60,80,100,120)):
        print("Out of Range.\n")
        pass_marks = int(input("Enter Your total PASS Credits: "))

    defer_marks = int(input("Enter Your total DEFER Credits: "))
    fail_marks = int(input("Enter Your total FAIL Credits: "))
    
    total = pass_marks + defer_marks + fail_marks
    if not total == 120:
        print("Total Incorrect.\n")
    elif pass_marks == 120:     #Condition to Check for "Progress"
        print("Progress\n")
        progress.append("Progress")     #Storing inputs into list progress = []
        progress.append(pass_marks)
        progress.append(defer_marks)
        progress.append(fail_marks)

    elif pass_marks == 100:     #Condition to Check for "Module Trailer"
        print("Progress (Module Trailer)\n")
        module_trailer.append("Progress (Module Trailer)")      #Storing inputs into list module_trailer = []
        module_trailer.append(pass_marks)
        module_trailer.append(defer_marks)
        module_trailer.append(fail_marks)

    #Conditions to check "Module Retriever"
    elif (pass_marks == 80 or pass_marks == 60) or (pass_marks == 40 and defer_marks >= 20) or (pass_marks == 20 and defer_marks >=40) or (pass_marks == 0 and defer_marks >= 60):
        print ("Do not Progress - Module Retriever\n")
        module_retriever.append("Do not Progress - Module Retriever")   #Storing inputs into list module_retriever = []
        module_retriever.append(pass_marks)
        module_retriever.append(defer_marks)
        module_retriever.append(fail_marks)

    elif fail_marks >=80:   #Condition to Check for "Exclude"
        print("Exclude\n")      
        exclude.append("Exclude")       #Storing inputs into list exclude = []
        exclude.append(pass_marks)
        exclude.append(defer_marks)
        exclude.append(fail_marks)
        
    print("Would you like to Enter another set of Data?")
    another_set = str(input("Enter 'y' for yes or 'q' to quit and view results: "))
    print("\n")
        
    if another_set == "q":
        
        from graphics import *

        def histogram():

            #Histogram Window 
            win = GraphWin("Histogram", 800, 600)
            win.setBackground("Honeydew")

            #Histogram Heading
            histogram = Text(Point(200,30),"Histogram Results")
            histogram.setStyle("bold")
            histogram.setSize(18)
            histogram.draw(win)

            #X axis Line
            line = Line(Point(100,500),Point(700,500))
            line.draw(win)

            #Total Number of inputs for Progress, Module Trailer, Module Retriever and Exclude
            pro_tot = int(len(progress)/3)
            tra_tot = int(len(module_trailer)/3)
            ret_tot = int(len(module_retriever)/3)
            ex_tot = int(len(exclude)/3)

            #Length for each Columns
            pro_len = 500 - (15*pro_tot)
            tra_len = 500 - (15*tra_tot)
            ret_len = 500 - (15*ret_tot)
            ex_len = 500 - (15*ex_tot)

            #Progress - Column
            pro_box = Rectangle(Point(150,500), Point(250,pro_len))
            pro_box.setFill("Lime")
            pro_box.draw(win)

            #Progress - Label
            pro = Text(Point(200,510), "Progress")
            pro.setFill("Grey")
            pro.setStyle("bold")
            pro.draw(win)

            #Progress - Number
            pro_num = Text(Point(200,pro_len-10),pro_tot)
            pro_num.setFill("Grey")
            pro_num.setStyle("bold") 
            pro_num.draw(win)

            #Module Trailer - Column
            tra_box = Rectangle(Point(270,500), Point(370,tra_len))
            tra_box.setFill("OliveDrab")
            tra_box.draw(win)

            #Module Trailer - Label
            tra = Text(Point(320,510), "Trailer")
            tra.setFill("Grey")
            tra.setStyle("bold")
            tra.draw(win)

            #Module Trailer - Number
            tra_num = Text(Point(320,tra_len-10),tra_tot)
            tra_num.setFill("Grey")
            tra_num.setStyle("bold")
            tra_num.draw(win)

            #Module Retriever - Column
            ret_box = Rectangle(Point(390,500), Point(490,ret_len))
            ret_box.setFill("Olive")
            ret_box.draw(win)

            #Module Retriever - Label
            ret = Text(Point(440,510), "Retriever")
            ret.setFill("Grey")
            ret.setStyle("bold")
            ret.draw(win)

            #Module Retriever - Number
            ret_num = Text(Point(440,ret_len-10),ret_tot)
            ret_num.setFill("Grey")
            ret_num.setStyle("bold")
            ret_num.draw(win)

            #Exclude - Column
            ex_box = Rectangle(Point(510,500), Point(610,ex_len))
            ex_box.setFill("MistyRose")
            ex_box.draw(win)

            #Exclude - Label
            ex = Text(Point(560,510), "Excluded")
            ex.setFill("Grey")
            ex.setStyle("bold")
            ex.draw(win)

            #Exclude - Number
            ex_num = Text(Point(560,ex_len-10),ex_tot)
            ex_num.setFill("Grey")
            ex_num.setStyle("bold")
            ex_num.draw(win)

            out_tot = pro_tot + tra_tot + ret_tot + ex_tot #Total of Outcomes

            #Outcome
            outcome = Text(Point(270,550), str(out_tot) + " outcomes in total.")
            outcome.setFill("Gray")
            outcome.setSize(16)
            outcome.setStyle("bold")
            outcome.draw(win)

            win.getMouse()
            win.close()

        histogram()
       
        print("Part 2:")

        #Printing the saved inputs from list progress = []
        for i in range(0,len(progress),4):
            print(progress[i],"-",progress[i+1], progress[i+2],progress[i+3])
            
        #Printing the saved inputs from list module_trailer = []
        for i in range(0,len(module_trailer),4):
            print(module_trailer[i],"-",module_trailer[i+1], module_trailer[i+2],module_trailer[i+3])

        #Printing the saved inputs from list module_retriever = []
        for i in range(0,len(module_retriever),4):
            print(module_retriever[i],"-",module_retriever[i+1], module_retriever[i+2],module_retriever[i+3])

        #Printing the saved inputs from list exclude = []
        for i in range(0,len(exclude),4):
            print(exclude[i],"-",exclude[i+1], exclude[i+2],exclude[i+3])

        print("\nPart 3:")
        
        with open("part3.txt", "w") as f:
            for i in range(0,len(progress),4):
                print(progress[i],"-",progress[i+1], progress[i+2],progress[i+3])

            for i in range(0,len(module_trailer),4):
                print(module_trailer[i],"-",module_trailer[i+1], module_trailer[i+2],module_trailer[i+3])

            for i in range(0,len(module_retriever),4):
                print(module_retriever[i],"-",module_retriever[i+1], module_retriever[i+2],module_retriever[i+3])

            for i in range(0,len(exclude),4):
                print(exclude[i],"-",exclude[i+1], exclude[i+2],exclude[i+3])
        
        f = open("part3.txt")

        break
    
    elif another_set != "q":
        while another_set != "y":   #Condition in case the given input is neither "q" or "y"
            print("Invalid Input")
            another_set = input("Enter 'y' for yes or 'q' to quit and view results: ")
            print("\n")

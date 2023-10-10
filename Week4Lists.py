import random

def RandomPersonPicker():
#2. Random Person Picker (one chip) Write a program that will pick a person from a list of 10 names at random.
#Your program should:
#· Allow the user to enter the names (just first names will do).
#· Pick one person from the list and display their name   
    nameList = [] # creates an empty list
    for i in range(10): # use a for loop to get 10 input and append to the list
        tmpName = input("Enter name: "+ str(i)) #need to concatenate i as a string
        nameList.append(tmpName)# append the input to the list
    choice=int(random.randint(0,9)) #generate a random number integer between 0 and 9
    print("The Random name is: "+ nameList[choice]) # print the random element

def BiggestNumber():
#3. Biggest number (2 Chips) Write a program that will find the largest number of values stored in an array.
# Your program should:
##Allow the user to enter 5 values into the array
##Return the Largest number and it's position in the array
    numList = [] # creates an empty list
    for i in range(5): # use a for loop to get 10 input and append to the list
        thisNum = int(input("Enter num:"+str(i)+" ")) #need to concatenate i as a string
        numList.append(thisNum)# append the input to the list
    largest=0 #initialise largest
    for num in numList: #loop through List      
        if num > largest:# compare each number with the largest number
            largest = num # update if current number is larger
    print("Largst number is: "+str(largest))

def letterCount():
#4. Letter Count (2 chips) Write a program that works out how many letter a's there are in an inputted string Your program should:
#· allow the user to input a string
#· allocate each character to an element in an array (you can access the characters using array notation on the string)
#· Count and output the number of times the letter a appears
#· For an extra chip modify this program to count how many time each vowel appear keeping a running total in a 5 element array
    aCount=0 #initialise
    vowelCount=0
    myStr = str(input("enter a string"))
    for char in myStr:#loop through
        if char == "a": # increment a count if it's and a
            aCount+=1
        if char in "aeiou": #this is a easy way of asking if one string is in another
            vowelCount+=1 #extention work
    print("number of a's= "+ str(aCount))
    print("number of vowels= "+ str(vowelCount))
    
def nameSearch():
#5. Name Search (2 Chips) Write a program that will find a name in a list stored in an array Your program should:
#· Allow the user to enter the names (just first names will do).
#· Allow the user to enter the name they wish to search for
#· Return if the name is in the array and it's position
    nameList = [] # creates an empty list
    for i in range(10): # use a for loop to get 10 input and append to the list
        tmpName = input("Enter name: "+ str(i)) #need to concatenate i as a string
        nameList.append(tmpName)# append the input to the list

    searchName = input("what name do you wish to search for? ")
    found=False
    for i in range(10):# we could have looped through the list
        if searchName==nameList[i]:
            found=True
            index=i
            break #I know I said I didn't like this but MEH!
    if found:
        print(searchName + " is in the list at position: "+ str(index))
    else:
        print("name not in list")

def listReverse():
#5.Reversal (2 Chips) Write a program that will reverse the values store in an array (so the first value is the last etc..) Your program should:
#Allow the user to enter 5 values (or strings)
#· Display the array in the original order
#· assign the values on reverse element order to a new array
#· Display the new array... NB you must not just display the array in reverse order
    myList = ["bob","sam","pat","sally","wendy"] #hardcoded list you should have user inputs
    print(myList)#prints list
    myList.reverse() #reverses the list 
    print(myList)

def tallyChart():
# 6) Tally Chart (2 Chips) Write a program that counts and displays how many time a specific number is entered. i.e. if the user entered: 1 3 2 5 1 2 2 3 1 4 the program would output #1s=3, #2s=3, #3s=2, #4s=1,#5s=1 total numbers entered =10
#· Allow the user to enter up to 20 numbers (between 0 and 9)
#· tally how many of each number is entered
#· display the tally as above (or an appropriate table)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5] #hardcoded for speed
    #the list tally will store the count of each number index by the list
    tally = [0 for i in range(11)] # generates a list placing 0 in each element
    for thisNum in numbers:
        tally[thisNum]+=1 #incremetns the value 
    for i in range(1,10):
        print("the number "+str(i)+" appears "+str(tally[i])+" times in the list")

def selectNames():
#7) SELECT NAMES (2 Chips) Write a program that will produce a list of names where the surname is longer than the firstname The program should:
#· allows the user to enter 10 names (firstnames and surnames) into an array.
#· Compare the length of each first name and surname
#· Display a list of all the names where the surname is longer than the firstname
#NB I'm going to do 5 names to make the testing less painful

    names = [["" for i in range(2)] for j in range(5)] #creates a 2x5 list and places empty strings in it
    for n in range(5): #loops through the rows
        names[n][0] = input("enter firstname: ")
        names[n][1] = input("enter sirname: ")

    for n in range(5): #loops through the rows again!
        if names[n][0] < names[n][1]: #if sirname is greater than firstname
            print(names[n])
    
        
def expAverage():
# 8) EXPERIMENT AVERAGE (2 Chips) Write a program that allows the user to enter data for an experiment that times how long it takes for a ball to fall a set distance.. As a good scientist you repeat the experiment and take the average of the two values for each height e.g.
# Height Time 1 Time 2 Average
# The program should:
#· allow the user to enter height and two times and add it to the array
#· Calculate the average for each height and assign it to the four "column" of the array
#· Display the whole table in a reasonable format
    table = [[0 for i in range(4)] for j in range(5)] #generates a 4x5 table
    for n in range(5): #loops through the rows
        table[n][0] = int(input("enter height: "))
        table[n][1] = int(input("enter time1: "))
        table[n][2] = int(input("enter time2: "))
        table[n][3] = (table[n][1] + table[n][2])/2 #average

    #display table (there are better ways to do this!)
    print("ht \t t1 \t t2 \t ave t")
    for n in range(5): 
        print(table[n][0], end="\t")
        print(table[n][1], end="\t")
        print(table[n][2], end="\t")
        print(table[n][3], end="\t")

expAverage()
def Extention():
    letter=input("Enter the word in english: ")
    list=[]

    for i in range(len(letter)):
        list.append(letter)
    counter=(len(letter))

    if counter == 0:
        print(" You did not enter a valid word, try again ")
    elif counter == 1:
        print(" You did not enter a valid word, try again ")
    else:
        print("The entered word has",len(list),'letters')


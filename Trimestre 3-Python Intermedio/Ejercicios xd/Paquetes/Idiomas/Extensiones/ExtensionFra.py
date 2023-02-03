def France():
    lettr=input("entrer le mot en français: ")
    prêt=[]
    
    for i in range(len(lettr)):
        prêt.append(lettr[i])
    comptable=(len(prêt))
    
    if comptable == 0:
        print("Vous n'avez pas entré de mot valide, réessayez")
    elif comptable == 1:
        print("Vous n'avez pas entré de mot valide, réessayez")
    else:
        print("le mot saisi a",len(prêt),'lettre')



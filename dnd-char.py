import pymongo
from pymongo import MongoClient

cluster = MongoClient("<Mongo DB cluster connection info>")
db = cluster["Dnd"]
collection = db["Characters"]

go = True
while go:
    option = input('''
    Add Character: (A)
    Find Character: (F)
    See All Characters: (S)
    Update Character: (U)
    Delete Character: (D)
    Exit (X)
    Enter an option: ''')

    if (option == "X" or option == "x"):
        go = False

    elif (option == "A" or option == "a"):
        # create a new character
        name = input("What is the character name?: ")
        lv = input("What is " + name +"'s level?: ")
        clas = input("What is " + name +"'s class?: ")
        sub = input("What is " + name +"'s subclass?: ")
        post = {"name":name, "level":lv, "class":clas, "subclass":sub}
        collection.insert_one(post)
        input("Chsrscter created. Press enter to continue: ")

    elif (option == "F" or option == "f"):
        # find character
        name = input("Enter the name of your character?: ")
        query = collection.find({"name" : name})
        results = []
        for result in query:
            results.append(result)
        if len(results) < 1:
            print("There are no characters with that name.")
        else:
            for result in results:
                print(result["name"] + ", Lv" + result["level"] + " " + result["subclass"] + " "+ result["class"])
        input("Press enter to continue: ")
    
    elif (option == "D" or option == "d"):
        # delete a character
        name = input("Enter the name of your character?: ")
        query = collection.find({"name" : name})
        results = []
        for result in query:
            results.append(result)
        if len(results) < 1:
            print("There are no characters with that name.")
        elif len(results) == 1:
            inp = input("Are you sure you want to delete " + result["name"] + ", Lv" + result["level"] + " " + result["subclass"] + " "+ result["class"]+"\n (Y/N): ")
            if (inp == "Y" or inp == "y"):
                collection.delete_one(result)
        else:
            print("There are multiple characters with that name.")
            i = 0
            for result in results:
                print("("+str(i)+")"+result["name"] + ", Lv" + result["level"] + " " + result["subclass"] + " "+ result["class"])
                i += 1
            inp = int(input("Which Character would you like to delete?: "))
            result = results[inp]
            inp = input("Are you sure you want to delete " + result["name"] + ", Lv" + result["level"] + " " + result["subclass"] + " "+ result["class"]+"\n (Y/N): ")
            if (inp == "Y" or inp == "y"):
                collection.delete_one(result)
        input("Press enter to continue: ")

    elif (option == "U" or option == "u"):
        # Update a character
        name = input("Enter the name of your character?: ")
        query = collection.find({"name" : name})
        results = []
        for result in query:
            results.append(result)
        if len(results) < 1:
            print("There are no characters with that name.")
        elif len(results) == 1:
            new = results[0].copy()
            inp = input("Which category would you like to change?\n (name)\n (level)\n (class)\n (subclass)\n?: ")
            if (inp == "name") or (inp == "level") or (inp == "class") or (inp == "subclass"):
                new[inp] = input("Enter new " + inp + ": ")

            sure = input("Are you sure you want to change " 
            + result["name"] + ", Lv" + result["level"] + " " + result["subclass"] + " "+ result["class"]
            + " to " + new["name"] + ", Lv" + new["level"] + " " + new["subclass"] + " "+ new["class"]
            +"\n (Y/N): ")
            if (sure == "Y" or sure == "y"):
                collection.update_one(results[0], {"$set": new})
                print("Updated.\n")
            input("Press enter to continue: ")




        else:
            print("There are multiple characters with that name.")
            i = 0
            for result in results:
                print("("+str(i)+")"+result["name"] + ", Lv" + result["level"] + " " + result["subclass"] + " "+ result["class"])
                i += 1
            inp = int(input("Which Character would you like to edit?: "))
            result = results[inp]
            new = result.copy()
            cat = input("Which category would you like to change?\n (name)\n (level)\n (class)\n (subclass)\n?: ")
            if (cat == "name") or (cat == "level") or (cat == "class") or (cat == "subclass"):
                new[cat] = input("Enter new " + cat + ": ")

            sure = input("Are you sure you want to change " 
            + result["name"] + ", Lv" + result["level"] + " " + result["subclass"] + " "+ result["class"]
            + " to " + new["name"] + ", Lv" + new["level"] + " " + new["subclass"] + " "+ new["class"]
            +"\n (Y/N): ")
            if (sure == "Y" or sure == "y"):
                collection.update_one(results[inp], {"$set": new})
                print("Updated.\n")
            input("Press enter to continue: ")


    elif (option == "S" or option == "s"):
        # see all characters
        results = collection.find({})
        for result in results:
                print(result["name"] + ", Lv" + result["level"] + " " + result["subclass"] + " "+ result["class"])
        input("Press enter to continue: ")

    else:
        print("Please input a valid option.")

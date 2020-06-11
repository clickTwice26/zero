
print("---------------------------------------------------------------------------")
print(":              Cyber Rangers - We wanna be established                    :")
print(":                   script code: 000000000000001                          :")
print(":                    date created: 14/05/2020                             :")
print(":                    code writer: 5hagat0                                 :")
print(":        Script Name: Bangladesh's Division's Details                     :")
print(":                Script Type:Open Source                                  :")
print(":-------------------------------------------------------------------------:")
terminate = False
x = {"barisal": {"District": 6, "Upazilla": 39, "Council": 333}, "chittagong": {"District": 11, "Upazilla": 97, "Council": 336}, "dhaka": {"District": 13, "Upazilla": 93, "Council": 1833}, "khulna": {"District": 10, "Upazilla": 59, "Council": 270}, "mymensingh": {"District": 4, "Upazilla": 34, "Council": 350}, "rajshahi": {"District": 8, "Upazilla": 70, "Council": 558}, "rangpur": {"District": 8, "Upazilla": 58, "Council": 536}, "sylhet": {"District": 4, "Upazilla": 38, "Council": 334}}
                                                                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                                                                                           

while not terminate:
    #variables
    print("Please Select a action:")
    print("[+]List Of Division = 1")
    print("[+]Particular Division Details = Enter the name of Division")
    print("[+]All Division's District = 3")
    print("[+]Exit = 4")
    y = input("Please enter your operation: ")
    z = y.lower()
    f = y.capitalize()
    g = x.keys()
    while True:
        if y == "4":
            terminate = True
            break
        if z not in ["list", "exit", "quit", "list", "sylhet", "rangpur", "mymensingh", "khulna", "dhaka", "chittagong", "barisal", "1", "2", "3", "4"]:
             print("Unknown Operation")
             break
                     
        if y in ["list", "List", "1"]:
              print("|------------|")
              print("| Barisal    |")
              print("|------------|")
              print("| Chittagong |")
              print("|------------|")
              print("| Dhaka      |")
              print("|------------|")
              print("| Khulna     |")
              print("|------------|")
              print("| Mymensingh |")
              print("|------------|")
              print("| Rajshahi   |")
              print("|------------|")
              print("| Rangpur    |")
              print("|------------|")
              print("| Sylhet     |")
              print("|------------|")

              break
        if z in ["sylhet", "rangpur", "mymensingh", "khulna", "dhaka", "chittagong", "barisal"]:
            print("---------------------------------------")
            print("           The Info of                 ")
            print("            ", f) 
            print("     District:", x[z]["District"])
            print("     Upazilla:", x[z]["Upazilla"])
            print("     Council:", x[z]["Council"])
            print("---------------------------------------")
            break
        if y == "3":
            print("District = 1")
            print("Upazilla = 2")
            print("Council = 3")
            u = input("District/Upazilla/Council: ")
            if u == "1":
                jj = "District"
            elif u == "2":
                jj = "Upazilla"
            elif u == "3":
                jj = "Council"
            print(" ")
            print(" ")
            for i in g:
                print("------------------------------------")
                print("There are", x[i][jj], jj.capitalize(), "in", i.capitalize(), "Division")
                print("------------------------------------")
        print(" ")
        print(" ")
        break

                      
                    

        

print("---------------------------------------------------------------------------")
print(":                        Cyber Rangers                                    :")
print(":                   script code: 000000000000002                          :")
print(":                    date created: 13/06/2020                             :")
print(":                    code writer: 5hagat0                                 :")
print(":        Script Name: Bangladesh's Division's Details                     :")
print(":                Script Type:Open Source                                  :")
print(":-------------------------------------------------------------------------:")
import requests
import os
terminate = False
while not terminate:
    url = input("[+]Enter The Url: ")
    
    if not url.startswith("https"):
        print("[+]Add 'http://' or 'https://' before this Url")
        print("[+]Invalid Url")
        print("[+]Closing The Program")
        continue
    response = requests.get(url)
    

    if url.startswith("https") and response.ok == True:
        print("The Source Code")
        print(response.text)
        z = input("Do you want to save this file?(Y/n/exit): ")
        if z in ["yes", "y", "Y", "Yes"]:
            ff = True
        else:
            ff = False
        while ff:
            print("")
            print("---------------------------------------")
            print("[+]Please select the file types: ")
            print("[1]Html")
            print("[2]Text")
            print("[3]Php")
            print("[4]All in One")
            print("[5]Change Url")
            print("[6]Exit")
            print("---------------------------------------")
        
            ftype = input("[+]Please Select: ")
            if ftype == "1":
            
                print("[+]You have decided to save in Html")
                fp = open("Source_Code.html", "w")
                fp.write(response.text)
                fp.close()
                print("[+]Done")
                continue
            if ftype =="2":
                print("Y[+]ou have decided to save in text")
                fp = open("/shagato/Source_Code.txt", "w")
                fp.write(response.text)
                fp.close()
                print("[+]Done")
                continue
            if ftype == "3":
                print("You have decided to save in Php")
                fp = open("Source_Code.php", "w")
                fp.write(response.text)
                fp.close()
                print("[+]Done")
                continue
            if ftype == "4":
                print("[+]You have decided to save in Html")
                fp = open("Source_Code.html", "w")
                fp.write(response.text)
                fp.close()
            
                print("[+]You have decided to save in text")
                fp = open("Source_Code.txt", "w")
                fp.write(response.text)
                fp.close()
            
                print("[+]You have decided to save in Php")
                fp = open("Source_Code.php", "w")
                fp.write(response.text)
                fp.close()
                print("[+]Saving")
                print("[+]Saving.")
                print("[+]Saving..")
                print("[+]Saving...")
                print("[+]Saving....")
                print("[+]Saved")
                continue
            if ftype == "5":
                url = input("[+]Enter The Url: ")
                continue
            if ftype == "6":
                terminate = True
                continue
            else:
                print("[+]Unvalid Operation")
                break
            while not ff:
                print("[+]Closing This program")
        if z in ["exit", "Exit"]:
            print("Exiting.")
            print("Exiting..")
            print("Exiting...")
            print("Exiting....")
            print("Exiting.....")
            print("Exiting......")
            print("Exiting.......")
            print("Exiting........")
            print("Exiting.........")
            
            terminate = True


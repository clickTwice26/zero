print("---------------------------------------------------------------------------")
print(":                        Cyber Rangers                                    :")
print(":                   script code: 000000000000002                          :")
print(":                    date created: 13/06/2020                             :")
print(":                    code writer: 5hagat0                                 :")
print(":        Script Name: Website's Source Code Retriver                      :")
print(":                Script Type:Open Source                                  :")
print(":-------------------------------------------------------------------------:")

import requests
import os
import webbrowser as web

terminate = False
while not terminate:
    url = input("[+]Enter The Url: ")
    
    if not url.startswith("http"):
        print("[+]Add 'http://' or 'https://' before this Url")
        print("[+]Invalid Url or Command")
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
            print("[7]Our Website")
            print("---------------------------------------")
        
            ftype = input("[+]Please Select: ")
            if ftype == "1":
            
                print("[+]You have decided to save in Html")
                fp = open("Source_Code.html", "w", encoding=response.encoding)
                fp.write(response.text)
                fp.close()
                print("[+]Done")
                continue
            if ftype =="2":
                print("Y[+]ou have decided to save in text")
                fp = open("/shagato/Source_Code.txt", "w", encoding=response.encoding)
                fp.write(response.text)
                fp.close()
                print("[+]Done")
                continue
            if ftype == "3":
                print("You have decided to save in Php")
                fp = open("Source_Code.php", "w", encoding=response.encoding)
                fp.write(response.text)
                fp.close()
                print("[+]Done")
                continue
            if ftype == "4":
                print("[+]You have decided to save in Html")
                fp = open("Source_Code.html", "w", encoding=response.encoding)
                fp.write(response.text)
                fp.close()
            
                print("[+]You have decided to save in text")
                fp = open("Source_Code.txt", "w", encoding=response.encoding)
                fp.write(response.text)
                fp.close()
            
                print("[+]You have decided to save in Php")
                fp = open("Source_Code.php", "w", encoding=response.encoding)
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
            if ftype in ["exit", "Exit", "6"]:
                print("Exiting.")
                print("Exiting..")
                print("Exiting...")
                print("Exiting....")
                print("Exiting.....")
                print("Exiting......")
                print("Exiting.......")
                print("Exiting........")
                print("Exiting.........")
                print(
                '''
_______________██████████
_____________█████████████
____________██████████████
__________█_█████████████
_______███_█████████████
____██_█_███████████__██
__██_██__█████___________██
_███_█████████__________██
██_██_█████████
██_█_██████████
██_██_████████
█_████__██████
█_████___█████
█_████__█████
█_█████___████
█_█████___████
██_█████__████
_██_██████_████
███ __██████_███
█████ __█████__██
█_█_████__█████_██
██__████__█_████_██
████_█__██████████
_█████__██████████
__███__████████████
█__██__█████████████
█____████████████████
█_______███████████████
█__________██████████████
█____________██████████████
█______________█████████████
█_______________████████████
█_______________███████████
. ___██████████████████
█_██████████████████
█__█████████████████
█__███████______██████
_██__█_██________███████
_██_██____________███████
_██_█_____________████████
__██________________███████
██__________________███████
█____________________██████
█_____________________█████
█____________________███████
█____________________███████
█____________________█████__█████
█___________________█████████████
''')

                print("[+]Closing This program")
                terminate = True
                break
            if ftype == "7":
                web.open("https://scblog.netlify.app")
                print("Opening")
            else:
                print("[+]Unvalid Operation")
                break
            
                



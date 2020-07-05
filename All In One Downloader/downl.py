
from __future__ import unicode_literals
import youtube_dl
import urllib
import shutil
import requests
import sys
import os
try:


    
    yt_downloader = sys.argv[1]
    img_downloader = sys.argv[1]
    url = sys.argv[2]
    source_code = sys.argv[1]
    
    if yt_downloader == "-yt":
    
    
        if not url.startswith("https://"):
            
            url = "https://"+ url
            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
    elif img_downloader == "-img":
        name = input("Please Enter The File name: ")
        print(":---------------------:")
        print(":[+]Select File Type  :")
        print(":---------------------:")
        print(":    [1]PNG           :")
        print(":    [2]JPG           :")
        print(":    [3]Gif           :")
        print(":---------------------:")
        type1 = input("Please Enter:")
        if type1 == "1":
            ext = ".png"
        elif type1 == "2":
            ext = ".jpg"
        elif type1 == ".gif":
            ext = ".gif"
        
            
        
        
        
        response = requests.get(url)
        with open(name + ext, "wb") as img:
            img.write(response.content)
        print("Your Image has Saved")
    elif source_code == "-sc":
        response = requests.get(url)
        with open("Source_Code.txt", "w", encoding=response.encoding) as ff:
            ff.write(response.text)
        print("File Saved")
    sys.exit()
        
except IndexError:
    print("---------------------------------------------------------------------------")
    print(":                        Cyber Rangers                                    :")
    print(":                   script code: 000000000000004                          :")
    print(":                    date created: 22/06/2020                             :")
    print(":                    last updated: 05/07/2020                             :")
    print(":                    code writer: 5hagat0                                 :")
    print(":        Script Name: All In One Downloader                               :")
    print(":                Script Type:Open Source                                  :")
    print(":           Youtube Video | Image | Website Source Code                   :")
    print(":-------------------------------------------------------------------------:")
    print("")
    print(":--------------------------------------:")
    print(":    [+]Please Select An Option:       :")
    print(":--------------------------------------:")
    print(":     [1]Youtube Video Downloader      :")
    print(":     [2]Image Downloader              :")
    print(":     [3]Source Code Downloader        :")
    print(":     [4]Requirements                  :")   
    print(":If you are using this tool first time :")
    print(":please satisfy REQUIREMENTS this tool :")
    print(":--------------------------------------:")
    x = input("[+]Please Select a Option:")
    

    
    if x == "1":
        url = input("Please Enter the Url:")
    
    
        if not url.startswith("https://"):
            
            url = "https://"+ url
            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        elif url:
            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
    elif x == "2":
        
        import requests

        while True:
            url = input("Paste image URL: ")
            pic_name = input("Enter Image name: ")
            print(":----------------------------:")
            print(":   [+]Select File Type      :")
            print(":----------------------------:")
            print(":        [1]PNG              :")
            print(":        [2]JPG              :")
            print(":        [3]Gif              :")
            print(":        [4]Change Url       :")
            print(":----------------------------:")
            terminate = False

            while not terminate:
                file_format = input("Please Enter Your Option: ")

                if file_format in ["png", "Png", "1", "PNG"]:
                    x = ".png"
                    form = "PNG"
                elif file_format in ["2", "JPG", "Jpg", "jpg"]:
                    x = ".jpg"
                    form = "JPG"
                elif file_format in ["3", "GIF", "gif", "Gif"]:
                    x = ".gif"
                    form = "GIF"
                elif file_format == "4":
                    url = input("Paste image URL: ")
                    pic_name = input("Enter Image name: ")
                    print("Select File Type")
                    print("[1]PNG")
                    print("[2]JPG")
                    print("[3]Gif")
                    print("[4]Change Url")
                    continue



                elif file_format not in ["3", "GIF", "gif", "Gif", "png", "Png", "1", "PNG", "2", "JPG", "Jpg", "jpg"]:
                    print("Unknown Operation")
                    continue

                response = requests.get(url)
                with open(pic_name + x, "wb") as f:
                    f.write(response.content)
                    print("Image saved")
                    print("-------------------------------------")
                    print("Image Details:")
                    print(f"Name:{pic_name}|Format:{form}")
                    print("-------------------------------------")
    elif x == "4":
        os.system("pip install -r requirements.txt")
        os.system("python downl.py")
    elif x == "3":
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
                print("The Source Code Loaded")
                
                z = input("Do you want to save this file?(Y/n/exit): ")
            if z in ["yes", "y", "Y", "Yes"]:
                ff = True
            else:
                ff = False
            while ff:
                print("")
                print(":--------------------------------------:")
                print(":[+]Please select the file types:      :")
                print(":--------------------------------------:")
                print(":        [1]Html                       :")
                print(":        [2]Text                       :")
                print(":        [3]Php                        :")
                print(":        [4]All in One                 :")
                print(":        [5]Change Url                 :")
                print(":        [6]Exit                       :")
                print(":        [7]Our Website                :")
                print("---------------------------------------:")
        
                ftype = input("[+]Please Select: ")
                if ftype == "1":
            
                    print("[+]You have decided to save in Html")
                    fp = open("Source_Code.html", "w", encoding=response.encoding)
                    fp.write(response.text)
                    fp.close()
                    print("[+]Done")
                    continue
                if ftype =="2":
                    print("[+]You have decided to save in text")
                    fp = open("Source_Code.txt", "w", encoding=response.encoding)
                    
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
____██_█_█████████████
__██_██__██████
_███_███████████
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
            
        

    
    


    

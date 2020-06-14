print("---------------------------------------------------------------------------")
print(":                        Cyber Rangers                                    :")
print(":                   script code: 000000000000003                          :")
print(":                    date created: 14/06/2020                             :")
print(":                    code writer: 5hagat0                                 :")
print(":        Script Name: Image File Downloader                               :")
print(":                Script Type:Open Source                                  :")
print(":-------------------------------------------------------------------------:")

import requests
while True:
    url = input("Paste image URL: ")
    pic_name = input("Enter Image name: ")
    print("Select File Type")
    print("[1]PNG")
    print("[2]JPG")
    print("[3]Gif")




    file_format = input("Please Enter Your Image File Type: ")
    response = requests.get(url)
    if file_format == "1":
        x = ".png"
        form = "PNG"
    elif file_format == "2":
        x = ".jpg"
        form = "JPG"
    elif file_format == "3":
        x = ".gif"
        form = "GIF"



    with open(pic_name + x, "wb") as f:
        f.write(response.content)
        print("Image saved")
        print("Image Details:")
        print(f"Name: {pic_name} Format: {form}")


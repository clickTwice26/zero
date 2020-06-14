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
    print("[4]Change Url")
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




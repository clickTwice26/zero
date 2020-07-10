if __name__ == "__main__":

    from pathlib import Path
    import os
    import sys
    print(" [+]Select An Option:")
    print(" [1] Blog ")
    print(" [2] My Quotes ")
    print(" [3] Publish")
    print(" [4] How To use")
    print(" [5] Channel Video")
    option = input("[+]Please Enter Your Option: ")
    try:
        if option == "1":

            title = input("[+]Title: ")
            description = input("[+]Description: ")
            file_name = input("[+]File Name: ")
            position = ("[+]Position:")
            date = input("[+]Date: ")
            month = input("[+]Month: ")
            year = input("[+]Year: ")
            blog_number = input("[+]Blog Number: ")
            main_file_name = file_name + ".html"
            fp = open("blog.txt", "r", encoding="utf-8").read()

            s = fp.replace("\n", "<br>")
            print("[!]Blog.txt Retrieved Correctly[!]")
            print("| Your Blog is Here|")
            print("-------------------------------------------")
            print(fp)
            print("-------------------------------------------")
    
            blog2 = f"""
      <div id="content">
      <h1><a href="{file_name}" id="intro">[{blog_number}]<b>{title}</b></a></h1>
<p align="center">::::Posted on {date}|{month}|{year}::::::</p>

    <p style="font-family: sans-serif" align="center"><font size ="2">{description}
<a href="{file_name}"><font size="2">see more ..</font></a>...</font></p>

    </div>
"""
    
    
            ext = """
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

.topnav {
  overflow: hidden;
  background-color: #333;
}

.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

.topnav a.active {
  background-color: #4CAF50;
  color: white;
}
"""


            main_file = f"""


<html>
<head>
<title>{title}</title>
     <meta charset="utf-8">
    <meta property="og:image" content="https://i.imgur.com/OVrpbsb.png">
    <meta property="og:description" content="{description}">
<meta http-equiv="content-type" content="text/html; charset="UTF-8" />
    <link rel="shortcut icon" type="image/png" href="Shagato_p.png">
<link rel="stylesheet" href="css/1.css" type="text/css" media="screen,projection" />
</head>
<body>
<div id="container">
  <div id="header">
    <h1><a href="blog2.html">Shagato's <strong>Diary</strong></a></h1>
    <h2>The hardest work is to make that work simple</h2>


<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
{ext}

</style>
</head>
<body>

<div class="topnav">
 <a href="index.html">Home</a>
  <a class="active" href="blog2.html">Blogs</a>
  <a href="Quote/quotepage1.html">My Quotes</a>
  <a href="aboutme.html">About Me</a>
    <a href="channel.html">Youtube Channel</a>
    <a href="courses.html">Courses</a>
    <a href="download.html">Downloads</a>
    </div>
</div>

  <div id="content">
      <h1><a href="file_name" id="intro"><b>{title}</b></a></h1><br><br>
    <p align="center">{date} | {month.capitalize()} | {year}</p>
    
      <p style="font-family: sans-serif"><font size="3" align="{position}">{s}</font><br><br></p>
      </div>

  <div id="footer">
    <p> Author: Shagato Chy<br />
&copy; All your copyright information <a href="copy.html"><button>here</button></a></p>
  </div>
    </body>
    </div>
    </div>
    </body>
    
      </html>
"""
            print("[+]Do you Save this Blog?")
            print("       | Yes | No |")
            conf = input("[+]Please Choose Your Option: ")

            if conf in ["yes", "Yes"]:
                with open(file_name, "w", encoding="utf8") as fd:
                    fd.write(main_file)
            if conf in ["No", "no"]:
                print("Ok")
                print("[!]Resetted[!]")
                sys.exit()

            print("[+]Copy that for Blog2")
            print(blog2)
            os.system("I:\Github\scblog\blog2.html")
            print("[+]Do You Want To Publish?")
            print("----------------------------")

            publish_conf = input("| Yes | No | : ")
            if publish_conf in ["Yes", "yes"]:
                print("[+]Publishing")
                os.system("sh submit.sh")
                print("[+]Published SuccessFully")
            else:
                print("Closing Program")
                sys.exit
        if option == "3":
            print("[+]Publishing Your Work")
            os.system("sh submit.sh")
            print("[+]Published SuccessFully")
        elif option == "2":


            dataFolder = Path(r'Quote\Quote.txt')
            quote_no = input("[+]Quote Number: ")

            fp_Q = open(dataFolder, "r", encoding="utf-8").read()
            s = fp_Q.replace("\n", "<br>")
            my_quotes = f"""
                          <div id="content">
                <h1><a href="#intro" id="intro">[{quote_no}]</a></h1>
                  <font size="3">
            <p align="center">{s}</p>

            </font>
            </div>"""
            print(":------------------------------------------------------------------------------:")
            print(my_quotes)
            print(":------------------------------------------------------------------------------:")
             
            
            
            os.system("notepad I:\Github\scblog\Quote\QuotePage1.html")

            publish_c = input("Do you want to publish now?(Yes/No): ")

            if publish_c in ["yes", "Yes"]:
                os.system("sh submit.sh")
                print("[+]submited successfully")
        if option == "4":
            try:
                with open("about.txt", "r", encoding="utf8") as about:
                    ss = about.read()
                    print(ss)
            except FileNotFoundError:
                os.system("mkdir blog.txt")
                print("There are a Blog.txt.You Have to fill your Blog there at first")
        if option == "5":
            video_title = input("Video Titile: ")
            video_link = input(" [+] Video Link: ")
            z = 0
            D = "{"
            E = "}"
            url = video_link[32:]
            channel_str = f"""

<div id="content">
    <h1><a href="{video_link}" id="intro">{video_title}</a></h1>
      <div style="overflow:hidden;position: relative;">
      <iframe frameborder="0" scrolling="no" marginheight="0" marginwidth="0"width="333" height="200" type="text/html" src="https://www.youtube.com/embed/{url}?autoplay=1&fs=1&iv_load_policy=3&showinfo=0&rel=0&cc_load_policy=0&start=0&end=0&vq=large">
      </iframe><div style="position: absolute;bottom: 10px;left: 0;right: 0;margin-left: auto;margin-right: auto;color: #000;text-align: center;"><small style="line-height: 1.8;font-size: 0px;background: #fff;"> <a href="https://logen.com.au/">logen</a> </small></div><style>.newst{D}position:relative;text-align:right;height:420px;width:520px;{E} #gmap_canvas img{D}max-width:none!important;background:none!important{E}</style></div><br /></div>
"""
            print("-------------------------------------------------------------")

            print(channel_str)


            print("-------------------------------------------------------------")
            os.system("notepad I:\Github\scblog\channel.html")
            print("Saved SuccessFully")
            os.system("sh submit.sh")
            print("Published SuccessFully")
            
            
    except:
        print("Please input Valid Operation")




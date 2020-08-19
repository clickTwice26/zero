x = int(input("Atomic Number: "))
dif = 10



if 2 < x < 10: #for porjay 2
    porjay = "2"
    if 2 < x < 5:

        position = 10 - x #x = atomic number
        dif_x = dif + position
        group = 18 - dif_x

    if 4 < x < 11:
        dif_x = 10 - x
        group = 18 - dif_x
if 10 < x < 19: #for porjay 3
    porjay = "3"
    if 10 < x < 13:

        position = 18 - x #x = atomic number
        dif_x = dif + position
        group = 18 - dif_x
    if 12 < x < 19:
        dif_x = 18 - x
        group = 18 - dif_x
if 18 < x < 37:
    porjay = "4"
    dif_x = 36 - x
    group = 18 - dif_x
if 36 < x < 55:
    porjay = "5"

    dif_x = 54 - x
    group = 18 - dif_x

#pro 6
if 56 < x < 72:
    porjay = "6"
    group = "2"

    print("Lanthanide Series")
if 88 < x < 104:
    porjay = "7"
    group = "2"

    print("Actinoid Series")

if 71 < x < 88:
    porjay = "6"

    dif_x = 86 - x
    group = 18 - dif_x
if 103 < x < 119:
    porjay = "7"

    dif_x = 118 - x
    group = 18 - dif_x
if x == 1:
    group = "1"
    porjay = "1"
if x == 2:
    group = "18"
    porjay = "1"
if x == 55:
    group = "1"
    porjay = "6"
if x == 56:
    group = "2"
    porjay = "6"
if x == 87:
    group = "1"
    porjay = "7"
if x == 88:
    group = "2"
    porjay = "7"



print(f"""
he Atomic Number:|  {x}   |
The Group number:|  {group}   |
The Period number:|   {porjay}   |


""")

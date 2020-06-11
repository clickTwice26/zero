class User:
    name = ""
    email = ""
    password = ""

    def login(self):
        email = input("Please enter Email: ")
        password = input("Enter Passowrd: ")

        if email == self.email and password == self.password:

            print("Login = Satisfied")

            login = True
            print("Your Profile Details")
            print(self.name, "\n", self.email)

        else:
            print("Login Failed")
            login = False


    def logout(self):

        login = False
        print("Logged Out")

































user1 = User()
user1.name = "Shagato"
user1.email = "abc@gmail.com"
user1.password = "12345"
user1.login()



from abc import ABC
from .constants import AccountStatus





# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes ae private and accessed through their respective
# public getter methods and modified only through their public methods function.


class Account:
    def __init__(self, id, password, status=AccountStatus.ACTIVE):
        self.__id = id
        self.__password = password
        self.__status = status

    def reset_password(self):
        # check if the current password is correct
        # then get a new password, put it in self.__password
        # HOW THE FUCK WILL THIS BE BOOLEAN ??
        # passwords should be min. 6 characters.

        check_password = input(__prompt="Enter your current password:")
        if check_password == self.__password:
            print("Password Correct! Type your new password:")
            new_password = input()
            print("Type your new password one more time:")
            new_password2 = input()
            if new_password == new_password2:
                self.__password = new_password
                return "Password Changed!"
            else:
                print("The passwords don't match.")
                i = 1
                for i in range(3):
                    print("Type your new password one more time:")
                    new_password2 = input()
                    if new_password == new_password2:
                        self.__password = new_password
                        return "Password Changed!"
                    else:
                        print("The passwords don't match.")
                        i -= 1
                return "Failed to change the password."

        else: #buraya da 3 deneme hakkı falan koyulabilir.
            print("Wrong Password.")
            return "Failed to change the password."


# from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, address, email, phone, account):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__account = account


class Customer(Person):
    def make_booking(self, booking):
        None

    def get_bookings(self):
        None


class Admin(Person):
    def add_movie(self, movie):
       # movie.title: str = input("Movie Title: ")
       # movie.description: str = input("Description: ")
       # movie.duration_in_mins: int = int(input("Duration (in minutes): "))
       # movie.language: str = input("Language: ")
       # movie.release_date: int = int(input("Release Date: ")) #this might not be a date idk
       # movie.country: str = input("Country: ")
       # movie.genre: str = input("Genre: ")
       # movie.movie_added_by: str = input("Added By: ")
        None

    def add_show(self, show):
        if add_show_button == True
            #title --> boşluk doldur, duration --> boşluğu doldur vsvs




    def block_user(self, customer):
        if block_user_button == True
            #kullanıcı adı girişi
            customer.status = AccountStatus.BLOCKED #?????????????????????????????
            return "customer is blocked."


class FrontDeskOfficer(Person):
    def create_booking(self, booking):
        None


class Guest:
    def register_account(self):
        None



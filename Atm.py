class Atm:
    def__init__(self,cardnumber,pin):   
       self.cardnumber = cardnumber
       self.pin = print

    def check_balance(self):
        print("your balance is 50000")

    def withdrawl(self,amount):
        new_amount = 50000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+str(new_ammount))


def main():
    Card_number =input("insert your card number:- ")
    pin_number  =input("enter your pin number:- ")

    new_user = Atm(Card_number ,Pin_number)

    print("choose your activity ")
    print("1.balance Enquriy   2.withdraw1")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.check_blance()
    else (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withhdraw1(ammount)
    else:
        print("entter a valid number")


if __name__=="__main__":
    main()
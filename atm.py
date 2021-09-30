import random
class Atm:
    def __init__(self, CardNumber, CardPin, Cash, Amount, WoD, Cb):
        self.CardNumber = CardNumber
        self.CardPin = CardPin
        self.Cash = Cash
        self.Amount = Amount
        self.WoD = WoD
        self.Cb = Cb
    def Withdrawl(self):
        Cash -= Amount
        print("You have withdrawed:", Amount)
    def Deposit(self):
        Cash += Amount
        print("You have deposited:", Amount)
    def Balance(self):
        if Cash < 0:
            print("You have a Debt! Pay up!")
        else:
            print("Balance is:", Cash)
    def main():
        CardNumber = input("Insert your card number:")
        CardPin = input("Insert your card pin:")
        WoD = input("Do you want to deposit or withdraw?")
        Amount = input("How much money do you want to withdraw or deposit?")
        Cb = input("Do you want to check balance?")
        Cash = 0
        if WoD == "withdraw" & Cash != 0:
            Withdrawl()
            Balance()
        elif WoD == "deposit" :
            Deposit()
            Balance()
        if Cb == "yes":
            Balance()
        if Cb == "no":
            print("Okay then! maybe next time!")
    main()
Mustang = Atm(5, 4, 3, 2, 1)


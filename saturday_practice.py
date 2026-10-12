class BankAccount:
   
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance
        self.transactions=[]
        self.status=[]
        self.balance=[]
    
    def deposit(self,amount):
        self.__balance+=amount
        print(f"Deposited:{amount}")
        self.transactions.append(amount)
        self.status.append("Deposit")
        self.balance.append(self.__balance)


    def withdraw(self,amount):
        if amount>self.__balance:
            raise InsufficientFundsError("Balance is insufficient !")
        self.__balance-=amount
        print(f"Withdrawn:{amount}")
        self.transactions.append(amount)
        self.status.append("withdrawn")
        self.balance.append(self.__balance)
    def transaction_history(self):
        print("transaction_history:")
        print("-"*25)
        print("amount".ljust(8),"status".ljust(8),"Total_balance")
        for i in range(len(self.transactions)):
            
            print(str(self.transactions[i]).ljust(6)," ",self.status[i].ljust(5)," ",str(self.balance[i]))
            print("-"*25)

    def get_balance(self):
        return self.__balance
        
class InsufficientFundsError(Exception):
    pass
class SavingsAccount(BankAccount):
    def __init__(self,account_number,balance,intrestrate,years):
        super().__init__(account_number,balance)
        self.intrestrate=intrestrate
        self.years=years

    def intrest_amount(self):
        balance=self.get_balance()
        print("BALANCE BEFORE INTREST:",self.get_balance())
        intrest=(balance*self.intrestrate*self.years)/100
        self.deposit(intrest)
        return intrest


myAcc=BankAccount(101,0)
myAcc.deposit(5000)
myAcc.withdraw(1000)
print("balance:",myAcc.get_balance())
remaining_balance=myAcc.get_balance()
myTotalIntrest=SavingsAccount(102,remaining_balance,5,2)
print(f"intrest generated:{myTotalIntrest.intrest_amount()}")
print(f" Total Balance after intrest:",myTotalIntrest.get_balance())
myAcc.transaction_history()










    
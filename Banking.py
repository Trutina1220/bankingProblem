class Customer:
    def __init__(self,firstName:str,lastName:str):
        self.firstName = firstName
        self.lastName = lastName
        self.account = 0

    def getfirstname(self):
        return self.firstName

    def get_last_name(self):
        return self.lastName

    def get_account(self):
        return self.account.get_balance()

    def set_account(self,amount:float):
        self.account = Account(amount)


class Bank:
    def __init__(self,bankName:str,numberOfCustomers:int=0):
        self.customers = []
        self.numberofCustomers = numberOfCustomers
        self.bankName = bankName

    def addCustomer(self,firstName:str,lastName:str):
        self.customers.append(Customer(firstName,lastName))

    def get_num_of_customers(self):
        return self.customers.__len__()

    def get_customers(self,index:int):
        return self.customers[index].getfirstname()+" "+self.customers[index].get_last_name()



class Account:
    def __init__(self,balance:float):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self,amount:float):
        if amount<self.balance:
            print("The amount exceeded your balance")
            return self.balance
        else:
            self.balance -= amount

    def withdraw(self,amount:float):
        if amount<self.balance:
            print("The amount exceeded your balance")
            return self.balance
        else:
            self.balance -= amount

bank1 = Bank("BCA")
bank1.addCustomer("Eric","Edgari")
bank1.addCustomer("Jack","lee")
print(bank1.get_customers(1))
print(bank1.get_num_of_customers())
customer1 = Customer("Lee","John")
customer1.set_account(145000)
print(customer1.get_account())


'''
Created on May 3, 2016

@author: Gianni
'''
from random import randint
class Customer:
    'A class that represents a customer'
    
    def __init__(self, first, last, ssnumber='000-00-000'):
        'Initiates Customer data'
        
        self.firstName = first
        self.lastName = last
        self.SSN = ssnumber
        
    def __str__(self):
        'Overrides to string and returns customer first name, last name, and ssn'
        
        return str(self.firstName + ' ' + self.lastName + ' (ssn: ' + self.SSN + ')')

class BankAccount:
    'A class that defines a base bank account class'
    
    def __init__ (self, cust):
        'Initiates Bank account'
        
        self.customer = cust
        self.acctNumber = BankAccount.generateAcctNumber(self)
        self.balance = 0
    
    def deposit(self, amount):
        'Deposits an amount into the customer\'s balance'
        
        self.balance += amount
        
    def withdraw(self, amount):
        'Withdraws an amount from the customer\'s balance'
        
        if (amount < self.balance):
            self.balance -= amount
        else:
            print(self.customer.__str__() + ' , insufficient funds to withdraw  ${:,.2f}'.format(self.balance))
        
    def applyAnnualInterest(self):
        'Applies interest'
    
    def generateAcctNumber(self):
        'Generates a random 10 digit number'
        
        stringList = []
        
        for i in range(10):
            stringList.append(str(randint(0,9)))
            
        return (''.join(stringList))
    
    def __str__(self):
        'Overrides to string and returns a pretty overview of the bank account'
        return str(self.customer.__str__() + ' , account number ' + self.acctNumber + ', balance ${:,.2f}'.format(self.balance))
    
class CheckingAccount(BankAccount):
    'A class that defines the checking account sub class'
    
    def applyAnnualInterest(self):
        'Overrides apply interest and applies a 2% interest for any amount in excess of $10,000'
        if (self.balance > 10000):
            self.balance += ((self.balance - 10000) * 0.02)
    
class SavingAccount(BankAccount):
    'A class that defines the saving account sub class'
    
    def applyAnnualInterest(self):
        'Overrides apply interest and applies a flat 5% interest'
        self.balance += (self.balance * 0.05)

def main():
    'Main method'

    alin = Customer('Alin', 'Smith', '111-11-1111')
    mary = Customer('Mary', 'Lee', '222-22-2222')
    alinAccnt = CheckingAccount(alin)
    maryAccnt = SavingAccount(mary)

    alinAccnt.deposit(20000)
    print(alinAccnt)
    alinAccnt.withdraw(5000)
    print(alinAccnt)
    alinAccnt.applyAnnualInterest()
    print(alinAccnt)

    maryAccnt.deposit(10000)
    print(maryAccnt) 
    maryAccnt.withdraw(15000)
    print(maryAccnt)
    maryAccnt.applyAnnualInterest()
    print(maryAccnt)
    
#Main Method

main()
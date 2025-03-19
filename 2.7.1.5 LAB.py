UPPER_AUDIT_AMOUNT = 100000
BANK_ACCOUNT = 'DE6850010517973485'

class bankerror(Exception):
    pass

class bankaccount():
    
    def __init__(self, amount=0):
        self.__accountnumber = BANK_ACCOUNT
        self.__accountbalance = amount

    @property
    def rekening(self):
        return self.__accountnumber
    
    @rekening.setter
    def rekening(self, newnumber):
        print(f"Error: Changing bank details from {self.__accountnumber} to {newnumber} is not permitted")
        return self.__accountnumber
    
    @rekening.deleter
    def rekening(self):
        print(f"Error: Removing {self.__accountnumber} to {newnumber} is not permitted")
        return self.__accountnumber
    
    @property
    def account(self):
        return self.__accountbalance
   
    @account.setter
    def account(self, amount):
        # if self.__accountnumber != newaccount:
        #     raise bankerror("Error: Not authorised to change account number: " + number)
        
        if self.__accountbalance + amount < 0:
            raise bankerror("Negative bank balance is not permitted")
        
        if self.__accountbalance + amount > UPPER_AUDIT_AMOUNT:
            print('Audit: Bankoperation exceeds 100.000€')
        
        self.__accountbalance += amount
        
    @account.deleter
    def account(self):
        if self.__accountbalance == 0:
            print(f"Account: {self.__accountnumber} has been deleted")
        else:
            raise bankerror(f"Cannot delete account number: {self.__accountnumber}, because the balance ({self.__accountbalance}€) is not zero.")
            
# test your class behavior by:
# setting the balance to 1000;
# trying to set the balance to -200;
# trying to set a new value for the account number;
# trying to deposit 1.000.000;
# trying to delete the account attribute containing a non-zero balance.

knab = bankaccount()   
print(f"Account number and initial balance: {knab.account}")    

print('\n# setting the balance to 1000')
knab.account = 1000
print(f"Balance: {knab.account}")   

try:
    print('\n# trying to set the balance to -200 (by subtracting -1200)')
    knab.account = -1200
    print(f"Account number and balance: {knab.account}")             
except bankerror as e:
    print("Error:", e)

print("\n# trying to set a new value for the account number")
knab.rekening = 'GE681232973485'

print('\n# trying to deposit 1.000.000')
knab.account += 1000000
print(f"Account number and balance: {knab.account}")             

try:
    print('\n# trying to delete the account attribute containing a non-zero balance.')
    del knab.account
except bankerror as e:
    print("Error:", e)

print()







    


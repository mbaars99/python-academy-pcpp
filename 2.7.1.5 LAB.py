UPPER_AUDIT_AMOUNT = 100000
BANK_ACCOUNT = 'DE6850010517973485'

class bankerror(Exception):
    pass

class BankAccount():
    
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
       
    @property
    def account(self):
        return self.__accountbalance
   
    @account.setter
    def account(self, amount):
        
        if self.__accountbalance + amount < 0:
            raise bankerror("Negative bank balance is not permitted")
        
        if amount > UPPER_AUDIT_AMOUNT:
            print('Audit: Bankoperation exceeds 100.000€')
        
        self.__accountbalance += amount
                   
    def close_account(self):
        if self.__accountbalance != 0:
            raise bankerror("Cannot delete account number, because the balance is not zero.")
        else:
            print(f"Account: {self.__accountnumber} deleted succesfully")
    
# test your class behavior by:
# setting the balance to 1000;
# trying to set the balance to -200;
# trying to set a new value for the account number;
# trying to deposit 1.000.000;
# trying to delete the account attribute containing a non-zero balance.

knab = BankAccount()   
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
    knab.close_account()
except bankerror as e:
    print("Error:", e)







    

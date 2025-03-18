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
    def rekening(self):
        raise bankerror("Error: Changing bank details is not permitted")    

    @property
    def account(self):
        return self.__accountbalance
   
    @account.setter
    def account(self, amount):
        # if self.__accountnumber != newaccount:
        #     raise bankerror("Error: Not authorised to change account number: " + number)
        
        if self.__accountbalance + amount < 0:
            raise bankerror("Error: Negative bank balance is not permitted for: " + self.__accountnumber)
        
        if self.__accountbalance + amount > UPPER_AUDIT_AMOUNT:
            print('Audit: Bankoperation exceeds 100.000€', end=' ')
        
        self.__accountbalance += amount
        
    @account.deleter
    def account(self, number):
        if self.__accountbalance != 0:
            raise bankerror("Error: Cannot delete account number: " + number + ", because balance is not zero.")

# test your class behavior by:
# setting the balance to 1000;
# trying to set the balance to -200;
# trying to set a new value for the account number;
# trying to deposit 1.000.000;
# trying to delete the account attribute containing a non-zero balance.

knab = bankaccount()   
print(f"Account number and balance: {knab.account}")             

knab.account = 1000
print(f"Account number and balance: {knab.account}")             

knab.account = -200
print(f"Account number and balance: {knab.account}")             

knab.rekening = 'BE91798829733676'



knab.account += 100000
print(f"Account number and balance: {knab.account}")             










    


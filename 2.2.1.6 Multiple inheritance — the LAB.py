class Fax():
    def send(self):
        print('Send() method from Fax Class')

    def print(self):
        print('Print() method from Fax Class')

class Printer():
    def print(self):
        print('Print() method from Printer Class')

class Scanner():
    def scan(self):
        print('Scan() method from Scanner Class')

class SPF(Scanner, Printer, Fax): #'SPF' means 'Scanner', 'Printer', 'Fax')
    pass

class SFP(Scanner, Fax, Printer): #'SFP' means 'Scanner', 'Fax', 'Printer'
    pass

print('SPF')
spf = SPF()
spf.scan()
spf.print()
spf.send()

print()

print('SFP')
sfp = SFP()
sfp.scan()
sfp.print()
sfp.send()







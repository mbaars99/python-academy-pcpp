import abc
import time
from datetime import datetime


class Scanner(abc.ABC):
    @abc.abstractmethod
    def scan_document(self):
        pass
    
    @abc.abstractmethod
    def get_scanner_status(self):
        pass

class Printer(abc.ABC):
    @abc.abstractmethod
    def print_document(self):
        pass
    
    @abc.abstractmethod
    def get_printer_status(self):
        pass

# a cheap device, made of a cheap printer and a cheap scanner, so device capabilities (resolution) should be low;
class MFD1(Scanner, Printer):
    def __init__(self, serial):
        self.serial = serial
        self.max_resolution = "300 DPI"

    def scan_document(self):
        return f"The document has been scanned at {self.max_resolution}"
    
    def get_scanner_status(self):
        return f"Scanner status: {self.max_resolution}, serial {self.serial}"
    
    def print_document(self):
        return f"The document has been printed at {self.max_resolution}"

    def get_printer_status(self):
        return f"Printer status: {self.max_resolution}, serial {self.serial}"

#a medium-priced device allowing additional operations like printing operation history, and the resolution is better than the lower-priced device
class MFD2(Scanner, Printer):
    def __init__(self, serial):
        self.serial = serial
        self.max_resolution = "600 DPI"
        self.history = []

    def log_operation(self, action):
        entry = f"{action} at {self.max_resolution}"
        self.history.append(entry)
        return entry

    def scan_document(self):
        return self.log_operation('The document has been scanned')
    
    def get_scanner_status(self):
        self.history.append(f"Scanner status provided")
        return f"Scanner status: {self.max_resolution}, serial {self.serial}"
    
    def print_document(self):
        return self.log_operation('The document has been printed')

    def get_printer_status(self):
        self.history.append(f"Printer status provided")
        return f"Printer status: {self.max_resolution}, serial {self.serial}"
    
    def get_ops_history(self):
        return "\n".join(self.history)

# a premium device allowing additional operations like printing operation history and fax machine.
class MFD3(Scanner, Printer):
    def __init__(self, serial):
        self.serial = serial
        self.max_resolution = "2400 DPI"
        self.history = []

    def log_operation(self, action):
        entry = f"{datetime.now()} - {action} at {self.max_resolution}"
        display = f"{action} at {self.max_resolution}"
        self.history.append(entry)
        return display

    def scan_document(self):
        return self.log_operation('The document has been scanned')

    def print_document(self):
        return self.log_operation('The document has been printed')
    
    def get_scanner_status(self):
        self.history.append(f"{datetime.now()} - Scanner status provided")
        return f"Scanner status: {self.max_resolution}, serial {self.serial}"
    
    def get_printer_status(self):
        self.history.append(f"{datetime.now()} - Printer status provided")
        return f"Printer status: {self.max_resolution}, serial {self.serial}"
    
    def get_ops_history(self):
        return "\n".join(self.history)
    
    def send_fax(self, number):
        self.history.append(f"{datetime.now()} - Fax sent to: {number}")
        return f"Fax sent to: {number}"

p1 = MFD1('SN202824')
print('-' * 100)
print("a cheap device, made of a cheap printer and a cheap scanner, so device capabilities (resolution) should be low.")
print(p1.scan_document() + ' - ' + p1.get_scanner_status())
print(p1.print_document() + ' - ' + p1.get_printer_status())
print()

p2 = MFD2('SN891573')
print('-' * 100)
print("a medium-priced device allowing additional operations like printing operation history, and the resolution is better than the lower-priced device.")
print(p2.scan_document() + ' - ' + p2.get_scanner_status())
print(p2.print_document() + ' - ' + p2.get_printer_status())
print('\nOperation history:')
print(p2.get_ops_history())
print()

p3 = MFD3('SN215739')
print('-' * 100)
print("a premium device allowing additional operations like printing operation history and fax machine.")
print(p3.scan_document() + ' - ' + p3.get_scanner_status())
print(p3.print_document() + ' - ' + p3.get_printer_status())
print(p3.send_fax('1-844-Say-CISA'))
print('\nOperation history:')
print(p3.get_ops_history())
print()
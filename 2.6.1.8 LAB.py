import abc

class Scanner(abc.ABC):
    @abc.abstractmethod
    def scan_document(self):
        pass
    
    @abc.abstractmethod
    def get_scanner_status(self):
        pass
    
class MFD1(Scanner):
    def __init__(self, capabilties, serial):
        super().__init__()
        self.capabilties = capabilties
        self.serial = serial

    def scan_document(self):
        return 'The document has been scanned'
    
    def get_scanner_status(self):
        return f"Capabilities: {self.capabilties}, serial {self.serial}"

class Printer(abc.ABC):
    @abc.abstractmethod
    def print_document(self):
        pass
    
    @abc.abstractmethod
    def get_printer_status(self):
        pass

class MFD2(Printer):
    def __init__(self, capabilties, serial):
        super().__init__()
        self.capabilties = capabilties
        self.serial = serial

    def print_document(self):
        return 'The document has been printed'
    
    def get_printer_status(self):
        return f"Capabilities: {self.capabilties}, serial {self.serial}"

class MFD3(Printer):
    def __init__(self, capabilties, serial):
        super().__init__()
        self.capabilties = capabilties
        self.serial = serial

    def print_document(self):
        return 'The document has been printed'
    
    def get_printer_status(self):
        return f"Capabilities: {self.capabilties}, serial: {self.serial}"

   
p1 = MFD1('cheap device' + ', low resolution', 'SN202824')
print(p1.scan_document())
print(p1.get_scanner_status())

print()


p2 = MFD2('printing operation history' + ', medium resolution', 'SN891573')
print(p2.print_document())
print(p2.get_printer_status())

print()

p3 = MFD2('printing operation history' + ', high resolution' + ', fax machine', 'SN989900')
print(p2.print_document())
print(p2.get_printer_status())

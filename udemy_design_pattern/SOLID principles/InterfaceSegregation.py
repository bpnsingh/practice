from abc import abstractclassmethod, abstractmethod


class Machine:
    def print(self,document):
        raise NotImplementedError()
    def fax(self,document):
        raise NotImplementedError()
    def scan(self,document):
        raise NotImplementedError()

class MultifunctionPrinter(Machine):
    def print(self,document):
        pass
    def fax(self,document):
        pass
    def scan(self,document):
        pass

class OldPrinter(Machine):
    def print(self, document):
        # ok - print stuff
        pass

    def fax(self, document):
        pass  # do-nothing

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')

p1 = OldPrinter()
p1.print('document')
#p1.scan('test')

#Solution: Better approach
class Printer:
    @abstractmethod
    def print(self,document):
        pass

class Scanner:
    @abstractmethod
    def scan(self,document):
        pass

class MyPrinter(Printer):
    def print(self,document):
        print(document)

class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        pass  # something meaningful

class MultiFunctionDevice(Printer, Scanner):  # , Fax, etc
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)


printer = OldPrinter()
printer.fax(123)  # nothing happens
printer.scan(123)  # oops!
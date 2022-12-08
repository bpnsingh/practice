class Journal:
    def __init__(self):
        self.enteries = []
        self.count = 0

    def add_entry(self,text):
        self.enteries.append(text)
        self.count +=1

    def remove_entry(self,pos):
        del self.enteries[pos]

    def __str__(self):
        return "\n".join(self.enteries)
        #return "\t".join(self.enteries)

    def save(self,filename):
        file = open(filename, 'w')
        file.write(str(self))

class WriteManager:
    @staticmethod
    def save(journal,file):
        file = open(file, 'w')
        file.write(str(journal))
        file.close()




instanceJournal = Journal()
instanceJournal.add_entry("I cried today")
instanceJournal.add_entry("I love my job")
instanceJournal.add_entry("I love my Life")
instaceWrite = WriteManager()
instaceWrite.save(instanceJournal,'abc.txt')
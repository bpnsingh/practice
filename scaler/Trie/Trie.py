class TrieNode:
    def __init__(self,value=None):
        self.value = value
        self.child = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        parent = self.root
        for i,char in enumerate(word):
            if char not in parent.child:
                parent.child[char] = TrieNode(char)
            parent = parent.child[char]
        parent.isEnd = True

    def search(self,word):
        parent = self.root
        for ch in word:
            if ch not in parent.child:
                return False
            parent = parent.child[ch]
        return parent.isEnd
    def startswith(self,word):
        parent = self.root
        for ch in word:
            if ch not in parent.child:
                return False
            parent = parent.child


if __name__ == '__main__':
    word_list = ['abc','abde','abcd','glo','glow','abd','ab']
    search_list = ['ab', 'banana', 'dog', 'glo']
    mytrie = Trie()
    for word in word_list:
        mytrie.insert(word)
    for word in search_list:
        print (mytrie.search(word))

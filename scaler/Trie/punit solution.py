'''
Insert words in dictionary and check whether words exist in

'''

class Trie:
    def __init__(self):
        self.hashmap={}
        self.end = False
    def insert(self,root,word):
        curr = root
        for ch in word:
            if ch not in curr.hashmap:
                newnode=Trie()
                curr.hashmap[ch]=newnode
            curr = curr.hashmap[ch]
        curr.end = True
    def search(self,root,word):
        curr = root
        for ch in word:
            if ch not in curr.hashmap:
                return False
            else:
                curr=curr.hashmap[ch]
        return curr.end


class Solution:
    # def _init_(self):
    #     self.trie_node = TrieNode()
    words = ['cat','dog','zebra']
    root = Trie()
    for word in words:
        root.insert(root,word)
    TC = ['dog','bhalu']
    for word in TC:
        print (root.search(root,word))



'''
Given a list of N words, find the shortest unique prefix to represent each word in the list.

NOTE: Assume that no word is the prefix of another. In other words, the representation is always possible

Problem Constraints
1 <= Sum of length of all words <= 106
Input Format
First and only argument is a string array of size N.

Output Format
Return a string array B where B[i] denotes the shortest unique prefix to represent the ith word.

Example Input
Input 1:
 A = ["zebra", "dog", "duck", "dove"]
Input 2:

A = ["apple", "ball", "cat"]


Example Output
Output 1:

 ["z", "dog", "du", "dov"]
Output 2:

 ["a", "b", "c"]

'''
from day23.prrintdescending import print_dsc


class TrieNode:
    def __init__(self,value=None):
        #self.value = value
        self.child = {}
        self.isEnd = False
        self.freq = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        parent = self.root
        for i,char in enumerate(word):
            if char not in parent.child:
                parent.child[char] = TrieNode(char)
                parent.freq = 0
            parent.freq += 1
            parent = parent.child[char]
        parent.isEnd = True

    def search(self,word):
        parent = self.root
        ans=''
        result=[]
        for ch in word:
            ans += ch
            if parent[ch].freq == 1:
                return ans
            else:
                parent = parent.child[ch]
        return ans

if __name__ == '__main__':
    word_list = ["zebra", "dog", "duck", "dove"]
    mytrie = Trie()
    ans= []
    for word in word_list:
        mytrie.insert(word)
    for word in word_list:
        temp=mytrie.search(word)
        ans.append(temp)
    print(ans)




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
    def __init__(self):
        self.hashmap = {}
        self.end = False
        self.count = 0


class Solution:
    # def _init_(self):
    #     self.trie_node = TrieNode()
    def insert(self, root, word):
        curr = root
        for char in word:
            if char not in curr.hashmap:
                new_node = TrieNode()
                new_node.count += 1
                curr.hashmap[char] = new_node
            else:
                curr.hashmap[char].count += 1
            curr = curr.hashmap[char]
        curr.end = True

    def search_prefix(self, word, root):
        prefix = ''
        curr = root
        for char in word:
            # print (curr.hashmap)
            if curr.hashmap[char].count == 1:
                prefix += char
                break
            else:
                prefix += char
                curr = curr.hashmap[char]
        return prefix

        # @param A : list of strings
        # @return a list of strings
    def prefix(self, A):
        root = TrieNode()
        curr = root
        ans = []
        for word in A:
            self.insert(root, word)
        for word in A:
            pref = self.search_prefix(word, root)
            ans.append(pref)
            # print (ans)
        return ans



scaler = Solution()
word_list = ["zebra", "dog", "duck", "dove"]
print(scaler.prefix(word_list))




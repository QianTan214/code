"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string 
containing only letters a-z or .. 
A . means it can represent any one letter.

"""

"""
解题思路: 字典树，在查找的时候，使用dfs，如果遇到点，要遍历所有子树
"""
# 208题

# method 1:

最后dfs不是特别明白

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.d
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["#"] = True
                  

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.dfs(self.d, word, 0)
                
    def dfs(self, node, word, i):
        
        if i == len(word):
            return "#" in node
        if word[i] == ".":
            for child in node:
                if child != "#" and self.dfs(node[child], word, i+1):
                    return True
            return False
        if word[i] not in node:
            return False
        return self.dfs(node[word[i]], word, i+1)
            
                    
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# method 2:

class WordDictionary:

    def __init__(self):
        """ Initialize your data structure here. """
        self.dic = defaultdict(set)

    def addWord(self, word: str) -> None:
        """ Adds a word into the data structure. """
        self.dic[len(word)].add(word)

    def search(self, word: str) -> bool:
        """ Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. """
        if '.' not in word:
            return word in self.dic[len(word)]
        for v in self.dic[len(word)]:
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else:
                return True
        return False
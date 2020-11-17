"""
Implement a trie with insert, search, and startsWith methods.

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
"""

# 字典树/前缀树 Trie (Prefix Tree)
# 字典里套字典

"""
解题思路: 字典树的每一个节点都是一个map，key是当前字母，value是所有的子树，
如果一个单词结束，就在下方插入一个#作为标记

"""
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.dic
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["#"] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        
        cur = self.dic
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return "#" in cur # 看"#"是否在cur字典中
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        
        cur = self.dic
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Iterate over letters adding children
        cur = self.root

        for letter in word:
            # Add letter if not present
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        # Iterate over letters looking for children
        cur = self.root
        for letter in word:
            # Word does not exist
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        # Same as search without checking for isEnd
        cur = self.root
        for letter in prefix:
            # Word does not exist
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

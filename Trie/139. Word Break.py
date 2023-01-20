class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Trie
        # 1. Build a trie from wordDict
        # 2. Iterate through s looking for words
        # 3. Create tuples of word starts and end
        # 4. Use DP to find if there is a path to the end

        # Build trie
        root = TrieNode()
        for word in wordDict:
            cur = root
            for letter in word:
                cur = cur.children[letter]
            cur.isEnd = True

        # Search through the trie for words
        words = []
        for i, letter in enumerate(s):
            cur = root
            cur_index = i
            # Search for each starting letter
            while cur_index < len(s):
                # Check if letter is in trie
                # If it's not, return
                # If it is, go to next letter and check for is word
                cur_letter = s[cur_index]
                if cur_letter in cur.children:
                    cur = cur.children[cur_letter]
                    if cur.isEnd:
                        words.append((i, cur_index))
                    cur_index += 1
                else:
                    break

        # Dynamic programming
        dp = [False for _ in range(len(s) + 1)]
        # Start of string is true
        dp[0] = True
        # If start of word has been part of a word
        # Set end of word to be part of next word
        for start, end in words:
            if dp[start]:
                dp[end + 1] = True

        # Return true if path to end of string exists
        return dp[-1]

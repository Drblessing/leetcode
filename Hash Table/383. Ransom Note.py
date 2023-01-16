class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Hash Table
        # 1. Iterate through ransomNote and magazine
        # 2. Create hash table of word counts
        # 3. Check that magazine has >= ransomNote value
        # 4. Optimize by only creating one hashtable for magazine

        # Add to inventory
        hash_table = defaultdict(int)
        for letter in magazine:
            hash_table[letter] += 1
        # Remove from inventory
        for letter in ransomNote:
            hash_table[letter] -= 1
            # Check for running out
            if hash_table[letter] < 0:
                return False
        # All letters present
        return True

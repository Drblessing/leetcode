class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Prime facotrization
        # 1. Turn words into prime numbers
        # 2. Compare

        # 1. Build letter to prime dict
        primes = [
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
            53,
            59,
            61,
            67,
            71,
            73,
            79,
            83,
            89,
            97,
            101,
        ]
        alphabet = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
        alphabet_to_prime = {}

        for i in range(len(alphabet)):
            alphabet_to_prime[alphabet[i]] = primes[i]

        # Turn into prime numbers and compare
        strs_to_prime = defaultdict(list)
        for word in strs:
            multiple = 1
            for char in word:
                multiple = alphabet_to_prime[char] * multiple
            strs_to_prime[multiple].append(word)

        return list(strs_to_prime.values())

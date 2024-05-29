class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Init hashmap to store losses count
        losses_count = defaultdict(int)
        # Iterate through matches
        for winner, loser in matches:
            # Add winner to hashmap with default value 0
            # if not in hashmap
            losses_count[winner]
            # Add 1 to losers count
            losses_count[loser] += 1
        # Iterate over hashmap to gather one loss and no loss players
        one_loss = []
        no_loss = []
        for player, losses in losses_count.items():
            if losses == 0:
                no_loss.append(player)
            elif losses == 1:
                one_loss.append(player)
        # Return sorted lists
        return [sorted(no_loss), sorted(one_loss)]


# Time Complexity: O(n*log(n)) where n is the number of matches
# hashmap operations O(1) and sorting is O(n*log(n))
# Space Complexity: O(n) where n is the number of matches
# we create a hashmap to store all players and their losses
# which requires O(n) space in the worst case scenario

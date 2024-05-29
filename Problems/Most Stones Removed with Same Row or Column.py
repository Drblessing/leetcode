class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        def removePoints(row,col):
            stones_set.discard((row,col))
            for col_new in row_dict[row]:
                if (row,col_new) in stones_set:
                    removePoints(row,col_new)
            
            for row_new in col_dict[col]:
                if (row_new,col) in stones_set:
                    removePoints(row_new,col)
        
        
        stones_set = {(row,col) for row,col in stones}
        
        cnt = 0 
        
        row_dict = defaultdict(list)
        col_dict = defaultdict(list)
        
        for row,col in stones_set:
            row_dict[row].append(col)
            col_dict[col].append(row)
        
        for stone in stones:
            
            if tuple(stone) in stones_set:
                cnt += 1
                removePoints(stone[0],stone[1])
                
        return len(stones) - cnt
            
            
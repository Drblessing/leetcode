class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rect1Area = abs(ax2-ax1)*abs(ay2-ay1)
        rect2Area = abs(bx2-bx1)*abs(by2-by1)
        
        # Sort x-dimensions
        xDimSort = sorted([(ax1,1),(bx1,2),(ax2,1),(bx2,2)])
        xOverlap = len(set([i[1] for i in xDimSort[:2]])) == 2
        
        # Sort y-dim
        yDimSort = sorted([(ay1,1),(by1,2),(ay2,1),(by2,2)])
        yOverlap = len(set([i[1] for i in yDimSort[:2]])) == 2
        
        # No x-overlap or y-overlap
        if (not(xOverlap)) or (not(yOverlap)): return rect1Area + rect2Area
        
        # Calculate x and y overlap, middle dim
        overlapArea = abs(xDimSort[1][0] - xDimSort[2][0]) * abs(yDimSort[1][0] - yDimSort[2][0])
        
        return rect1Area + rect2Area - overlapArea
        
        
        
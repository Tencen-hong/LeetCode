class Solution:
    '''
        解方程：
        4X + 2Y = tomatoSlices
        X + Y = cheeseSlices
    '''

    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        X = (tomatoSlices - 2*cheeseSlices)/2
        if int(X) == X and X >= 0 and cheeseSlices-X >= 0:
            return [int(X), int(cheeseSlices-X)]
        else:
            return []

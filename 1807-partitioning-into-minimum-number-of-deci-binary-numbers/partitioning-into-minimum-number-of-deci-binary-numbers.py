class Solution:
    def minPartitions(self, n: str) -> int:
        mAx = 0

        for val in n:
            currChVal = int(val)
            
            mAx = max(mAx, currChVal)

        return mAx
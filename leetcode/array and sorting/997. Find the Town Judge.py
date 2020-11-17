class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        """
        法官入度N-1，即大家都相信他。出度0，即不相信任何人，法官入度减出度是N-1
        """

        count = [0] * (N+1)
        # N个人，N+1的array，因为想要让每个人的ID和count array里的index对应，用index表示人的ID

        for [x, y] in trust: # 也可直接写成x,y，不加[]
            count[x] -= 1 # x相信别人，x出度减一
            count[y] += 1 # y被相信，y入度加一
        
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1
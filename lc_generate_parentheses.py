class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(k, n):
            if k == 0 and n == 0:
                return [[]]
            col = []
            if k >= 1:
                close_res = generate(k - 1, n)
                for i in close_res:
                    col.append([')'] + i)
            if n >= 1:
                open_res = generate(k + 1, n - 1)
                for j in open_res:
                    col.append(['('] + j)
            return col
        return [''.join(x) for x in generate(0, n)]
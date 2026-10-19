class Solution:
    def countBits(self, n: int) -> list[int]:
        output_arr = []
        for i in range(0,n+1):
            j = i
            summ_digits = 0
            while True:
                summ_digits = summ_digits + (j%2)
                if j==0 or j==1:
                    output_arr.append(summ_digits)
                    break
                j=int(j/2)
        return output_arr

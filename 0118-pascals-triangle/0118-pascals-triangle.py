class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        if numRows == 1:
            output.append([1])
            return output
        if numRows == 2:
            output.append([1])
            output.append([1,1])
            return output

        if numRows > 2:
            output.append([1])
            output.append([1,1])
            mem = 2
            while mem < numRows:
                result = []
                for i in range(mem+1):
                    if i == 0 or i == mem:
                        result.append(1)
                    else:
                        result.append(output[-1][i-1] + output[-1][i])
                output.append(result)
                mem += 1
            
            return output

        

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binary1 = int(a, 2)
        binary2 = int(b, 2)

        return format(binary1 + binary2, 'b')

        # By using format(number, 'b'), we can convert a number to binary. 
        # By using bin(number), we can convert a binary to number, but with the prefix '0b'. So, through bin(number)[2:], we can slice the first two letter to get only binary in type string.  
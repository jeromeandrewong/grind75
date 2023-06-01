class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        pa, pb = len(a) - 1, len(b) - 1
        carry = 0

        while carry or pa >= 0 or pb >= 0:
            total = carry
            if pa >= 0:
                total += a[pa]
                pa -= 1

            if pb >= 0:
                total += b[pb]
                pb -= 1
            result.append(str(total % 2))
            carry = total // 2

        return "".join(reversed(result))

    # result = ['0','0','1']
    # carry = 0

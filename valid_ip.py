# https://leetcode.com/problems/validate-ip-address/
# Solution reasonable

class Solution:
    def validIPAddress(self, IP: str) -> str:
        # Attempt IPv4
        check_4 = IP.split('.')
        if len(check_4) == 4:
            for num in check_4:
                try:
                    if 0 > int(num) or int(num) > 255 or (num[0] == '0' and num != '0'):
                        return 'Neither'
                except:
                    return 'Neither'
            return "IPv4"
        # Attempt IPv6
        check_6 = IP.split(':')
        if len(check_6) == 8:
            for block in check_6:
                try:
                    blank = int(block, 16)
                    if len(block) >= 5 or len(block) < 1:
                        return 'Neither'
                except:
                    return 'Neither'
            return 'IPv6'
        return 'Neither'
                    
        
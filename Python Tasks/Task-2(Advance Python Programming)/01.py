'''
Topic : Defanging an IP Address
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

refer full question : https://leetcode.com/problems/defanging-an-ip-address/
'''
# Solution

# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         address = address.split('.')
#         return "[.]".join(address)

class Solution:
    def defangIPaddr(address):
        address = address.split('.')
        return '[.]'.join(address)

ip = input('Enter IP address : ')
obj = Solution
print(Solution.defangIPaddr(ip))

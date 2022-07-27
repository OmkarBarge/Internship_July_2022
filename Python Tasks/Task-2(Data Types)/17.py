'''
Topic : The Captain's Room

refer full question : https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true
'''
#Solution - 1

k, rooms, single, multiple = input(), input().split(), set(), set()

for room in rooms: single.add(room) if room not in single else multiple.add(room)

print(single.difference(multiple).pop())


# Solution - 2

k,arr = int(input()),list(map(int, input().split()))

myset = set(arr)

print(((sum(myset)*k)-(sum(arr)))//(k-1))
print(sum(myset))
print(sum(arr))
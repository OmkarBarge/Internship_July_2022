'''
Topic : The Minion Game

refer full question : https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
'''

#Solution

def minion_game(string):
    # your code goes here
    k = 0
    s = 0
    vowels = "AaEeIiOoUu"
    for i in range(len(string)):
        if string[i] in vowels:
            k = k + len(string) - i
        else:
            s = s + len(string) - i

    if k > s:
        print("Kevin", k)
    elif k == s:
        print("Draw")
    else:
        print("Stuart", s)

minion_game('BANANA')
'''
Topic : What's Your Name?

refer full question : https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true
'''


def print_full_name(first, last):
    # Write your code here
    st = "Hello {} {} ! You just delved into python."
    return (st.format(first,last))
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print(print_full_name(first_name, last_name))
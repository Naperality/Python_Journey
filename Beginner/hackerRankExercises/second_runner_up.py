# Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score. You are given  scores. 
# Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains . The second line contains an array   of  integers each separated by a space.

def secondRunner(arr):
    arr.sort()
    for num in arr[::-1]:
        if num < max(arr):
            return num

arr = [2,3,6,6,5,7,8,8,2]
print(secondRunner(arr))

# hacker rank style 
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    max_num = max(arr)
    for num in arr[::-1]:
        if num < max_num:
            break
    print(num)
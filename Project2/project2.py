'''
Project 2 - Name That Triangle - Spring 2022  
Author: Your name and VT pid here (not your full id)

Describe the program here.

I have neither given or received unauthorized assistance on this assignment.
Signed:  Type your name here
'''
import math
def main():
    print("Welcome to the Triangle Evaluator!")
    done = False
    while(not done):
        s1 = get_side(1)
        s2 = get_side(2)
        s3 = get_side(3)
        category = categorize_triangle(s1,s2,s3)
        area = compute_area(s1,s2,s3)
        print("\n")
        print_results(category,area)
        print("\n")
        done_ans = input("Process another triangle (y or n)? ")
        print("\n")
        if (done_ans == 'n'):
            done = True
            break
        elif(done_ans == 'y'):
            done = False
    print("Thanks for using the Triangle Evaluator!")

def get_side(side_num):
    valid = False
    side_len = int(input("Enter side length #" +str(side_num)))
    while(not valid):
        if (side_len <= 0):
            side_len = int(input("Invalid side value. Please reenter: "))
        else:
            valid = True
    return side_len

def categorize_triangle(s1,s2,s3):
    category =""
    if (s1 == s2 == s3):
        category ="equilateral"
    elif(s1 == s2 or s2 == s3 or s1 == s3):
        category ="isosceles"
    else:
        category ="scalene"
    return category

def compute_area(s1,s2,s3):
    s = (s1+s2+s3) / 2
    area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    return area

def print_results(category,area):
    if(category[0] == 's'):
        print("That is a",category,"triangle with area",str(area))
    else:
        print("That is an",category,"triangle with area",str(area))

if __name__ == '__main__':
    main()
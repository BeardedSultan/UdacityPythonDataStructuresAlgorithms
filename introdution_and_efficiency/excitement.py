# Write a function called "show_excitement" where the string
# "I am super excited for this course!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.
# Don't just copy/paste it 5 times into a single variable!


def show_excitement():
    # Your code goes here!
    string = "I am super excited for this course! "
    output = "" 
    for i in range(0, 5):
        output += string
    return output

print(show_excitement())

#efficiency practice
#1: O(n)
#2: O(1)
#3: O(nm)
#4: O(n^2)
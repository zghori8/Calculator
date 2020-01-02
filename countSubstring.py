from collections import Counter

def find_Substring(string, substring):
    total = Counter([string[i: i + len(substring)] for i in range(len(string))])
    return total[substring]
    
string = input("Input string: ")
substring = input("Input substring: ")

print(find_Substring(string, substring))

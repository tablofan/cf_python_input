# Example solution to:
# https://codeforces.com/problemset/problem/4/A

# Fast Input
import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    # Take Input
    n = int(input())
    
    # Print output instead of returning the answer
    if n>2 and not n%2:
        print("YES")
    else:
        print("NO")
    
if __name__ == "__main__":
    # Define globals here
    main()

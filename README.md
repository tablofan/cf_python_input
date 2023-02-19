# CF Python Guide

This guide will go through the basics of taking input with Python in Codeforces.

## Template
Base template, I recommend starting with this if you have no idea what you're doing. Feel free to customize as you see fit.
```python
# A significantly faster input function
import sys  
input = sys.stdin.readline  
  
def solve():  
    # write code here
  
def main():
	# Change 'int(input())' to '1' if question only gives 1 test case  
    for _ in range(int(input())):  
        solve()  
  
if __name__ == "__main__":
	# Declare any global variables here  
    main()
```

## Compiler
Recommended:
Latest version of Pypy3

## Taking Input
input() takes a whole line as a string. It's our job to process the input into the format we want.
If we want to take a line as a string, then simply
```python
string = input()
```
**Example 1:**
> The first line contains an integer **t**. Then **t** test cases follow
> The first line of each test case contains one integer **n**
> The second line contains **n** distinct integers
> 
> Example:
>2
>5
>1 5 4 3 2
>8
>2 1 3 4 5 6 8 7

In this case, the 2 is dealt with by our template.
Each of our solve function would then look like:
```python
    def solve():
	n = int(input())
	a = [int(i) for i in input().split()]
	# OR
	a = map(int, input().split())
	# str.split() defaults to splitting by whitespace
```

**Example 2:**
> The first and the only line of the input file contains two numbers **n** and **r**
> 
> Example:
>3 5

There is only 1 test case in each test so we need to change our main function to
```python
def main(): 
    for _ in range(1):  
        solve()
    # or just
    solve()
```

```python
def solve():
    n, r = map(int, input().split())
```

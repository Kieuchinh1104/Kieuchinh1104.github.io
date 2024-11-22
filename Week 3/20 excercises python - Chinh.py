"""
def checkOddEven(x):
    if(x % 2 ==0):
        print("Even")
    else:
        print("Odd")  
checkOddEven(9)  

"""

"""
def check_conditions(a, b, flag):
    if (a >= 0) != (b >= 0) and (flag == False):
        return True
    elif (a < 0) and (b < 0) and (flag == True):
        return True
    else:
        return False
print(check_conditions(5, -3, False))  

"""
"""
def friends_in_trouble(j_angry, s_angry):
    if (j_angry and s_angry) or (not j_angry and not s_angry):
        return True
    else:
        return False
print(friends_in_trouble(True, True))   
print(friends_in_trouble(True, False))  

"""

"""
def cat_hat(str):
    cat_count = str.count("cat")
    hat_count = str.count("hat")
    return cat_count == hat_count
print(cat_hat("catandhat"))            
print(cat_hat("catandhatcat"))         

"""

"""
def multiplicationTable(N):
    for i in range(1, 11): 
        print(i * N, end =" ") 

multiplicationTable(5)

"""

"""
def stringJumper(str):
    for i in range(0, len(str), 2): 
        print(str[i], end ="") 

stringJumper("hello world")

"""
"""
def printInDecreasing(x):
    while(x >= 0):
        print(x, end=" ")
        x -= 1

printInDecreasing(5)

"""
"""
def printIncreasingPower(x):
    i = 1
    while i <= x:
        print(f"{i}2", end=" ")
        i += 1

printIncreasingPower(5)

"""
"""
def neg(n):
    while n <= 0:
        print(n, end=" ")
        n += 1  

def pos(n):
    while n > 0:
        print(n - 1, end=" ")
        n -= 1  

def print_numbers(n):
    if n < 0:
        neg(n)
    else:
        pos(n)

print_numbers(-5)  
print("\n")        
print_numbers(5)   

"""
"""
class ArrayUtils:
    def get_min_max(self, arr):

        if not arr:
            return []  

        min_element = arr[0]
        max_element = arr[0]

        for num in arr:
            if num < min_element:
                min_element = num  
            if num > max_element:
                max_element = num  

        return [min_element, max_element]

array_utils = ArrayUtils()
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
result = array_utils.get_min_max(arr)
print(result)  

"""
"""
class Solution:    
    def doUnion(self, arr1, arr2):
        union_set = set(arr1) | set(arr2)
        return len(union_set)

solution = Solution()
arr1 = [1, 2, 2, 3, 4]
arr2 = [3, 4, 4, 5, 6]
result = solution.doUnion(arr1, arr2)
print(result)  

"""
"""
class Solution:
    def intersection(self, arr1, arr2):
        i, j = 0, 0
        result = []
        
        while i < len(arr1) and j < len(arr2):
            if arr1[i] == arr2[j]:
                if len(result) == 0 or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1
        
        return result
    
solution = Solution()
arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 4, 6]
result = solution.intersection(arr1, arr2)
print(result)  

"""
"""
def trim(str_input):
    return str_input.strip()

def exists(str_input, x):
    return str_input.find(x)  

def exists_bool(str_input, x):
    return x in str_input  

def titleIt(str_input):
    return str_input.title()

def casesSwap(str_input):
    return str_input.swapcase()

if __name__ == "__main__":
    original_str = "   hello WORLD! welcome to PYTHON programming.   "
    substring = "WORLD"
    
    trimmed_str = trim(original_str)
    print("Trimmed String:", f"'{trimmed_str}'")
    
    index = exists(original_str, substring)
    print(f"Index of '{substring}':", index)
    
    exists_flag = exists_bool(original_str, substring)
    print(f"Does '{substring}' exist in the string?", exists_flag)
    
    title_cased = titleIt(original_str)
    print("Title Case:", f"'{title_cased}'")
    
    swapped_case = casesSwap(original_str)
    print("Swapcase:", f"'{swapped_case}'")
    
"""
"""
class Solution:
    def toLower(self, s: str) -> str:
        return s.lower()

sol = Solution()
print(sol.toLower("MixedCASE"))       

"""
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split('.')
        
        words.reverse()
        
        return '.'.join(words)

sol = Solution()

print(sol.reverseWords("one.two.three"))   # Output: "three.two.one"

"""
"""
def welcomeAboard(name):
    print(f"Welcome {name}")

welcomeAboard("John")  # Output: "Welcome John"

"""
"""
def join_middle(bound_by, tag_name):
    mid_index = len(bound_by) // 2  
   
    return bound_by[0:mid_index] + tag_name + bound_by[mid_index:]

print(join_middle("[]", "item"))       
print(join_middle("<>", "content"))     

"""
"""
def combo_string(a, b):
    if len(a) < len(b):
        short, longer = a, b
    else:
        short, longer = b, a

    return short+longer+short

print(combo_string("cat", "elephant"))  

"""
"""
class Solution:
    def isPalindrome(self, S):
        return S == S[::-1]

sol = Solution()
print(sol.isPalindrome("madam"))      
print(sol.isPalindrome("hello"))      

"""
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        seen = set()       
        result = []        
        
        for char in s:    
            if char not in seen:  
                seen.add(char)     
                result.append(char) 
        
        return ''.join(result)  

sol = Solution()
print(sol.removeDuplicates("Programming"))   

"""
class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False
        
        return sorted(str1) == sorted(str2)

sol = Solution()
print(sol.isAnagram("listen", "silent"))  
print(sol.isAnagram("hello", "world"))  


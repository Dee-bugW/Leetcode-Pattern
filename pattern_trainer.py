statistics = {
    "Hash Map":0,
    "Stack":0,
    "Math":0
}

statistics["Hash Map"] += 1
statistics["Stack"] += 1
statistics["Math"] += 1


def main():
    while True:
        print("========== Pattern Trainer ==========")
        print("1. Two Sum")
        print("2. Valid Parentheses")
        print("3.Palindrome Number")
        print("4.Roman to Integer")
        print("5. Exit")
        print("6.View Statistics?")

        choice = input("Select an option: ")

        if choice == "1":
            two_sum_trainer()
        elif choice == "2":
            valid_parentheses_trainer() 
        elif choice == "3":
            palindrome_trainer() 
        elif choice == "4":
            roman_trainer()
        elif choice == "5":
            print("exited.")
            break
        elif choice == "6":
            show_statistics()
        else:
            print("invalid")


#two sum
def two_sum_trainer():
    try:
        nums = list(map(int, input("Enter numbers: "). split()))
        target = int(input("Target: "))

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                print("Answer: ", [seen[complement], i])
                print("Pattern: Hash Map")
                return 
            else:
                seen[num] = i
        print("no solution")
    except ValueError:
        print("only enter integers seperated by spaces")

#valid parentheses
def valid_parentheses_trainer():
    s = input("Enter parentheses string: ")
    pairs = {
        ")": "(",
        "]":"[",
        "}":"{"
    }

    stack = []

    for char in s:
        if char in pairs:
            if not stack or stack.pop() != pairs:
                print("invalid")
                return 
            else:
                stack.append(char)
            #valid if stack empty, invalid if stack still has elements
    print("Valid" if not stack else "Invalid")

#palindrome 
def palindrome_trainer():
    x = int(input("Enter a long number: "))

    original = x
    reversed = 0 
    while x > 0:
        digit = x % 10
        reversed = reversed * 10 + digit 
        x //= 10

    if original == reversed:
        print("Palindrome")
    else:
        print("Not Palindrome")

#roman
def roman_trainer():
    s = input("Roman numeral: ").upper()
    roman = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }

    result = 0
    for i in range(len(s)):
        current = roman[s[i]]
        if i + 1 < len(s) and current < roman[s[i + 1]]:
            result -= current 
        else:
            result += current 
    print("Integer: ", result)

#statistics
def show_statistics():
    print("Stats: ")
    for key, value in statistics.items():
        print(f"{key}: {value}")

main() 
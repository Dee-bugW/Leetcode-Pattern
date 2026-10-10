# Interview-Pattern
Common Leetcode Problems and their patterns (EASY) - Python

1. Hash Map
   example:
     seen = {}
     for i, num in enumerate(nums):
       complement = target - num
       if complement in seen:
         return [seen[complement], i]
       seen[num] = i

2. Two Pointers
   example:
     left = 0
     right = len(s) - 1
     while left < right:
       left += 1
       right -= 1

3. Stack
   example:
     stack = []
     for char in s:
       stack.append(char)
     stack.pop()

4. String Processing
   example:
     split()
     lower()
     join()

5. Math Pattern
   example:
     %, //, *=, +=

6. Recursion
   example:
     def traverse(node):
       if node is None:
         return
       traverse(node.left)
       print(node.val)
       traverse(node.right)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

Example:
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]
Here is a function signature example:

class Solution:
  def getRange(self, arr, target):
    # Fill this in.

# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]
"""


class Solution:
    def __init__(self):
        self.findings = [-1, -1]

    def getRange(self, arr, target):
        for i in range(len(arr)):
            if self.findings[0] != -1 and self.findings[1] != -1:
                break
            head = i
            tail = len(arr)-1-i
            if self.findings[0] == -1 and arr[head] == target:
                self.findings[0] = head
            if self.findings[1] == -1 and arr[tail] == target:
                self.findings[1] = tail
        return self.findings


# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string, find the length of the longest substring without repeating characters.

class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.

print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        indexes = {}
        substr = ''
        length = 0
        for i, c in enumerate(s):
            substr += c
            if c not in indexes:
                indexes[c] = i
            else:
                if len(substr) > length:
                    length = len(substr)
                substr = c
        return length


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10

class Solution:
  def isAnagram(seld,s,t):
    from collections import Counter
    return Counter(s) == Counter(t)

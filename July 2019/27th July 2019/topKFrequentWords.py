# Source: https://leetcode.com/problems/top-k-frequent-words/

# Level: Medium

# Date: 27th July 2019, 2019


# Given a non-empty list of words, return the k most frequent elements.
#
# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency,
# then the word with the lower alphabetical order comes first.
#
# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
# with the number of occurrence being 4, 3, 2 and 1 respectively.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.


class Solution:
    def topKFrequent(self, words, k: int):
        hashMap = {}
        heap = []

        for word in words:
            if word in hashMap:
                hashMap[word] = shift(heap, hashMap[word], hashMap)
            else:
                heap.append([word, 0])
                hashMap[word] = 0
                hashMap[word] = shift(heap, len(heap) - 1, hashMap)

        return [word[0] for word in heap[:k]]


def shift(array, elemIndex, hashMap):
    array[elemIndex][1] += 1

    while elemIndex > 0:
        prevIndex = elemIndex - 1
        previousCount = array[prevIndex][1]
        elemCount = array[elemIndex][1]

        if elemCount > previousCount:
            array[prevIndex], array[elemIndex] = array[elemIndex], array[prevIndex]
        elif elemCount == previousCount and array[prevIndex][0] > array[elemIndex][0]:
            array[prevIndex], array[elemIndex] = array[elemIndex], array[prevIndex]
        else:
            break

        hashMap[array[elemIndex][0]] = elemIndex
        hashMap[array[prevIndex][0]] = prevIndex
        elemIndex -= 1

    return elemIndex

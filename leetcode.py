'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
'''


def twoNumsSun():
    nums = [eval(x) for x in input().split()]
    target = int(input("请输入target"))
    list = []
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                list.append(i)
                list.append(j)
                return list


'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
'''


def jiafa():
    list1 = [eval(x) for x in input().split()]
    list2 = [eval(x) for x in input().split()]
    result = []
    jinwei = 0
    for i in range(len(list1)):
        for j in range(i, len(list2)):
            num = list1[i] + list2[j] + jinwei
            if num >= 10:
                jinwei = 1
                result.append(0)
            else:
                result.append(num)
            break
    return result


'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。'''


def zczc():
    s = input()
    length = len(s)
    max = 0
    result = 0
    for i in range(length):
        for j in range(i, length):
            if s[j] not in s[i:j]:
                max += 1
            else:
                break
        result = max if max > result else result
        max = 0
    return result


'''给你一个字符串 s，找到 s 中最长的回文子串。'''


def longestPalindrome():
    s = input()
    length = len(s)
    result = 0
    resultIndex = 0
    for i in range(1, length - 1):
        k = i
        while i > 0 and k < length - 1 and s[i - 1] == s[k + 1]:
            i -= 1
            k += 1
        max = k - i + 1
        if max > result:
            resultIndex = i
        result = max if max > result else result
    print(s[resultIndex:resultIndex + result])


if __name__ == '__main__':
    longestPalindrome()

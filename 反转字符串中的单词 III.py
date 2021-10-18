def reverseWords(s):
    return " ".join(s[::-1].split(" ")[::-1])


s = "Let's take LeetCode contest"
print(reverseWords(s))

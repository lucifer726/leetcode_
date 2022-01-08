def largestRectangleArea(heights):
    n, heights, st, ans = len(heights), [0] + heights + [0], [], 0
    for i in range(n + 2):
        while st and heights[st[-1]] > heights[i]:
            ans = max(ans, heights[st.pop(-1)] * (i - st[-1] - 1))
        st.append(i)
    return ans



heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))

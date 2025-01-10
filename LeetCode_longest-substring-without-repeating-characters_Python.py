def longest_substring(s):
    ans = 0
    curr_string = s
    d = {}
    temp_ans = 0
    for i in range(len(curr_string)):
        if curr_string[i] not in d:
            d[curr_string[i]] = i
            temp_ans = temp_ans + 1
        else:
            index_to_remove_before = d[curr_string[i]]
            if temp_ans > ans:
                ans = temp_ans
            l = list(d.keys())
            for j in l:
                if d[j]<=index_to_remove_before:
                    d.pop(j)
            d[curr_string[i]] = i
            temp_ans = len(d)
    if temp_ans > ans:
        ans = temp_ans
    return ans

final_ans = longest_substring("aab")
print(final_ans)
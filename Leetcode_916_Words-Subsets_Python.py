from itertools import count


def word_subsets(words1, words2):
    ans = []
    all_letters_with_count = {}
    for i in words2:
        for j in i:
            try:
                if all_letters_with_count[j] < i.count(j):
                    all_letters_with_count[j] = i.count(j)
            except KeyError:
                all_letters_with_count[j] = 1

    for l in words1:
        flag = True
        for k in all_letters_with_count:
            if not all_letters_with_count[k]<=l.count(k):
                flag = False
                break
        if flag:
            ans.append(l)

    return ans

final_ans = word_subsets(["amazon","apple","facebook","google","leetcode"], ["lo","eo"])
print(final_ans)
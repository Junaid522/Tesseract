# https://leetcode.com/discuss/interview-question/algorithms/374846/twitter-oa-2019-university-career-fair


def universityCareerFair(arrival, duration):
    aux = sorted(
        list(zip(arrival, duration)),
        key=lambda p: (sum(p), p[1])
    )
    print(aux)
    ans, end = 0, -float('inf')
    print(ans, end)
    for arr, dur in aux:
        if arr >= end:
            ans, end = ans + 1, arr + dur
            print(ans, end)
        print(ans, end)
    return ans


# universityCareerFair([1, 3, 3, 5, 7], [2, 2, 1, 2, 1])

print(universityCareerFair([1, 3, 3, 5, 7], [2, 2, 1, 2, 1]))  # 4
# print(universityCareerFair([1, 2], [7, 3]))  # 1
# print(universityCareerFair([1, 3, 4, 6], [4, 3, 3, 2]))  # 2
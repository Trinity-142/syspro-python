def solution(a):
    ans = {}
    for value, key in a.items():
        if key in ans.keys():
            if type(ans[key]) == str:
                ans[key] = (ans[key], value)
            elif type(ans[key]) == tuple:
                ans[key] = (ans[key]) + (value,)
        else:
            ans[key] = value
    return ans

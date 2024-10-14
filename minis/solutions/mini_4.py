def solution(inpp):
    a = inpp.replace("\"", "").replace("'", "").replace(":", "").replace("}", "").replace("{", "").split(", ")
    a = {i.split()[0]: int(i.split()[1]) for i in a}

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

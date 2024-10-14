def solution(inp):
    strr = inp.replace("], ", "|").replace(", ", " ").replace("]", "").replace("[", "").replace("'", "").replace("\"", "").split("|")
    a = list(map(int, strr[0].split()))
    b = [i for i in strr[1].split()]
    return list((int(a[i]), b[i]) for i in range(min(len(a), len(b))))

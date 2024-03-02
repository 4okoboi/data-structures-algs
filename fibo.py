def fibo(stop: int) -> list:
    if stop == 0:
        return []
    res = [1, 1]
    for i in range(stop - 2):
        res.append(res[i] + res[i + 1])
    return res


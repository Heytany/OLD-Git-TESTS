def Kmt_method_test(X, Y):

    q = 0
    w = 0
    e = 0
    t = 0
    a = 0
    b = 0
    u = 0

    if len(X) != len(Y):
        print("Размеры листов должны быть одинаковыми")
        return [0, 0]
    else:

        N = len(Y)

        for i in range(0, N):
            q += N * X[i] * Y[i]
            w += X[i]
            e += Y[i]
        r = q - w * e

        for i in range(0, N):
            t = t + N * (X[i] ** 2)
            u = u + X[i]

        u = (u ** 2)

        for i in range(0, N):
            a = r / (t - u)
            b = 1 / N * (e - a * w)
    return [a, b]

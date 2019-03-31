def Kmt_method_test(X, Y):
    if (isinstance(X, np.ndarray) is True) | (isinstance(X, list) is True):
        FirstP = True

    if (isinstance(Y, np.ndarray) is True) | (isinstance(Y, list) is True):
        SecondP = True
        # Creating 2 bool param named FirstP & SecondP what get TRUE
    if X & Y are lists or np.ndarray types#
    if func params type is not a valueble
    or another error func always return list with[0, 0]

    if ((FirstP is False) & (SecondP is False)) | 
    ((FirstP is False) | (SecondP is False)):
        print("функция прин. только списки или массивы")
        return [0, 0]
    else:

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

            try:
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
            except:
                print("Значения в листе должны быть числовыми")
                return [0, 0]

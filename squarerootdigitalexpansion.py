import decimal
import math

D = decimal.Decimal


def squareroot(t, p):
    summation = 0
    with decimal.localcontext() as ctx:
        ctx.prec = p + 5
        for i in range(2, t+1):
            s = D(i)
            x = D(1)
            h = D(0.5)
            x1 = D(0)
            for m in range(500):
                x1 = h * (x + (s / x))
                x = x1
            rounded = round(x1, p)
            result = D(rounded).quantize(D('0.' + ('0' * (p - 1))), rounding=decimal.ROUND_HALF_UP)
            result = str(result % 1)
            if str(result).__contains__('E'):
                continue
            summation += sum(list(map(int, result[2:p+1])))
        return summation
    #     with decimal.localcontext() as ctx:
    #         if math.sqrt(i) % 1 == 0:
    #             continue
    #         ctx.prec = p + 5
    #         x = n.sqrt()
    #         rounded = round(x, p)
    #         result = D(rounded).quantize(D('0.'+('0' * (p - 1))), rounding=decimal.ROUND_HALF_UP)
    #
    #         result = str(result % 1)
    #         summation += sum(list(map(int, result[2:p+1])))
    # return summation

print(squareroot(int(input()), int(input())))
from Crypto.Util.number import inverse
import re
from pwn import *
from ecdsa import ellipticcurve


def inverse_mod(k, p):
    if k == 0:
        return 0

    if k < 0:
        return p - inverse_mod(-k, p)

    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = p, k

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    gcd, x, y = old_r, old_s, old_t

    assert gcd == 1
    assert (k * x) % p == 1

    return x % p


def is_on_curve(point, curve):
    if point is None:
        return True

    x, y = point

    return (y * y - x * x * x - curve.a() * x - curve.b()) % curve.p() == 0


def point_neg(point, curve):
    assert is_on_curve(point, curve)

    if point is None:
        # -0 = 0
        return None

    x, y = point
    result = (x, -y % curve.p())

    assert is_on_curve(result, curve)

    return result


def point_add(point1, point2, curve):
    if point1 is None:
        return point2
    if point2 is None:
        return point1

    x1, y1 = point1
    x2, y2 = point2

    if x1 == x2 and y1 != y2:
        return None

    if x1 == x2:
        m = (3 * x1 * x1 + curve.a()) * inverse_mod(2 * y1, curve.p())
    else:
        m = (y1 - y2) * inverse_mod(x1 - x2, curve.p())

    x3 = m * m - x1 - x2
    y3 = y1 + m * (x3 - x1)
    result = (x3 % curve.p(),
              -y3 % curve.p())

    return result


def scalar_mult(k, point, curve):
    assert is_on_curve(point, curve)

    if point is None:
        return None

    if point[1] == 0 and k % 2 == 0:
        return None

    if k < 0:
        return scalar_mult(-k, point_neg(point, curve), curve)

    result = None
    addend = point

    while k:
        if k & 1:
            result = point_add(result, addend, curve)
        addend = point_add(addend, addend, curve)

        k >>= 1

    return result


def extract_points_from_string(s):
    points = re.findall(r'\((\d+), (\d+)\)', s)
    return [[int(x), int(y)] for x, y in points]


def extract_scalars_and_points(s):
    scalars = re.findall(r'(\d+)\*([A-Z])', s)
    scalar_dict = {point: int(scalar) for scalar, point in scalars}

    return scalar_dict


def extract_curve_parameters(s):
    a_b_match = re.search(r'y\^2 = x\^3 \+ (\d+)\*x \+ (\d+)', s)
    p_match = re.search(r'Finite Field of size (\d+)', s)

    if a_b_match and p_match:
        a = int(a_b_match.group(1))
        b = int(a_b_match.group(2))
        p = int(p_match.group(1))
        return a, b, p
    else:
        return None, None, None


r = remote("ctf.mf.grsu.by", 9028)

for x in range(5):
    r.recvuntil(b"Elliptic Curve defined by Ep(a,b): ")
    data = r.recvline().strip().decode()
    print("elliptic curve =", data)
    a, b, p = extract_curve_parameters(data)
    print(a, b, p)
    curve = ellipticcurve.CurveFp(p, a, b)
    r.recvline()
    for _ in range(10):
        print("a, b, p =", a, b, p)
        infinity = False
        data = r.recvline().strip().decode()
        print("points =", data)
        points = extract_points_from_string(data)
        # P = Point(curve, points[0][0], points[0][1])
        # Q = Point(curve, points[1][0], points[1][1])
        data = r.recvline().strip().decode()
        print("scalar =", data)
        scalar = extract_scalars_and_points(data)
        if a == 1 and b == 0:
            mP = None
            for i in range(scalar["P"]):
                mP = point_add(mP, points[0], curve)
        else:
            mP = scalar_mult(scalar["P"], points[0], curve)
        print("mP =", mP)

        if a == 1 and b == 0:
            nQ = None
            for i in range(scalar["Q"]):
                nQ = point_add(nQ, points[1], curve)
        else:
            nQ = scalar_mult(scalar["Q"], points[1], curve)
        print("nQ =", nQ)
        sum_points = point_add(mP, nQ, curve)
        print("sum_points =", sum_points)
        if "R" in scalar:
            if a == 1 and b == 0:
                kR = None
                for i in range(scalar["R"]):
                    kR = point_add(kR, points[2], curve)
            else:
                kR = scalar_mult(scalar["R"], points[2], curve)
            print("kR =", kR)
            sum_points = point_add(sum_points, kR, curve)
        if sum_points:
            answer = str(sum_points[0]) + "," + str(sum_points[1])
        else:
            answer = "None"
        print("answer =", answer)
        r.sendline(answer.encode())
        print(r.recvline())
print(r.recvline())

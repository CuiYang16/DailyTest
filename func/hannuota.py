def move(n, a, b, c):
    """
    n为圆盘数，abc为柱子
    :param n:
    :param a:
    :param b:
    :param c:
    :return:
    """
    if n == 1:
        print(a, "->", c)
        return
    # a柱移到b柱(简化为n-1个圆盘)
    move(n - 1, a, c, b)
    # a柱移到c柱（移到最下面的圆盘）
    move(1, a, b, c)
    # b柱移到c柱(简化为n-1个圆盘)
    move(n - 1, b, a, c)


move(3, "A", "B", "C")

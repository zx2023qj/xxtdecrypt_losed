import json


def unsigned_right_shift(value, shift):
    # # 处理负数
    # if value < 0:
    #     value += 2 ** 32  # 将负数转换为无符号整数
    # return value >> shift
    # 保持值在 32 位范围内（无符号整数）
    value &= 0xFFFFFFFF
    # 右移指定位数
    return (value >> shift) & 0xFFFFFFFF


def to_signed_32_bit(value):
    """
    将输入值模拟为32位有符号整数
    """
    # 保留低32位
    value &= 0xFFFFFFFF  # 取低32位

    # 如果高位符号位为1，表示负数，需要转换为负数形式
    if value & 0x80000000:  # 检查最高位
        value -= 0x100000000  # 转换为负数
    return value


def func617e8c(var4eb3cd, var1e99e4):
    var5306aa = to_signed_32_bit(var4eb3cd & 0xffff) + to_signed_32_bit(var1e99e4 & 0xffff)
    var36a6b2 = ((to_signed_32_bit(var4eb3cd >> 0x10) + to_signed_32_bit(var1e99e4 >> 0x10)) + to_signed_32_bit(
        var5306aa >> 0x10))
    return to_signed_32_bit(to_signed_32_bit(var36a6b2 << 0x10) | to_signed_32_bit(var5306aa & 0xffff))
    # print(var4eb3cd + var1e99e4)
    # num = (var4eb3cd + var1e99e4) & 0xFFFFFFFF
    # num = to_signed_32_bit(var4eb3cd + var1e99e4)
    # if num >= 0x80000000:  # 0x80000000 是 32 位整数的负数起始点
    #     num -= 0x100000000  # 将其转换为负数
    # return num


def func204160(var474951, var51070f):
    # if var474951 < 0:
    #     var474951 = (1 << 32) + var474951
    # print((var474951 << var51070f) & 0xFFFFFFFF)
    var1 = to_signed_32_bit(var474951 << var51070f)
    return to_signed_32_bit(var1 | (unsigned_right_shift(var474951, 0x20 - var51070f)))


def func28fa76(var2fa589, var237a2f, var46d43a, var2ce627, var1c2624, var179943):
    # print(var2fa589, var237a2f, var46d43a, var2ce627, var1c2624, var179943)
    return func617e8c(
        func204160(func617e8c(func617e8c(var237a2f, var2fa589), func617e8c(var2ce627, var179943)), var1c2624),
        var46d43a)
    # return func204160(var237a2f+var2fa589+var2ce627+var179943, var1c2624)+var46d43a


def func75c801(var964d14, var413c52, var21d717, var41ec94, var2ddd4f, var4a3948, var1a75e3):
    var1 = to_signed_32_bit(var413c52 & var21d717)
    var2 = to_signed_32_bit(to_signed_32_bit(~var413c52) & var41ec94)
    var3 = to_signed_32_bit(var1 | var2)
    res = func28fa76(var3, var964d14, var413c52, var2ddd4f, var4a3948,
                     var1a75e3)
    # print(res)
    return res


def func2d67e7(var5edf2d, var41facf, var310561, var30e737, varc4bcdd, var3f344b, var4757ae):
    var1 = to_signed_32_bit(var41facf & var30e737)
    var2 = to_signed_32_bit(var310561 & to_signed_32_bit(~var30e737))
    var3 = to_signed_32_bit(var1 | var2)
    res = func28fa76(var3, var5edf2d, var41facf, varc4bcdd, var3f344b,
                     var4757ae)
    # print(res)
    return res


def funcf6e538(vareb2360, var59af59, var467ca5, var648572, var2b0633, var21de34, var8a713c):
    var1 = to_signed_32_bit(var59af59 ^ var467ca5)
    var2 = to_signed_32_bit(var1 ^ var648572)
    res = func28fa76(var2, vareb2360, var59af59, var2b0633, var21de34, var8a713c)
    # print(res)
    return res


def func2dbeaf(var566776, var1d70cf, var2f6c16, var112b18, var2d7de9, var3aa708, var16c8a3):
    var1 = to_signed_32_bit(var1d70cf | to_signed_32_bit(~var112b18))
    var2 = to_signed_32_bit(var2f6c16 ^ var1)
    res = func28fa76(var2, var566776, var1d70cf, var2d7de9, var3aa708, var16c8a3)
    # print(res)
    return res


def dftu_enc(d, f, t, u):
    salt = "NrRzLDpWB2JkeodIVAn4"
    ori = d + f + t + u + salt
    # ori = "%7B%22r%22%3A%228d128ee00fa7b354857c8652f6dedced%22%2C%22t%22%3A%22doc%22%2C%22l%22%3A1%2C%22f%22%3A4%2C%22p%22%3A1%2C%22tp%22%3A1%2C%22wc%22%3A131%2C%22ic%22%3A47%2C%22v%22%3A2%2C%22s%22%3A1%2C%22h%22%3A0%2C%22ext%22%3A%22%7B%5C%22_from_%5C%22%3A%5C%22245055799_104076320_254538083_e619568b77200ae4e7cc053e489355ba%5C%22%7D%22%7DreadPoint20241120161642300254538083NrRzLDpWB2JkeodIVAn4"
    # 创建一个足够大的数组，初始化为 0
    array1 = [0] * 1000  # 计算需要的数组长度
    # 计算 num
    num = len(ori) * 8

    # 遍历并填充 array1
    for i in range(0, num, 8):
        index = i >> 5  # i // 32
        char_code = ord(ori[i // 8]) & 0xff  # 获取字符的 Unicode 编码
        array1[index] |= (char_code << (i % 32))  # 位运算

    array1[num >> 5] |= 0x80 << (num % 0x20)

    array1[(unsigned_right_shift(num + 0x40, 9) << 4) + 0xe] = num
    # print(array1)

    var37b23e = 0x67452301
    var129cea = -0x10325477
    var52e7b2 = -0x67452302
    var27f070 = 0x10325476

    for i in range(0, 111, 0x10):
        var1aac91 = var129cea
        var23215c = var52e7b2
        var32bcb7 = var27f070
        var5d86d3 = var37b23e
        # print(i)
        # 56
        var37b23e = func75c801(var37b23e, var129cea, var52e7b2, var27f070, array1[i], 0x7, -0x28955b88)
        # 59
        var27f070 = func75c801(var27f070, var37b23e, var129cea, var52e7b2, array1[i + 0x1], 0xc, -0x173848aa)

        var52e7b2 = func75c801(var52e7b2, var27f070, var37b23e, var129cea, array1[i + 0x2], 0x11, 0x242070db)

        var129cea = func75c801(var129cea, var52e7b2, var27f070, var37b23e, array1[i + 0x3], 0x16, -0x3e423112)

        var37b23e = func75c801(var37b23e, var129cea, var52e7b2, var27f070, array1[i + 0x4], 0x7, -0xa83f051)

        var27f070 = func75c801(var27f070, var37b23e, var129cea, var52e7b2, array1[i + 0x5], 0xc, 0x4787c62a)

        var52e7b2 = func75c801(var52e7b2, var27f070, var37b23e, var129cea, array1[i + 0x6], 0x11, -0x57cfb9ed)

        var129cea = func75c801(var129cea, var52e7b2, var27f070, var37b23e, array1[i + 0x7], 0x16, -0x2b96aff)

        var37b23e = func75c801(var37b23e, var129cea, var52e7b2, var27f070, array1[i + 0x8], 0x7, 0x698098d8)

        var27f070 = func75c801(var27f070, var37b23e, var129cea, var52e7b2, array1[i + 0x9], 0xc, -0x74bb0851)

        var52e7b2 = func75c801(var52e7b2, var27f070, var37b23e, var129cea, array1[i + 0xa], 0x11, -0xa44f)

        var129cea = func75c801(var129cea, var52e7b2, var27f070, var37b23e, array1[i + 0xb], 0x16, -0x76a32842)

        var37b23e = func75c801(var37b23e, var129cea, var52e7b2, var27f070, array1[i + 0xc], 0x7, 0x6b901122)

        var27f070 = func75c801(var27f070, var37b23e, var129cea, var52e7b2, array1[i + 0xd], 0xc, -0x2678e6d)

        var52e7b2 = func75c801(var52e7b2, var27f070, var37b23e, var129cea, array1[i + 0xe], 0x11, -0x5986bc72)

        var129cea = func75c801(var129cea, var52e7b2, var27f070, var37b23e, array1[i + 0xf], 0x16, 0x49b40821)

        var37b23e = func2d67e7(var37b23e, var129cea, var52e7b2, var27f070, array1[i + 0x1], 0x5, -0x9e1da9e)

        var27f070 = func2d67e7(var27f070, var37b23e, var129cea, var52e7b2, array1[i + 0x6], 0x9, -0x3fbf4cc0)

        var52e7b2 = func2d67e7(var52e7b2, var27f070, var37b23e, var129cea, array1[i + 0xb], 0xe, 0x265e5a51)

        var129cea = func2d67e7(var129cea, var52e7b2, var27f070, var37b23e, array1[i], 0x14, -0x16493856)

        var37b23e = func2d67e7(var37b23e, var129cea, var52e7b2, var27f070, array1[i + 0x5], 0x5, -0x29d0efa3)

        var27f070 = func2d67e7(var27f070, var37b23e, var129cea, var52e7b2, array1[i + 0xa], 0x9, 0x2441453)

        var52e7b2 = func2d67e7(var52e7b2, var27f070, var37b23e, var129cea, array1[i + 0xf], 0xe, -0x275e197f)

        var129cea = func2d67e7(var129cea, var52e7b2, var27f070, var37b23e, array1[i + 0x4], 0x14, -0x182c0438)

        var37b23e = func2d67e7(var37b23e, var129cea, var52e7b2, var27f070, array1[i + 0x9], 0x5, 0x21e1cde6)

        var27f070 = func2d67e7(var27f070, var37b23e, var129cea, var52e7b2, array1[i + 0xe], 0x9, -0x3cc8f82a)

        var52e7b2 = func2d67e7(var52e7b2, var27f070, var37b23e, var129cea, array1[i + 0x3], 0xe, -0xb2af279)

        var129cea = func2d67e7(var129cea, var52e7b2, var27f070, var37b23e, array1[i + 0x8], 0x14, 0x455a14ed)

        var37b23e = func2d67e7(var37b23e, var129cea, var52e7b2, var27f070, array1[i + 0xd], 0x5, -0x561c16fb)

        var27f070 = func2d67e7(var27f070, var37b23e, var129cea, var52e7b2, array1[i + 0x2], 0x9, -0x3105c08)

        var52e7b2 = func2d67e7(var52e7b2, var27f070, var37b23e, var129cea, array1[i + 0x7], 0xe, 0x676f02d9)

        var129cea = func2d67e7(var129cea, var52e7b2, var27f070, var37b23e, array1[i + 0xc], 0x14, -0x72d5b376)

        var37b23e = funcf6e538(var37b23e, var129cea, var52e7b2, var27f070, array1[i + 0x5], 0x4, -0x5c6be)

        var27f070 = funcf6e538(var27f070, var37b23e, var129cea, var52e7b2, array1[i + 0x8], 0xb, -0x788e097f)

        var52e7b2 = funcf6e538(var52e7b2, var27f070, var37b23e, var129cea, array1[i + 0xb], 0x10, 0x6d9d6122)

        var129cea = funcf6e538(var129cea, var52e7b2, var27f070, var37b23e, array1[i + 0xe], 0x17, -0x21ac7f4)

        var37b23e = funcf6e538(var37b23e, var129cea, var52e7b2, var27f070, array1[i + 0x1], 0x4, -0x5b4115bc)

        var27f070 = funcf6e538(var27f070, var37b23e, var129cea, var52e7b2, array1[i + 0x4], 0xb, 0x4bdecfa9)

        var52e7b2 = funcf6e538(var52e7b2, var27f070, var37b23e, var129cea, array1[i + 0x7], 0x10, -0x944b4a0)

        var129cea = funcf6e538(var129cea, var52e7b2, var27f070, var37b23e, array1[i + 0xa], 0x17, -0x41404390)

        var37b23e = funcf6e538(var37b23e, var129cea, var52e7b2, var27f070, array1[i + 0xd], 0x4, 0x289b7ec6)

        var27f070 = funcf6e538(var27f070, var37b23e, var129cea, var52e7b2, array1[i], 0xb, -0x155ed806)

        var52e7b2 = funcf6e538(var52e7b2, var27f070, var37b23e, var129cea, array1[i + 0x3], 0x10, -0x2b10cf7b)

        var129cea = funcf6e538(var129cea, var52e7b2, var27f070, var37b23e, array1[i + 0x6], 0x17, 0x4881d05)

        var37b23e = funcf6e538(var37b23e, var129cea, var52e7b2, var27f070, array1[i + 0x9], 0x4, -0x262b2fc7)

        var27f070 = funcf6e538(var27f070, var37b23e, var129cea, var52e7b2, array1[i + 0xc], 0xb, -0x1924661b)

        var52e7b2 = funcf6e538(var52e7b2, var27f070, var37b23e, var129cea, array1[i + 0xf], 0x10, 0x1fa27cf8)

        var129cea = funcf6e538(var129cea, var52e7b2, var27f070, var37b23e, array1[i + 0x2], 0x17, -0x3b53a99b)

        var37b23e = func2dbeaf(var37b23e, var129cea, var52e7b2, var27f070, array1[i], 0x6, -0xbd6ddbc)

        var27f070 = func2dbeaf(var27f070, var37b23e, var129cea, var52e7b2, array1[i + 0x7], 0xa, 0x432aff97)

        var52e7b2 = func2dbeaf(var52e7b2, var27f070, var37b23e, var129cea, array1[i + 0xe], 0xf, -0x546bdc59)

        var129cea = func2dbeaf(var129cea, var52e7b2, var27f070, var37b23e, array1[i + 0x5], 0x15, -0x36c5fc7)

        var37b23e = func2dbeaf(var37b23e, var129cea, var52e7b2, var27f070, array1[i + 0xc], 0x6, 0x655b59c3)

        var27f070 = func2dbeaf(var27f070, var37b23e, var129cea, var52e7b2, array1[i + 0x3], 0xa, -0x70f3336e)

        var52e7b2 = func2dbeaf(var52e7b2, var27f070, var37b23e, var129cea, array1[i + 0xa], 0xf, -0x100b83)

        var129cea = func2dbeaf(var129cea, var52e7b2, var27f070, var37b23e, array1[i + 0x1], 0x15, -0x7a7ba22f)

        var37b23e = func2dbeaf(var37b23e, var129cea, var52e7b2, var27f070, array1[i + 0x8], 0x6, 0x6fa87e4f)

        var27f070 = func2dbeaf(var27f070, var37b23e, var129cea, var52e7b2, array1[i + 0xf], 0xa, -0x1d31920)

        var52e7b2 = func2dbeaf(var52e7b2, var27f070, var37b23e, var129cea, array1[i + 0x6], 0xf, -0x5cfebcec)

        var129cea = func2dbeaf(var129cea, var52e7b2, var27f070, var37b23e, array1[i + 0xd], 0x15, 0x4e0811a1)

        var37b23e = func2dbeaf(var37b23e, var129cea, var52e7b2, var27f070, array1[i + 0x4], 0x6, -0x8ac817e)

        var27f070 = func2dbeaf(var27f070, var37b23e, var129cea, var52e7b2, array1[i + 0xb], 0xa, -0x42c50dcb)

        var52e7b2 = func2dbeaf(var52e7b2, var27f070, var37b23e, var129cea, array1[i + 0x2], 0xf, 0x2ad7d2bb)

        var129cea = func2dbeaf(var129cea, var52e7b2, var27f070, var37b23e, array1[i + 0x9], 0x15, -0x14792c6f)

        var37b23e = func617e8c(var37b23e, var5d86d3)
        # print(var37b23e)

        var129cea = func617e8c(var129cea, var1aac91)
        # print(var129cea)

        var52e7b2 = func617e8c(var52e7b2, var23215c)
        # print(var52e7b2)

        var27f070 = func617e8c(var27f070, var32bcb7)
        # print(var27f070)
    # print(var37b23e, var129cea, var52e7b2, var27f070)
    array2 = [var37b23e, var129cea, var52e7b2, var27f070]
    length = len(array2) * 0x20
    # print(length)
    enc = ""
    for i in range(0, length, 0x8):
        # for i in range(1):
        var1 = to_signed_32_bit(i >> 0x5)
        var2 = unsigned_right_shift(array2[var1], i % 0x20)
        var3 = to_signed_32_bit(var2 & 0xff)
        # print(var3)
        enc += chr(var3)
    # print(enc)
    enc = enc.encode('utf-16-le').hex()
    enc = ''.join(enc[i:i + 2] for i in range(0, len(enc), 4))
    # print(enc)
    # print(len(enc))
    return enc

def ft_des(s: str) -> str:
    s = list(s)
    local_1c = 0
    for i in range(len(s)):
        shift = ord("0123456"[local_1c])
        if i % 2 == 0:
            for _ in range(shift):
                c = ord(s[i]) - 1
                if c == 0x1f:
                    c = ord('~')
                s[i] = chr(c)
        else:
            for _ in range(shift):
                c = ord(s[i]) + 1
                if c == 0x7f:
                    c = ord(' ')
                s[i] = chr(c)
        local_1c += 1
        if local_1c == 6:
            local_1c = 0
    return "".join(s)


if __name__ == "__main__":
    original = "boe]!ai0FB@.:|L6l@A?>qJ}I"
    token = ft_des(original)
    print("Token:", token)

import re

def base():
    # 有结果
    match = re.search(r"[1-9]\d{5}", "BIT 100081")
    if match:
        print(match.group(0))

    # 另一种等价模式
    pat = re.compile(r"[1-9]\d{5}")
    match = pat.search("BIT 100810")
    if match:
        print(match.group(0))

    # 无结果
    match = re.match(r"[1-9]\d{5}", "BIT 100081")
    if match:
        print(match.group(0))

    print("------------------")
    # 有结果
    match = re.match(r"[1-9]\d{5}", "100081 BIT ")
    if match:
        print(match.group(0))

    list = re.findall(r"[1-9]\d{5}", "100081 BIT TSU100085 ")
    print(list)

    list = re.split(r"[1-9]\d{5}", "100081 BIT TSU100085")
    print(list)

    list = re.split(r"[1-9]\d{5}", "100081 BIT TSU100085", maxsplit=1)
    print(list)

    for m in re.finditer(r"[1-9]\d{5}", "100081 BIT TSU100085"):
        if m:
            print(m.group(0))

    p = re.sub(r"[1-9]\d{5}", ":zipcode", "BIT10081 TSU 100082 100083")
    print(p)
    print(type(p))

if __name__ == "__main__":
    match = re.search(r"[1-9]\d{5}", "WHU100081 BIT TSU100085 ")
    print(match.string)
    print(match.start())
    print(match.group(0))
    print(match.pos)
    print(match.endpos)
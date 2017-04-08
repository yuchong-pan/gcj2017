import random

if __name__ == "__main__":
    with open("a.in", "w") as w:
        w.write("100\n")
        for _ in range(100):
            n = 1000
            s = ["+"] * n
            k = random.randint(1, n)
            t = random.randint(1, n)
            for i in range(t):
                p = random.randint(0, n - k)
                for j in range(k):
                    s[p + j] = "-" if s[p + j] == "+" else "+"
            w.write("%s %s\n" % ("".join(s), k))

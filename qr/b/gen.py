import random

if __name__ == "__main__":
    with open("b.in", "w") as w:
        w.write("100\n")
        for _ in range(100):
            w.write("%s\n" % random.randint(1, 10 ** 18))

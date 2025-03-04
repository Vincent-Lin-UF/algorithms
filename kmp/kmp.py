class KMP:
    def partial(self, pattern):
        # String -> [Int]
        ret = [0]

        for i in range(1, len(pattern)):
            j = ret[i-1]
            while j > 0 and patter[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j+1 if pattern[j] == pattern[i] else j)
        return ret

    def search(self, T, P):
        # String -> String -> [Int]
        partial, ret, j = self.partial(P), [], 0

        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]:
                j += 1
            if j == len(P):
                ret.append(i - (j-1))
                j = partial[j - 1]
        return ret


def test():
    p1 = "aa"
    t1 = "aaaaaaaa"

    kmp = KMP()
    a = kmp.search(t1,p1)
    print(a)
    print(len(t1))

    t2 = "aaaaaaaaaaaaaaaaaaaa"
    b = kmp.search(t2,p1)
    print(b)
    print(len(t2))

    t3 = "abdabeabtabctabc"
    p3 = "abc"
    assert(kmp.search(t3,p3) == [9,13])

if __name__ == "__main__":
    test()

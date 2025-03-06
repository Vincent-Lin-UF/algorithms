def monotonicStackIncrease(nums):
    stack = []
    res = []

    for num in nums:
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)

    while stack:
        res.insert(0,stack.pop())
    return res

def monotonicStackDecrease(nums):
    stack = []
    res = []

    for num in nums:
        while stack and stack[-1] < num:
            stack.pop()

        if stack:
            res.append(stack.pop())
        else:
            res.append(-1)

        stack.append(num)

    return res

if __name__ == "__main__":
    test1 = [3,1,4,1,5,9,2,6]
    incRes = monotonicStackIncrease(test1)
    decRes = monotonicStackDecrease(test1)
    print(f"Monotonic increasing stack:", incRes)
    print(f"Monotnic decreasing stack:", decRes)

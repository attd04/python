def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    string_n = str(n)

    iteration_count = 0
    happy_num = False
    while not happy_num:
        total = 0
        count = 0
        iteration_count += 1
        for num in string_n:
            count += 1
            print(f"count = {count}")
            num = int(num)
            print(f"num = {num}")
            total += (num*num)
            print(f"total = {total}")

            if total == 1:
                happy_num = True

            if iteration_count == 10:
                happy_num = True

            if count == len(string_n):
                string_n = str(total)
                print(f"new string n = {string_n}")

    if iteration_count == 10:
        return False
    else:
        return happy_num


isHappy(2)

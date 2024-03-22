def solution(s):
    tmp = ""
    ans = ""
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for a in s:
        tmp += a
        for index, elem in enumerate(num):
            str_index = str(index)
            if str_index in tmp:
                ans+=str_index
                tmp = ""
            elif elem in tmp:
                ans+=str_index
                tmp = ""
    return int(ans)


def solution2(s):
    ans = s
    dict_num = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    for key, value in dict_num.items():
        print(key, value)
        ans = ans.replace(key, value)
        print(ans)
    return(int(ans))

answer = solution2("2three45sixseven")
print(answer)
def solution(friends, gifts):
    give_score = [0] * len(friends)
    receive_score = [0] * len(friends)
    present_score = [0] * len(friends)
    next_month = [0] * len(friends)

    arr = [
        [0 for _ in range(len(friends))]
        for _ in range(len(friends))
    ]

    names_dict = {name: index for index, name in enumerate(friends)}

    for elem in gifts:
        a1, a2 = tuple(elem.split())
        arr[names_dict[a1]][names_dict[a2]] += 1

    for i in range(len(friends)):
        for j in range(len(friends)):
            give_score[i] += arr[i][j]
            receive_score[i] += arr[j][i]

    for i in range(len(friends)):
        present_score[i] = give_score[i] - receive_score[i]

    for i in range(len(friends)):
        for j in range(len(friends)):
            if i < j:
                if arr[i][j] != arr[j][i]:
                    if arr[i][j] > arr[j][i]:
                        next_month[i] += 1
                    else:
                        next_month[j] += 1
                elif arr[i][j] == arr[j][i]:
                    if present_score[i] > present_score[j]:
                        next_month[i] += 1
                    elif present_score[j] > present_score[i]:
                        next_month[j] += 1
                    else:
                        pass
    answer = max(next_month)
    return answer

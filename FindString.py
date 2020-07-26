def count_substring(string, sub_string):
    answer = 0
    tag = False

    len_str = len(string)
    len_sub = len(sub_string)

    for i in range(0, (len_str - len_sub + 1)):
        tag = True
        print("i reteration: {}".format(i))
        for j in range(0, len_sub):
            print("sub {}: {}, str {}: {}".format(j, sub_string[j], (i + j), string[i + j]))
            if (sub_string[j] != string[i + j]):
                tag = False
        
        if tag == True:
            answer += 1

    return answer


para1 = "ABCDCDC"
para2 = "CDC"

ans = count_substring(para1, para2)

print (ans)
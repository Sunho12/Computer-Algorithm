def postage_stamps(cost, stamps):
    stamps = sorted(stamps, reverse=True)
    count = 0
    for i in range(len(stamps)):
        while stamps[i] <= cost:
            cost -= stamps[i]
            count += 1
            postStamps[i] += 1
            if cost == 0:
                break
        if cost == 0:
            break
    print(stamps, end = " ")
    return count


cost = 140
postStamps = [0, 0, 0, 0, 0, 0, 0, 0, 0]
stamps = [1, 10, 21, 34, 70, 100, 350, 1225, 1500]
min_count = postage_stamps(cost, stamps)


print ("=", end = " ")
print ('(', end = " ")
for i in range(len(stamps)):
    if (i < 8):
        print (postStamps[i], end = ", ")
    else:
        print (postStamps [i], end = " ")
    

print (')')

print ("The number of stamps solved by the greed algorithm is " , min_count, ".")





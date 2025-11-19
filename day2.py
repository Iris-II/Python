

l  = [1, 2, 3, 4, 5]
ages = [10, 23, 40, 32]
ages1 = ages[0]
ages2 = ages[1]

ages.append(60)
print(ages)

ages.insert(1, 15)
print(ages)

ages.remove(60)
print(ages)

ages.pop()
print(ages)


late_age = ages.pop()
print(ages)
print(late_age)

#sort: 오름차순 정렬
ages.sort()
print(ages)

#튜플
s = (10, 20)
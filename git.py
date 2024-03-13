# 1 masala
# gap = input("Gap kiriting: ")
# substr = set()
# l = 0
# result = ""

# for i in range(len(gap)):
#     while gap[i] in substr:
#         substr.remove(gap[l])
#         l += 1
#     substr.add(gap[i])
#     gap1 = gap[l:i+1] 
#     if len(gap1) > len(result):
#         result = gap1

# if len(gap[l:i+1]) > len(result):
#     result = gap[l:i+1]

# print(result)


# 2 masala
# gap = input("Gap kiriting: ")

# yarmi = len(gap) // 2

# qism1 = gap[:yarmi + (len(gap) % 2)]
# qism2 = gap[yarmi + (len(gap) % 2):]

# gap2 = qism2 + qism1

# print(gap2)


# 3 masala
# fayl = open("gap.txt", "w")

# fayl.write(input("gap kiriting: "))
# fayl.close()

# fayl = open("gap.txt")

# for i in fayl.read().split():
#     soz = set(i)
#     a = list()
#     a.extend(i)
#     if len(soz) == len(a):
#         yarmi = len(i) // 2
#         qism1 = i[:yarmi + (len(i) % 2)]
#         qism2 = i[yarmi + (len(i) % 2):]
#         gap2 = qism2 + qism1
#         print(gap2)


# fayl.close()
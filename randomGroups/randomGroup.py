#write code to generate 40 numbers
#write code to take 5 random samples each from those 40 numbers OR
#randomize list, split into 8
#assign those 8 samples of 5 to groups 1-8

members_list = []

for n in range(40):
    members_list.append(n+1)
print(members_list)

members = random.sample(members_list, 40)

members_1 = members[0:5]
members_2 = members[5:10]
members_3 = members[10:15]
members_4 = members[15:20]
members_5 = members[20:25]
members_6 = members[25:30]
members_7 = members[30:35]
members_8 = members[35:40]
# for i in range(1, 9):
#     group = i
print('Group', 1, 'and their members', members_1)
print('Group', 2, 'and their members', members_2)
print('Group', 3, 'and their members', members_3)
print('Group', 4, 'and their members', members_4)
print('Group', 5, 'and their members', members_5)
print('Group', 6, 'and their members', members_6)
print('Group', 7, 'and their members', members_7)
print('Group', 8, 'and their members', members_8)

#version 1: this can still improve so I will upload the varations I come up with
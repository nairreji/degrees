# i=[]
# s="295297,304141,330373,373889,417741,420238,926084,1201607,1659337,1781796,1959490,2132285,2771200,3281548,3319920,4005402,4287320"
# x=s.split(',')
# x.sort()
# x = ["m" + a for a in x]
# i=i+x
# l="676297,786741,565673"
# m=l.split(',')
# m.sort()
# m = ["a" + a for a in m]
# i=i+m
# j=i[len(i)-1]
# j=j[1:]
# if "a676297" in i:
#     print("Yes")
# xdict= dict()
# xdict['102'] = {'name': 'Kevin Bacon', 'birth': '1958', 'movies': {'104257', '112384'}}
# y=xdict['102']["movies"]
# print(y)

l=['m112384', 'a193', 'a197', 'a129']
l.sort()
print(l)
if 'a193' in l:
    print("Yes")
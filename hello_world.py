x = "Its Thanksgiving day. Its my birthday, too!"
print x.replace ("month", "day" )

seta = set([2,54,-2,7,12,98])
print(max(seta))
print(min(seta))

x = ["hello",2,54,-2,7,12,98,"world"]
print("%s %s"%(x[0], x[-1]))

x = [19,2,54,-2,7,12,98,32,10,-3,6]
print sorted (x)
print x

x = [-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
x[0] = [x[0]]
for num in range( 1, (len(x)/2) ):
    x[0].append(x.pop(1))
    print x

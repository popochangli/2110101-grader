n = int(input())
l = []
fema = {}
sema= {}
for i in range(n):
    d = input().split(',')
    for x in d:
        l.append(float(x))
fema[6]=(1/7)*(sum(l[:7]))
sema[13]=(1/14)*(sum(l[:14]))
for i in range(7,len(l)):
    fema[i]=(2/8)*l[i]+(6/8)*(fema[i-1])
for i in range(14,len(l)):
    sema[i]=(2/15)*l[i]+(13/15)*(sema[i-1])
tf = []
for i in range(13,len(l)):
    if fema[i]<=sema[i]: tf.append(0)
    else: tf.append(1)
printed = 0
for i in range(1,len(tf)):
    if tf[i]==1 and tf[i-1]==0:
        printed = 1
        print('BUY at','%.2f' % float(l[i+13]))
    elif tf[i]==0 and tf[i-1]==1:
        printed = 1
        print('SELL at','%.2f' % float(l[i+13]))
if not printed: print('No results')
'''
8
9.13,9.08,9.29,9.25,9.45,9.24,9.23
9.22,9.29,9.24,9.25,9.21,9.14,9.16
9.17,9.2,9.17,9.38,9.51,9.59,9.54
9.71,9.93,11.22,10.96,11.25,11.18,11.31
11.77,11.13,11.21,11.24,11.64,11.78,11.59
11.75,11.69,11.82,11.35,11.55,11.74,11.79
11.88,11.93,12.38,12.06,11.75,11.83,11.55
11.67,11.65,11.76,11.37,11.46,11.29,11.47

4
6.59,7.34,7.15,7.18,7.14,7.41,7.29
7.24,7.21,7.19,7.24,7.32,7.39,7.27
7.2,7.19,6.97,7.29,7.35,7.35,7.72
8.06,8.07,7.8,8.08,8.07,8.16,8.12

1
34.99,31.04,32.85,32.05,32.15,32.35,32.84
'''
import support

x=support.read_file_int_array('day1.txt')
count=0
last=x[0]
for i in range(1, len(x)):
    if x[i]>last:
        count+=1
    last=x[i]

print(f'part 1 {count=}')

count=0
win_r=4
while win_r<len(x)+1:
    if sum(x[win_r-3:win_r])>sum(x[win_r-4:win_r-1]):
        count+=1
    win_r+=1

print(f'part 2 {count=}')
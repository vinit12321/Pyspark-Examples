'''
Writing code for taking set & perform different commands.
'''
n=int(input())
s=set(map(int,input().split()))
num_of_cmds=int(input())
for _ in range(num_of_cmds):
    cmd=input().split()
    if(cmd[0]=='pop'):
        s.pop()
    elif(cmd[0]=='remove'):
        s.remove(int(cmd[1]))
    elif (cmd[0]=='discard'):
        s.discard(int(cmd[1]))

print(sum(s))

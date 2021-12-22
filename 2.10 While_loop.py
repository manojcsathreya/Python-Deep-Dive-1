#while loop
'''
Syntax:
    
while <condition>:
    body
    
'''

#we do not have do-while loop. We can use the alternate instead
i=5
while True:
    print(i)
    if i==5:
        break
#op: 5

#continue : Skips the statements below continue and returns back to starting of loop

i=0
while i<10:
    i+=1
    if(i%2==0):
        continue
    print(i)
    
#op: 1,3,5,7,9

#while else: executes iff there is no break statement inside the loop
l=[1,2,3]
found= False
val =10
idx=0
while (idx<len(l)):
    if(l[idx]==val):
        found=True
        break
    idx+=1
if not found:
    l.append(val)

print(l)

#while else way of doing this
l=[1,10,2,3]
val =10
idx=0
while idx<len(l):
    if l[idx]==val:
        break
    idx+=1
else:
    l.append(val)
    
print(l)
#op: [1,10,2,3]


#finally always executes inside while loop

a=0
b=2
while a<4:
    print('---------------')
    a+=1
    b-=1
    try:
        a/b
    except ZeroDivisionError:
        print('{0}, {1} - disvision by zero'.format(a,b))
    finally:
         print('{0}, {1} - always executes'.format(a,b))
    
    print('{0}, {1} - inside loop'.format(a,b))
    
  '''
  ---------------
1, 1 - always executes
1, 1 - inside loop
---------------
2, 0 - disvision by zero
2, 0 - always executes
2, 0 - inside loop
---------------
3, -1 - always executes
3, -1 - inside loop
---------------
4, -2 - always executes
4, -2 - inside loop
  '''

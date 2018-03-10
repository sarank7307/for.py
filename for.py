words=['boom','booom','boomer']
print(words.append('wrigleys'))
print(words.insert(2,'NO.1'))
print(words)

for w  in words :
    if len(w)<5 :
        print(w,end=' ')

print('\n')

for i in range(-10,-20,-2) :
    print(i,end=' ')

print('\n')

for i in range(len(words)) :
    print(i,words[i],end='   ')

print('\n')

print(range(10))

print(list(range(10)))

for n in range(2,50) :
    for d in range(2,n) :
        if n%d==0 :
            #print('n =',d,'*',n//d)
            break;

    else:
        print(n,'is prime')


for i in range(10) :
    if i%2==0 :
        pass
        print(i,'is even')
        continue
    print(i,'is odd')

file = open ('text_parsed.txt', 'r', encoding='utf-8')
result = open('gold.txt', 'w', encoding='utf-8')
text = file.readlines()
count = 0 
for t in text:
    arr = t.split()
    word = arr[0]
    lemma = arr[2]
    gram = arr[1]
    pos = gram[0]
    form = gram[1:]
    if word != '.':
        print(word)
        count+=1
    elif word != ',':
        print(word)
        count+=1
    elif word != '?':
        print(word)
        count+=1
    elif word != '...':
        print(word)
        count+=1
    elif word != '!':
        print(word)
        count+=1
    elif word != '—':
        print(word)
        count+=1
    elif word != ':':
        print(word)
        count+=1
    elif word != ')':
        print(word)
        count+=1
    elif word != '(':
        print(word)
        count+=1
print(count)        
   
file.close()
result.close()

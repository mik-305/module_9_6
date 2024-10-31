def all_variants(text):
    razm = 0
    for razm in range(len(text)):
        for j in range(len(text)-razm):
            yield text[j:j+razm+1]

a = all_variants('abc')
for i in a:
    print(i)
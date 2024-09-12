def all_variants(str):
    for i in range(len(str)):
        for j in range(i + 1, len(str) + 1):
            yield str[i:j]



a = all_variants("abc")
for i in a:
    print(i)
a=['а','у','е','о','э','ю','и','ы','я']

def vowel(a,b):
    caunt=0
    for i in a:
        if i in b:
            caunt+=1
    print(caunt)
vowel(a,'привет')

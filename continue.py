flag= True
i=0
while flag is True:
    i=i+1
    print(i)
    try:
        if i ==10:
            continue
            
            i="sds"
    except Exception as e:
        print(e)

    i=i+2

    if i >=20:
        break



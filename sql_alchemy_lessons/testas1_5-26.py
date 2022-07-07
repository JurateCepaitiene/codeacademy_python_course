# Sukurti funkciją, kuri patikrintų, ar paduotas Lietuvos piliečio asmens kodas yra validus.
# Padaryti, kad programa sugeneruotų teisingą asmens kodą (panaudojus anksčiau sukurtą funkciją) pagal įvestą lytį, 
# gimimo datą ir eilės numerį).

def check_id(id:str) -> bool:
    
    if len(id)!=11:
        return False

    for i in id:
        try:
            int(i)
        except Exception as e:
            return False
    
    x = int(id[0])

    if x > 6 or x < 1:
        return False

        # arba if int(code[0]) < 1 or int(code[0]) > 6:

        # return False

    from datetime import datetime
    # date1 = id[1:7]
    # print(date1)

    month = id[3:4]
    day = id[5:6]

    if month >



    return True

print(check_id('18274562522'))



# veikia !!



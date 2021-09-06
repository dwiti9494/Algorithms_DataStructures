# Looping through Python dicts

dict_1 = {
            ( "Jack", "010-023456"),
            ( "Pete", "010-7487587"),
            ( "Zack", "010-4356745")
        }
for name, phonenr in dict_1:
    print(name, ":", phonenr)

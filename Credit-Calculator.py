import argparse , sys , math

def Overpayment(a, b ,c):
    overp = math.ceil((a * b) -c)
    print("Overpayment = {0}".format(int(overp)))
    
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.add_argument("--type")
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

list1 = [args.type, args.payment, args.principal, args.periods, args.interest]
if len(list1) < 4:
    print("Incorrect parameters")
    
if args.type == "diff" and args.type =="payment":
    print("Incorrect parameters")
elif args.payment and args.payment < 0 or args.principal and args.principal < 0 or args.periods and args.periods < 0 or args.interest and args.interest < 0:
    print("Incorrect parameters")
    
if args.type == "diff":
    if args.principal and args.periods and args.interest:
        cost = 0
        i = args.interest / (12 * 100)
        for m in range(1 , args.periods + 1):
            dm = math.ceil(args.principal / args.periods + i * (args.principal - args.principal * (m - 1) / args.periods))
            dm = math.ceil(dm)
            cost += dm
            print("Month {0} : paid out {1}".format(m,int(dm)))
        
        overpayment = cost - args.principal
        print("\nOverpayment = {0}".format(int(overpayment)))
    else:
        print("Incorrect parameters")
    
elif args.type == "annuity":
    if args.payment and args.periods and args.interest:
        i = args.interest / (12 * 100)
        p = args.payment / ((i * (pow(i+1,args.periods))) / (pow(i+1,args.periods) - 1))
        p = int(p)
        print("Your credit principal = {0}!".format(p))
        Overpayment(args.periods , args.payment , p)
        
    elif args.principal and args.periods and args.interest:
        i = args.interest / (12 * 100)
        a = args.principal * (i * pow(i+1,args.periods) / ((pow(i+1,args.periods) - 1)))
        a = math.ceil(a)
        print("Your annuity payment = {0}!".format(int(a)))
        Overpayment(args.periods , a , args.principal)
        
    elif args.principal and args.payment and args.interest:
        i = args.interest / (12 * 100)
        n = math.log((args.payment / (args.payment - i * args.principal)),i+1)
        n = math.ceil(n)
        year = n//12
        month = n % 12
        if month == 0:
            print("You need {0} years to repay the credit!".format(int(year)))
        elif year == 0:
            print("You need {0} month to repay the credit!".format(int(month)))
        else:
            print("You need {0} years and {1} months to repay this credit!".format(int(year),int(month)))
            
        Overpayment( n + month , args.payment , args.principal )
    else:
        print("Incorrect parameters")
        
else:
    print("Incorrect parameters")
        
    
    
        
    
    

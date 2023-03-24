#list and data QAP 4
#By: Brokelynn upshall
# date: 2023/03/24

# One Stop Insurance Company
#import
import datetime

# Constants.
f = open('OSICDef.dat', 'r')
INVOICE_NUM = int(f.readline().strip())
PREM_RATE = float(f.readline().strip())
ADDCAR_DISC = float(f.readline().strip())
LIABILITY_RATE = float(f.readline().strip())
GLASS_RATE = float(f.readline().strip())
LOANERCAR_RATE = float(f.readline().strip())
HST_RATE = float(f.readline().strip())
PROCESS_FEE = float(f.readline().strip())
f.close()

# Display the Policy Number at beginning of program.
print()
print(f"Policy #: {INVOICE_NUM}")
print()

while True:

    # User inputs.
    CustFirstName = input("Enter the customer's first name:                 ").title()
    CustLastName = input("Enter the customer's last name:                   ").title()

    print()

    CustStAdd = input("Enter the customer's Street Address:              ").title()
    CustCity = input("Enter the customer's city:                       ").title()

    # Validate the province with a list.
    ProvList = ["NL", "NS", "PE", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "NV", "NT"]
    while True:
        Prov = input("Enter the customer's province(LL):               ").upper()

        if not Prov in ProvList:
            print("Invalid province, please reenter.")
        else:
            break

    PostCode = input("Enter the customer's postal code:                ").upper()
    print()

    while True:
        CustPhNum = input("Enter the customer's phone number(9999999999):         ")
        if CustPhNum == "":
            print("Cannot be left blank please reenter.")
        elif len(CustPhNum) != 10:
            print("Phone number must be 10 digits long, please reenter.")
        elif not CustPhNum.isdigit():
            print("Phone number must be digits(0-9) only, please reenter.")
        else:
            CustPhNum = "(" + CustPhNum[0:3] + ")" + CustPhNum[3:6] + "-" + CustPhNum[6:10]
            break

    print()

    # Number of cars insured with calculation.
    while True:
        NumOfCar = int(input("Enter the number of cars to be insured:             "))
        if NumOfCar == 1:
            CarTotal = PREM_RATE
            break
        else:
            CarTotal = (NumOfCar - 1) * (PREM_RATE * ADDCAR_DISC) + PREM_RATE
            break

    print()

    # Extra cost coverages.
    while True:
        Liability = input("Enter Y/N for extra liability coverage up to $1,000,000: ").upper()
        if Liability== "Y":
            Liability = LIABILITY_RATE
            break
        else:
            Liability = 0
            break

    while True:
        Glass = input("Enter Y/N for glass coverage:                       ").upper()
        if Glass == "Y":
            Glass = GLASS_RATE
            break
        else:
            Glass = 0
            break

    while True:
        LoanerCar = input("Enter Y/N for the loaner car option:                ").upper()
        if LoanerCar == "Y":
            LoanerCar = LOANERCAR_RATE
            break
        else:
            LoanerCar = 0
            break

    print()

    # Calculations
    ExtraCosts = LoanerCar + Glass + Liability
    TotInsPrem = CarTotal + ExtraCosts
    HST = TotInsPrem * HST_RATE
    TotCost = TotInsPrem + HST

    # Invoice date.
    InvDate = datetime.datetime.now()
    InvDateDsp = InvDate.strftime("%Y-%m-%d")

    # Next payment due on the first day of the next month.
    Payment = InvDate + datetime.timedelta(days=32)
    Payment = Payment.replace(day=1)
    PaymentDsp = Payment.strftime("%B %d, %Y")

    # Full or monthly payments.
    while True:
        Pay = input("Enter F or M to pay in Full or Monthly payments:      ").upper()
        if Pay == "F":
            Status = "Pay in Full:"
            Pay = TotCost
            break
        elif Pay == "M":
            Pay = (TotCost + PROCESS_FEE) / 8
            Status = "Monthly Payments/Month:"
            break
        else:
            break

    # receipt.
    print()
    print("                         One Stop")
    print("                    Insurance Company")
    print("---------------------------------------------------------")
    print(f"Policy #: {INVOICE_NUM:<4d}                   Invoice Date: {InvDateDsp:>10s}")
    print("---------------------------------------------------------")
    print("Customer:                             Customer Phone:")
    print()
    print(f"    {CustFirstName:<10s} {CustLastName:<10s}             {CustPhNum:>10s}")
    print(f"    {CustStAdd:<15s}")
    print(f"    {CustCity:<15s}, {Prov:2s} {PostCode}")
    print("---------------------------------------------------------")
    print(f"Number of cars to be insured:                          {NumOfCar:>2d}")
    print("---------                                       ---------")
    CarTotDsp = "${:,.2f}".format(CarTotal)
    print(f"Insurance Premium:                              {CarTotDsp:>9s}")
    print("---------                                       ---------")
    LiabilityDsp = "${:,.2f}".format(Liability)
    print(f"Extra Liability(Up to $1,000,000):              {LiabilityDsp:>9s}")
    GlassDsp = "${:,.2f}".format(Glass)
    print(f"Glass Coverage:                                 {GlassDsp:>9s}")
    LoanerCarDsp = "${:,.2f}".format(LoanerCar)
    print(f"Loaner Vehicle:                                 {LoanerCarDsp:>9s}")
    print("---------                                       ---------")
    ExtraCostsDsp = "${:,.2f}".format(ExtraCosts)
    print(f"Extra Costs Total:                              {ExtraCostsDsp:>9s}")
    print("---------                                       ---------")
    TotInsPremDsp = "${:,.2f}".format(TotInsPrem)
    print(f"Sub Total:                                      {TotInsPremDsp:>9s}")
    HSTDsp = "${:,.2f}".format(HST)
    print(f"HST:                                            {HSTDsp:>9s}")
    print("---------                                       ---------")
    TotCostDsp = "${:,.2f}".format(TotCost)
    print(f"Total:                                          {TotCostDsp:>9s}")
    print("---------------------------------------------------------")
    PayDsp = "${:,.2f}".format(Pay)
    print(f"{Status} {PayDsp:>9s}")
    print(f"Payment Due: {Payment.date()}")
    print("---------------------------------------------------------")

    # Save the data for the claim to a data file.
    f = open("Policies.dat", "a")
    f.write("{}, ".format(str(INVOICE_NUM)))
    f.write("{}, ".format(InvDateDsp))
    f.write("{}, ".format(CustFirstName))
    f.write("{}, ".format(CustLastName))
    f.write("{}, ".format(CustStAdd))
    f.write("{}, ".format(CustCity))
    f.write("{}, ".format(Prov))
    f.write("{}, ".format(PostCode))
    f.write("{}, ".format(str(NumOfCar)))
    f.write("{}, ".format(str(Liability)))
    f.write("{}, ".format(str(Glass)))
    f.write("{}, ".format(str(LoanerCar)))
    f.write("{}, ".format(Prov))
    f.write("{}\n ".format(str(TotCost)))
    f.close()

    print()
    print("Policy information processed and saved.")

    # Policy Number counter.


    f = open('OSICDef.dat', 'w')
    f.write("{}\n".format(str(INVOICE_NUM)))
    f.write("{}\n".format(str(PREM_RATE)))
    f.write("{}\n".format(str(ADDCAR_DISC)))
    f.write("{}\n".format(str(LIABILITY_RATE)))
    f.write("{}\n".format(str(GLASS_RATE)))
    f.write("{}\n".format(str(LOANERCAR_RATE)))
    f.write("{}\n".format(str(HST_RATE)))
    f.write("{}\n".format(str(PROCESS_FEE)))
    f.close()

    More = input("Do you want to enter another insurance policy? (Y/N): ").upper()
    if More != "Y":
        INVOICE_NUM += 1
        exit()

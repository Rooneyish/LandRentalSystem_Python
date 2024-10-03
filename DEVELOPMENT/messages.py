'''
displaying required information 
when the user rents and returns
'''
def display_rented_details(details):
    total_amount = 0
    print("Name: ",details[0][0],"\n")
    print("========================================\n")
    for each in details:
        print("Kitta Number: ",each[1])
        print("Location: ",each[2])
        print("Land Face: ",each[3])
        print("Anna: ",each[4])
        print("Price: ",each[5])
        print("Months: ",each[6])
        print("Date: ",each[7])
        print("Total amount: ",each[8])
        print("----------------------------------------\n")
        total_amount += int(each[8])
    print("Overall Total Amount: ",str(total_amount),"\n")


def display_return_details(details):
    total_amount=0
    print("Name: ",details[0][0],"\n")
    print("========================================\n")
    for each in details:
        print("Name:",each[0])
        print("Kitta Number:", each[1])
        print("Location:", each[2])
        print("Land Face:", each[3])
        print("Anna:", each[4])
        print("Months:", each[5])
        print("Date:", each[6])
        print("Total amount:",each[7])
        print("----------------------------------------\n")
        total_amount += float(each[7])
    print("Overall Total Amount: ",str(total_amount),"\n")
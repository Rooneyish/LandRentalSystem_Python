# importing requried files
import operation

# function that generates bill when the land is rented
def generate_invoice(details):
    total_amount = 0
    fileName = "Rent_" + details[0][0] + "_" + operation.function_date_time() + ".txt"
    file=open(fileName, "w")
    file.write("Name: "+details[0][0]+"\n")
    file.write("========================================\n")
    for each in details:
        file.write("Kitta Number: "+each[1]+"\n")
        file.write("Location: "+each[2]+"\n")
        file.write("Land Face: "+each[3]+"\n")
        file.write("Anna: "+each[4]+"\n")
        file.write("Price: "+each[5]+"\n")
        file.write("Months: "+each[6]+"\n")
        file.write("Date: "+each[7]+"\n")
        file.write("Total amount: "+each[8]+"\n")
        file.write("----------------------------------------\n")
        total_amount += int(each[8])
    file.write("Overall Total Amount: "+str(total_amount)+"\n")

# function that generates bill when the land is returned
def generateInvoiceReturn(details):
    total_amount=0
    fileName="Return_"+details[0][0]+"_"+operation.function_date_time()+".txt"
    file=open(fileName,"w")
    file.write("Name: "+details[0][0]+"\n")
    file.write("========================================\n")
    for each in details:
        file.write("Name:"+each[0]+"\n")
        file.write("Kitta Number:"+ each[1]+"\n")
        file.write("Location:"+ each[2]+"\n")
        file.write("Land Face:"+ each[3]+"\n")
        file.write("Anna:"+ each[4]+"\n")
        file.write("Months:"+ each[5]+"\n")
        file.write("Date:"+ each[6]+"\n")
        file.write("Total amount:"+each[7]+"\n")
        file.write("----------------------------------------\n")
        total_amount += float(each[7])
    file.write("Overall Total Amount: "+str(total_amount)+"\n")

# function that writes the details of the land that is being rented
def writing_to_files(details):
    file=open("rentedLand.txt","a")
    for each in details:
        file.write(','.join(each)+"\n")
    file.close()

# function that updates the status of the land after being rented or returned
def update(dataList):
    file=open("landData.txt","w")
    for line in dataList:
        file.write(','.join(line)+"\n")
    file.close()
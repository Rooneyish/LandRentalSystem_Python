# importing required files
import datetime
import messages
import write

'''
main function when the user wants to rent the land
'''
def rent(dataList):
    rentedLands=[]
    name=input("Please enter your name: ") # asking user's name
    while True:
        kitta=input("Enter 'Kitta' number of the land you want to rent or type 'done' to finish: ") # asking kitta number of the land the user wants to rent
        if kitta.lower()=='done':
            break
        for i in range(len(dataList)):
            if dataList[i][0]==kitta:
                if dataList[i][5].lower()=="available":
                    print('Land is Available!!')
                    months=0
                    try:
                        months=int(input("Number of months you want to rent for: "))
                    except:
                        print("Enter the months in number")
                    if months==0:
                        break
                    price=str(dataList[i][4])
                    location=str(dataList[i][1])
                    landface=str(dataList[i][2])
                    anna=str(dataList[i][3])
                    totalAmount=transaction(price,months)
                    rentedLands.append([name,kitta,location, landface, anna,price,str(months),str(datetime.datetime.now()),str(totalAmount)])
                    dataList[i][5]="NotAvailable"
                    updateLine=dataList
                    updateline(updateLine,dataList)
                    messages.display_rented_details(rentedLands)
                    write.generate_invoice(rentedLands)
                    break
                else:
                    print('Land is Not Available.\n Please enter a land that is available')
                    break
            
        else:
            print("There is no land in the data with 'kitta' number", kitta)
    return rentedLands

# function that calculates the total amount
def transaction(price,months):
    totalAmount=int(months)*int(price)
    print("The total amount for",months,"months: ",totalAmount,"\n")
    return totalAmount

# function that updates line
def updateline(updatedLine,dataList):
    for i in range(len(dataList)):
        if updatedLine[0]==dataList[i][0]:
            dataList[i]=updatedLine
            break

# function that generates unique number
def function_date_time():
    minute=str(datetime.datetime.now().minute)
    second=str(datetime.datetime.now().second)
    microsecond=str(datetime.datetime.now().microsecond)
    random=minute+second+microsecond
    rand=str(random)
    return rand

'''
main function when the user wants to return the land
'''
def Return(dataList, rentedList):
    returnedLands=[]
    name = input("Please enter your name: ")
    while True:
        kitta = input("Enter the 'Kitta' number of the land that you want to return or type 'done' to finish: ")
        if kitta.lower() == 'done':
            break
        found = False
        for i in range(len(rentedList)):
            if rentedList[i][0] == name and rentedList[i][1] == kitta:
                for j in range(len(dataList)):
                    if dataList[j][0] == kitta:
                        if dataList[j][5].lower() == "notavailable":
                            print("The land can be returned")
                            months = int(rentedList[i][6])
                            price = int(rentedList[i][5])
                            location=str(dataList[j][1])
                            landface=str(dataList[j][2])
                            anna=str(dataList[j][3])
                            total_amount = transaction(price, months)
                            returnMonth=0
                            try:
                                returnMonth=int(input("Enter the number of months you rented the land: "))
                            except:
                                print("Enter the months in number")
                            if returnMonth==0:
                                break
                            if returnMonth > months:
                                fine= Fine(total_amount)
                                total_amount+=fine
                                print("You have rented land for more than",months,"months. Therefore, your total amount after fine is",total_amount)
                            rentedList.pop(i)
                            returnedLands.append([name,kitta,location,landface,anna,str(returnMonth),str(datetime.datetime.now()),str(total_amount)])
                            dataList[j][5] = "Available"
                            updatedLine=dataList
                            updateline(updatedLine,dataList)
                            write.generateInvoiceReturn(returnedLands)
                            messages.display_return_details(returnedLands)
                            found = True
                            break
                if found==False:
                    print("The land cannot be returned as it was not rented by", name)
                break
        else:
            print("The land cannot be returned as it was not rented by", name)
    file=open("rentedLand.txt","w")
    for each in rentedList:
        file.write(",".join(each)+"\n")
    write.update(dataList)
    return returnedLands

# functions that calculates fine
def Fine(total_amount):
    finePercent=0.10
    return total_amount*finePercent

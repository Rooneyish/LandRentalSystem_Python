# function that collects data from the "landData.txt" file
def collection():
    file=open("landData.txt","r")
    dataList=[]
    for eachLine in file:
        eachLine=eachLine.replace("\n","")
        eachLine=eachLine.replace(" ","")
        eachLine=eachLine.split(",")
        dataList.append(eachLine)
    file.close()
    return dataList

# function that collects and displays the details of the land
def display():
    print("Kitta------Location-----LandFace------Anna------Price/Month------Status")
    file=open("landData.txt","r")
    for eachLine in file:
        print(eachLine.replace(",","-----"))
    file.close()

# function that collects rented land data from "rentedLand.txt" file
def collectionRented():
    file=open("rentedLand.txt","r")
    rentedList=[]
    for eachLine in file:
        eachLine=eachLine.replace("\n","")
        eachLine=eachLine.replace(" ","")
        eachLine=eachLine.split(",")
        rentedList.append(eachLine)
    file.close()
    return rentedList
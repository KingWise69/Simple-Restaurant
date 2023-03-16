print("")
import datetime
print("-----------------------------------------------------")

print( "CRIMSON  RESTAURANT " ,"         ""RECEIPT",sep='\n')

print("-----------------------------------------------------")

print("Date & Time :", datetime.datetime.now())

print("-----------------------------------------------------")

print (" ")
print("WELCOME TO CRIMSON RESTAURANT")

Food = "Juice", "Water", "Rice", "Meat", "Matooke","Kakomando"
prices = 3000,1500,5000,6500,4500,2500

Foods = ["ORDER OPTIONS:","1.Juice", "2.Water", "3.Rice ", "4.Meat", "5.Matooke","6.Kakomando"]
for y in Foods:print (y)

Items = ["PRICES FOR FOODS:","1.Juice - shs.3,000", "2.Water - shs.1,500" , "3.Rice - shs5,000" , "4.Meat - shs.6,500" , "5.Matooke - shs.4,500","6.Kakomando - shs.2,500"]
for p in Items:print(p)



myorderFood=[]
myorderCost=[]




order = input("May We Take Your Order? Yes or No :")

if order=="No":
 exit("Thank You And Come Again")
else:
     print("Welcome!!!")
nextorder = True
while nextorder==True:
  foodOrder = input("Please enter item : ")
  if foodOrder =="Juice":
    myorderFood.append(Food[0])
    myorderCost.append(prices[0])
  elif foodOrder=="Water":
    myorderFood.append(Food[1])
    myorderCost.append(prices[1])
  elif foodOrder=="Rice":
    myorderFood.append(Food[2])
    myorderCost.append(prices[2])
  elif foodOrder=="Meat":
    myorderFood.append(Food[3])
    myorderCost.append(prices[3])
  elif foodOrder=="Matooke":
    myorderFood.append(Food[4])
    myorderCost.append(prices[4])
  elif foodOrder=="Kakomando":
    myorderFood.append(Food[5])
    myorderCost.append(prices[5])
  else:
    print("NOT ON THE LIST")
  finished = input("Are You Done Ordering Yes/No :")
  if finished== "No":
    nextorder=True
  else:
    nextorder=False 
  print(myorderFood)
  print(myorderCost)
    
    
    
            


name = input("Customer name Mr/Ms/Mrs: "" " )
print (" ")







class Payment:
    def __init__(self, cashier_name):
        self.cashier_name = cashier_name

    def Payment(self):
        print("Cashier :""", self.cashier_name)


pay1 = Payment('King Wise')
print("____________________________________")

pay1.Payment()
print("____________________________________")
message = name,"Thank you for supporting us ...Come Again"
print(message)

print("")
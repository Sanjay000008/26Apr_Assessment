def Friut_Store():
    print('''
Welcome To Fruit Store App

                        Operations Manu
                        1) Add Fruit Stock
                        2) View Fruit Stock
                        3) Update Fruit Stock

    ''')

#1) Add Fruit Stock In Fruit Store
def Add_fruit_stock():

    file = open("FruitStore.txt",'a+')
    #Fruit Name:-
    f_nm = input("Enter Fruit Name:-")
        

    #Fruit Quantaty:-
    F_Q = True
    while F_Q == True:
        try :
            f_qut = int(input("Enter Fruit Quantity(In KG):- "))
        except:
            print("\n-----------------Please Enter Only Integer--------------------")
        else:
            F_Q = False


    #Fruit Prise:-
    F_P = True
    while F_P == True:
        try :
            f_pr = int(input("Enter Fruit Prise:- "))
        except:
            print("\n-----------------Please Enter Only Integer--------------------")
        else:
            F_P = False

    t = ['Fruit_name','Fruit_Quantity(kg)','Fruit_Prise']
    s = [f_nm,f_qut,f_pr]

    dic1 = dict(zip(t,s))
    file.write(f"{dic1}\n")
    file.close()

# View Fruit Stock:-
def View_Stock():

    file = open("FruitStore.txt",'r+')

    for i in file:
        print(i)

    file.close()


# Update Fruit Stock:-
def Update_Stock():
    file = open("FruitStore.txt",'r+')
    c=file.read()
    l=c.splitlines()
    d ={}
    for i in l:()
    key,value = i.split(':')
    d.update({key.strip():value.strip()})








    


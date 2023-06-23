
Main = True
while Main == True:
    print('''

            Welcome Fruit Store

            Select Your Role

                1)Manager
                2)Cumster

                3)Exit
    
    
    ''')
    con = True
    while con == True:
        try:
            choice = int(input("Enter Your Role:-"))
        except:
            print("\n--------------------Please Enter Only Integer--------------------")
        else:
            if choice <= 3 and choice > 0 :
                con = False
        finally:
            print("Welcome To Fruit Store")

    Fruit =True
    while Fruit == True:
        if choice == 1:
            import Fruit_Manager
            Fruit_Manager.Friut_Store

            con1 = True
            while con1 == True:
                try:
                    Fruit_Manager.Friut_Store()
                    choice=int(input("Engter operation which you want to perform:-"))
                except:
                    print("\n----------------Please Enter Only Integer----------------")
                else:
                    if choice <=3 and choice > 0:
                        con1 = False

            #1) Add Fruit Stock
            if choice == 1:
                Fruit_Manager.Add_fruit_stock()
            
            #2) View Fruit Stock
            if choice == 2:
                Fruit_Manager.View_Stock()

            #3) Update Fruit Stock
            if choice == 3:
                Fruit_Manager.Update_Stock()

            back = True
            while back == True:
                try:
                    x =str(input("Do you wan't to countinue Press 'y' for 'yes' 'n' for 'no':-"))
                except:
                    pass
                else:
                    if x == 'y' or x == 'n':
                        back = False
                    else:
                        print("\n---------------Please Enter 'y' or 'n'")

            if x == 'y':
                Fruit = True
            else:
                Fruit = False
        if choice == 3:
            Main = False
            Fruit = False
            print("Thanks for visit Fruit Store")
                
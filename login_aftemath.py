
import mysql.connector as mysql
IP_project = mysql.connect(host="localhost",user="root",password=Mysql_password,database="IP_project")
cursor = IP_project.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS item_table (itemid int(3), item_name varchar(20), price float(10,2), itemcategory varchar(30))")
IP_project.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS cart_table(itemid int(3),itemname varchar(20),price float(10,2),quantity int(3),totalprice float(100,2))")
IP_project.commit()
cursor.execute("TRUNCATE TABLE cart_table")
IP_project.commit()

def login_aftermath():
    b=0
    while b==0:
        print("""********************************************MAIN MENU********************************************
    1)SHOP
    2)VIEW CART
    3)CHECKOUT
    """)
        user_input_main=int(input("ENTER OPTION: "))

    ##******************************************definitions*********************************************************
        def delete_cartitem(itemid):
            newquantity=new-itemq
            cursor.execute(f"SELECT price FROM cart_table WHERE itemid={itemid}")
            price=cursor.fetchone()[0]
            totalprice=price*newquantity
            sql="update cart_table set quantity=%s,totalprice=%s where itemid=%s"
            val=(newquantity,totalprice,itemid)
            cursor.execute(sql,val)
            IP_project.commit()
            print(f"ITEM WITH ITEM ID {itemid} HAS BEEN DELTED")
            cursor.execute("select * from cart_table")
            print(cursor.fetchall())

    ##***************************************option computation***********************************************************

        if user_input_main==1:#SHOP
            import adding_product_to_cart as addtocart
            addtocart.add_to_cart()

        elif user_input_main==2:    #VIEW CART
            print("""********************************************CART********************************************""")
            import efficiency_definations as ed
            cursor.execute("select * from cart_table")
            ed.print_table(cursor.fetchall(),["Itemid","Itemname","Price","Quantity","Totalprice"])
            cursor.execute("select sum(totalprice) from cart_table")
            totalcost=cursor.fetchall()[0][0]
            print("GRAND TOTAL: ",totalcost)
            
            return_to_aftermath=False
            while not return_to_aftermath:
                print("""
    1)DELETE ITEM
    2)RETURN
        """)
                viewcart_user_choice=int(input("ENTER OPTION: "))
                if viewcart_user_choice==1:
                    itemid_correct=True
                    while itemid_correct:
                        itemid=int(input("ENTER ID: "))
                        cursor.execute(f"select * from cart_table where itemid={itemid}")
                        results = cursor.fetchall()
                        row_count = cursor.rowcount
                        if row_count==0:
                            print("***ITEM ID DOES NOT EXIST***")
                        else:
                            itemquantitycorrect=True
                            while itemquantitycorrect:
                                itemq=int(input("ENTER QUANTITY"))
                                cursor.execute(f"SELECT quantity FROM cart_table WHERE itemid={itemid}")
                                new=cursor.fetchone()[0]
                                if itemq<=0 or itemq>new:
                                    print("Invalid Quantity")
                                elif itemq==new:
                                    cursor.execute(f"delete from cart_table where itemid={itemid}")
                                    IP_project.commit
                                    print("ITEM DELETD SUCCESFULLY")
                                    itemid_correct = False
                                    itemquantitycorrect=False
                                    cursor.execute("select sum(totalprice) from cart_table")
                                    totalcost=cursor.fetchall()[0][0]
                                    print("GRAND TOTAL: ",totalcost)
                                else:
                                    itemquantitycorrect=False
                                    delete_cartitem(itemid)
                                    cursor.execute("select * from cart_table")
                                    ed.print_table(cursor.fetchall(),["Itemid","Itemname","Price","Quantity","Totalprice"])
                                    itemid_correct = False
                                    cursor.execute("select sum(totalprice) from cart_table")
                                    totalcost=cursor.fetchall()[0][0]
                                    print("GRAND TOTAL: ",totalcost)
                                    
                               
                            

                elif viewcart_user_choice==2:
                    return_to_aftermath=True

        elif user_input_main==3:
            pass
            quit()
                    


                    
                    
                
                    
            
                
            

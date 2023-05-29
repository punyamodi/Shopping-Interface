import mysql.connector as mysql
import efficiency_definations as ED

IP_project = mysql.connect(host="localhost",user="root",password=Mysql_password,database="IP_project")
cursor = IP_project.cursor()
##FINIDHING TOUCH if no product in category table print no product so loop desnt happen
def add_to_cart():
    user_wants_to_shop=True
    while user_wants_to_shop:
        print("""********************************SHOPPING**************************
    SELECT CATEGORY
    1) ELECTRONIC
    2) GROCERY
    3) TOYS
    4) CLOTHING
    5) EXIT SHOPPING
    """)
        user_cart_input=int(input("ENTER OPTION: "))

        #=============ELECTRONICS======================

        if user_cart_input==1:
            
            cursor.execute(f"select * from item_table where itemcategory='electronic'")
            ED.print_table(cursor.fetchall() ,['Item_ID','Item_Name','Price','Category'])
            
            in_category=True
            while in_category:
                    itemid=int(input("ENTER ID: "))
                    cursor.execute(f"select * from cart_table where itemid={itemid}")
                    results = cursor.fetchall()
                    row_count = cursor.rowcount
                    if row_count==0:
                        cursor.execute(f"select * from item_table where itemid={itemid}")
                        results = cursor.fetchall()
                        row_count = cursor.rowcount
                        if row_count==0:
                            print("ERROR: ITEM ID DOES NOT EXIST")
                        else:
                            in_category=False
                            correct_quantity=False
                            while not correct_quantity:
                                item_quntity=int(input("ENTER QUANTITY: "))
                                if item_quntity<=0:
                                    print("***INVALID QUANTITY***")
                                else:
                                    correct_quantity=True
                                    cursor.execute(f"select price from item_table where itemid={itemid}")
                                    item_price=cursor.fetchall()[0][0]
                                    totalprice=item_price*item_quntity
                                    cursor.execute(f"select item_name from item_table where itemid={itemid}")
                                    item_name=cursor.fetchall()[0][0]
                                    sql="insert into cart_table values(%s,%s,%s,%s,%s)"
                                    val=(itemid,item_name,item_price,item_quntity,totalprice)
                                    cursor.execute(sql,val)
                                    IP_project.commit()
                                    print("ITEM ADDED TO CART SUCCESFULLY")
                        
                    else:
                        in_category=False
                        cursor.execute(f"select quantity from cart_table where itemid={itemid}")
                        q=cursor.fetchone()[0]
                        qinput=int(input("ENTER QUANTITY:"))
                        item_quantity=qinput+q
                        sql="update cart_table set quantity=%s where itemid=%s"
                        val=(item_quantity,itemid)
                        cursor.execute(sql,val)
                        IP_project.commit()
                        cursor.execute(f"select price from item_table where itemid={itemid}")
                        price=cursor.fetchall()[0][0]
                        totalprice=item_quantity*price
                        sql="update cart_table set totalprice=%s where itemid=%s"
                        val=(totalprice,itemid)
                        cursor.execute(sql,val)
                        IP_project.commit()
                        print("ITEM ADDED TO CART SUCCESFULLY")
                        
                                    

        #========================GROCERY======================

        elif user_cart_input==2:

            cursor.execute(f"select * from item_table where itemcategory='grocery'")
            ED.print_table(cursor.fetchall() ,['Item_ID','Item_Name','Price','Category'])
            
            in_category=True
            while in_category:
                    itemid=int(input("ENTER ID: "))
                    cursor.execute(f"select * from cart_table where itemid={itemid}")
                    results = cursor.fetchall()
                    row_count = cursor.rowcount
                    if row_count==0:
                        cursor.execute(f"select * from item_table where itemid={itemid}")
                        results = cursor.fetchall()
                        row_count = cursor.rowcount
                        if row_count==0:
                            print("ERROR: ITEM ID DOES NOT EXIST")
                        else:
                            in_category=False
                            correct_quantity=False
                            while not correct_quantity:
                                item_quntity=int(input("ENTER QUANTITY: "))
                                if item_quntity<=0:
                                    print("***INVALID QUANTITY***")
                                else:
                                    correct_quantity=True
                                    cursor.execute(f"select price from item_table where itemid={itemid}")
                                    item_price=cursor.fetchall()[0][0]
                                    totalprice=item_price*item_quntity
                                    cursor.execute(f"select item_name from item_table where itemid={itemid}")
                                    item_name=cursor.fetchall()[0][0]
                                    sql="insert into cart_table values(%s,%s,%s,%s,%s)"
                                    val=(itemid,item_name,item_price,item_quntity,totalprice)
                                    cursor.execute(sql,val)
                                    IP_project.commit()
                                    print("ITEM ADDED TO CART SUCCESFULLY")
                        
                    else:
                        in_category=False
                        cursor.execute(f"select quantity from cart_table where itemid={itemid}")
                        q=cursor.fetchone()[0]
                        qinput=int(input("ENTER QUANTITY:"))
                        item_quantity=qinput+q
                        sql="update cart_table set quantity=%s where itemid=%s"
                        val=(item_quantity,itemid)
                        cursor.execute(sql,val)
                        IP_project.commit()
                        cursor.execute(f"select price from item_table where itemid={itemid}")
                        price=cursor.fetchall()[0][0]
                        totalprice=item_quantity*price
                        sql="update cart_table set totalprice=%s where itemid=%s"
                        val=(totalprice,itemid)
                        cursor.execute(sql,val)
                        IP_project.commit()
                        print("ITEM ADDED TO CART SUCCESFULLY")
            
            

        #========================TOYS=======================

        elif user_cart_input==3:

            cursor.execute(f"select * from item_table where itemcategory='toys'")
            ED.print_table(cursor.fetchall() ,['Item_ID','Item_Name','Price','Category'])
            
            in_category=True
            while in_category:
                    itemid=int(input("ENTER ID: "))
                    cursor.execute(f"select * from cart_table where itemid={itemid}")
                    results = cursor.fetchall()
                    row_count = cursor.rowcount
                    if row_count==0:
                        cursor.execute(f"select * from item_table where itemid={itemid}")
                        results = cursor.fetchall()
                        row_count = cursor.rowcount
                        if row_count==0:
                            print("ERROR: ITEM ID DOES NOT EXIST")
                        else:
                            in_category=False
                            correct_quantity=False
                            while not correct_quantity:
                                item_quntity=int(input("ENTER QUANTITY: "))
                                if item_quntity<=0:
                                    print("***INVALID QUANTITY***")
                                else:
                                    correct_quantity=True
                                    cursor.execute(f"select price from item_table where itemid={itemid}")
                                    item_price=cursor.fetchall()[0][0]
                                    totalprice=item_price*item_quntity
                                    cursor.execute(f"select item_name from item_table where itemid={itemid}")
                                    item_name=cursor.fetchall()[0][0]
                                    sql="insert into cart_table values(%s,%s,%s,%s,%s)"
                                    val=(itemid,item_name,item_price,item_quntity,totalprice)
                                    cursor.execute(sql,val)
                                    IP_project.commit()
                                    print("ITEM ADDED TO CART SUCCESFULLY")
                        
                    else:
                        in_category=False
                        cursor.execute(f"select quantity from cart_table where itemid={itemid}")
                        q=cursor.fetchone()[0]
                        qinput=int(input("ENTER QUANTITY:"))
                        item_quantity=qinput+q
                        sql="update cart_table set quantity=%s where itemid=%s"
                        val=(item_quantity,itemid)
                        cursor.execute(sql,val)
                        IP_project.commit()
                        cursor.execute(f"select price from item_table where itemid={itemid}")
                        price=cursor.fetchall()[0][0]
                        totalprice=item_quantity*price
                        sql="update cart_table set totalprice=%s where itemid=%s"
                        val=(totalprice,itemid)
                        cursor.execute(sql,val)
                        IP_project.commit()
                        print("ITEM ADDED TO CART SUCCESFULLY")

            
            
            

        #=======================CLOTHING=======================

        elif user_cart_input==4:
            
           cursor.execute(f"select * from item_table where itemcategory='clothing'")
           ED.print_table(cursor.fetchall() ,['Item_ID','Item_Name','Price','Category'])
           in_category=True
           while in_category:
                    itemid=int(input("ENTER ID: "))
                    cursor.execute(f"select * from cart_table where itemid={itemid}")
                    results = cursor.fetchall()
                    row_count = cursor.rowcount
                    if row_count==0:
                        cursor.execute(f"select * from item_table where itemid={itemid}")
                        results = cursor.fetchall()
                        row_count = cursor.rowcount
                        if row_count==0:
                            print("ERROR: ITEM ID DOES NOT EXIST")
                        else:
                            in_category=False
                            correct_quantity=False
                            while not correct_quantity:
                                item_quntity=int(input("ENTER QUANTITY: "))
                                if item_quntity<=0:
                                    print("***INVALID QUANTITY***")
                                else:
                                    correct_quantity=True
                                    cursor.execute(f"select price from item_table where itemid={itemid}")
                                    item_price=cursor.fetchall()[0][0]
                                    totalprice=item_price*item_quntity
                                    cursor.execute(f"select item_name from item_table where itemid={itemid}")
                                    item_name=cursor.fetchall()[0][0]
                                    sql="insert into cart_table values(%s,%s,%s,%s,%s)"
                                    val=(itemid,item_name,item_price,item_quntity,totalprice)
                                    cursor.execute(sql,val)
                                    IP_project.commit()
                                    print("ITEM ADDED TO CART SUCCESFULLY")
                        
                    else:
                        in_category=False
                        cursor.execute(f"select quantity from cart_table where itemid={itemid}")
                        q=cursor.fetchone()[0]
                        qinput=int(input("ENTER QUANTITY:"))
                        item_quantity=qinput+q
                        sql="update cart_table set quantity=%s where itemid=%s"
                        val=(item_quantity,itemid)
                        cursor.execute(sql,val)
                        IP_project.commit()
                        cursor.execute(f"select price from item_table where itemid={itemid}")
                        price=cursor.fetchall()[0][0]
                        totalprice=item_quantity*price
                        sql="update cart_table set totalprice=%s where itemid=%s"
                        val=(totalprice,itemid)
                        cursor.execute(sql,val)
                        IP_project.commit()
                        print("ITEM ADDED TO CART SUCCESFULLY") 


        elif user_cart_input==5:
            print("EXITING SHOPPING.......................................................................")
            user_wants_to_shop=False

        elif user_cart_input>5 or user_cart_input<=0:
            print('***INVALID CATEGORY***')

        else:
            print('***INVALID ENTRY***')
            
                                
## by Team EAGLE - KAPP

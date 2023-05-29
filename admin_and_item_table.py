from prettytable import PrettyTable as PT
import mysql.connector as mysql
IP_project = mysql.connect(host="localhost",user="root",password=Mysql_password,database="IP_project")
cursor = IP_project.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS item_table (itemid int(3), item_name varchar(20), price float(10,2), itemcategory varchar(30))")
IP_project.commit()




quit_admin=False
while quit_admin==False:
    print("""
**********************************************ADMIN OPTIONS***********************************
    1)ENTER NEW ITEM
    2)DELETE OLD ITEM
    3)CHANGE PRICE
    4)CHANGE CATEGORY
    5)CHANGE NAME
    6)EXIT
    """)
## ALL THE DEFfinitions
    def insert_item(itemid,itemname,price,itemcategory):
        sql="insert into item_table values(%s,%s,%s,%s)"
        val=(itemid,itemname,price,itemcategory)
        cursor.execute(sql,val)
        IP_project.commit()
        print("NEW ITEM INSERTED")
        cursor.execute(f"select * from item_table")
        results = cursor.fetchall()
        
        insert_item_table = PT()
        insert_item_table.field_names = ['Item_ID','Item_Name','Price','Category']
        for array_tuple in results:
            insert_item_table.add_row(array_tuple)
        print(insert_item_table)
        

    def delete_item(itemid):
        cursor.execute(f"DELETE FROM item_table WHERE itemid={itemid}")
        IP_project.commit()
        print(f"ITEM WITH ITEM ID {itemid} HAS BEEN DELTED")
        cursor.execute("select * from item_table")
        results = cursor.fetchall()

        delete_item_table = PT()
        delete_item_table.field_names = ['Item_ID','Item_Name','Price','Category']
        for array_tuple in results:
            delete_item_table.add_row(array_tuple)
        print(delete_item_table)

    def changeprice_item(itemprice):
        cursor.execute(f"UPDATE item_table SET price={itemprice} where itemid={itemid}")
        IP_project.commit()
        print("PRICE CHANGED SUCCESFULLY")
        cursor.execute(f"select * from item_table ")
        results = cursor.fetchall()

        change_price_item_table = PT()
        change_price_item_table.field_names = ['Item_ID','Item_Name','Price','Category']
        for array_tuple in results:
            change_price_item_table.add_row(array_tuple)
        print(change_price_item_table)

    def changecategory_item(itemcategory):
        sql="UPDATE item_table SET itemcategory=%s where itemid=%s"
        val=(itemcategory,itemid)
        cursor.execute(sql,val)
        IP_project.commit()
        print("CATEGORY CHANGED SUCCESFULLY")
        cursor.execute(f"select * from item_table ")
        results = cursor.fetchall()

        change_cat_item_table = PT()
        change_cat_item_table.field_names = ['Item_ID','Item_Name','Price','Category']
        for array_tuple in results:
            change_cat_item_table.add_row(array_tuple)
        print(change_cat_item_table)

    def changename_item(item_name):
        sql="UPDATE item_table SET item_name=%s where itemid=%s"
        val=(item_name,itemid)
        cursor.execute(sql,val)
        IP_project.commit()
        print("ITEM NAME CHANGED SUCCESFULLY")
        cursor.execute(f"select * from item_table ")
        results = cursor.fetchall()

        change_name_item_table = PT()
        change_name_item_table.field_names = ['Item_ID','Item_Name','Price','Category']
        for array_tuple in results:
            change_name_item_table.add_row(array_tuple)
        print(change_name_item_table)
        

## all code without definitions to perform operations starts from here
##OPTION INPUT***********************************************************************************************************************************        
    admin_choice=int(input("ENTER OPTION: "))
        
## INSERT ITEM***********************************************************************************************************************************
    if admin_choice==1:
        insert_item_exists=False
        while not insert_item_exists:
            itemid=int(input("ENTER ID: "))
            cursor.execute(f"select * from item_table where itemid={itemid}")
            results = cursor.fetchall()
            row_count = cursor.rowcount
            if row_count==0:
                itemname=input("ENTER NAME: ")
                invalidprice=True
                while invalidprice:
                    price=float(input("ENTER PRICE: "))
                    if price<0:
                        print("Invalid Price")
                    else:
                        invalidprice=False
                invalidcat=True
                while invalidcat:
                    cat=['ELECTRONIC',"TOYS","CLOTHING","GROCERY"]
                    itemcategory=input("ENTER CATEGORY: ")
                    if itemcategory not in cat:
                        print("*** Invalid Category ***")
                    else:
                        invalidcat=False
                    
                insert_item(itemid,itemname,price,itemcategory)
                cursor.execute("select * from item_table")
                print(cursor.fetchall())
                insert_item_exists=True
            else:
                print("***ITEM ID ALREADY EXSISTS***")

##DELETE ITEM**************************************************************************************************************************************
    if admin_choice==2:
        cursor.execute("select * from item_table")
        print(cursor.fetchall())
        
        delete_item_exists=True
        while delete_item_exists:
            itemid=int(input("ENTER ITEM ID: "))
            cursor.execute(f"select * from item_table where itemid={itemid}")
            results = cursor.fetchall()
            row_count = cursor.rowcount
            if row_count==0:
                print("***ITEM ID DOES NOT EXIST***")
            else:
                delete_item(itemid)
                delete_item_exists=False

## CHANGE PRICE OF ITEM******************************************************************************************************************************
    if admin_choice==3:
        cursor.execute("select * from item_table")
        print(cursor.fetchall())
        price_change_item_exists=True
        while price_change_item_exists:
            itemid=int(input("ENTER ITEM ID: "))
            cursor.execute(f"select * from item_table where itemid={itemid}")
            results = cursor.fetchall()
            row_count = cursor.rowcount
            if row_count==0:
                print("***ITEM ID DOES NOT EXIST***")
            else:
                itemprice=float(input("ENTER NEW PRICE: "))
                changeprice_item(itemprice)
                price_change_item_exists = False

##CHANGE CATEGORY*********************************************************************************************************************************
    if admin_choice==4:
        cursor.execute("select * from item_table")
        print(cursor.fetchall())
        change_cat_item_exists=True
        while change_cat_item_exists:
            itemid=int(input("ENTER ITEM ID: "))
            cursor.execute(f"select * from item_table where itemid={itemid}")
            results = cursor.fetchall()
            row_count = cursor.rowcount
            if row_count==0:
                print("***ITEM ID DOES NOT EXIST***")
            else:
                itemcategory=input("ENTER NEW CATEGORY: ")
                changecategory_item(itemcategory)
                change_cat_item_exists=False

##CHANGE NAME***************************************************************************************************************************************
    if admin_choice==5:
        cursor.execute("select * from item_table")
        print(cursor.fetchall())
        change_name_item_exists=True
        while change_name_item_exists:
            itemid=int(input("ENTER ITEM ID: "))
            cursor.execute(f"select * from item_table where itemid={itemid}")
            results = cursor.fetchall()
            row_count = cursor.rowcount
            if row_count==0:
                print("***ITEM ID DOES NOT EXIST***")
            else:
                item_name=input("ENTER NEW NAME: ")
                changename_item(item_name)
                change_name_item_exists=False


## EXIT***********************************************************************************************************************************************
    if admin_choice==6:
        print("***************************THANK YOU*************************************")
        quit_admin = True
        exit()
                
## INVALID OPTION*************************************************************************************************************************************
    if admin_choice>6 or admin_choice<=0:
        print("***INVALID OPTION***")
        


        
    

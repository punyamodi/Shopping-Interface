import mysql.connector as mysql
IP_project = mysql.connect(host="localhost",user="root",password=Mysql_password,database="IP_project")
cursor = IP_project.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS user_table (name VARCHAR(30),password varchar(30), email_id varchar(30), address VARCHAR(255))")

cursor.execute("SELECT email_ID, password FROM user_table WHERE email_ID = 'ADMIN@ADMIN.COM' and password = 'ADMIN123'")
cursor.fetchall()
row_count_admin = cursor.rowcount

if row_count_admin == 0:
    cursor.execute("INSERT INTO user_table VALUES ( 'ADMIN', 'ADMIN123', 'ADMIN@ADMIN.COM', 'REDACTED')")
    IP_project.commit()
else:
    pass

#==================================================================================
                                                        #check login
def Login(): 
    login = False
    while not login:
        login_email = str(input("Email: "))
        login_password = str(input("Password: "))
        if login_email == 'ADMIN@ADMIN.COM' and login_password == 'ADMIN123':
            login_admin = 'admin'
            return login_admin
        else:
            cursor.execute("SELECT email_id,password,name FROM user_table WHERE email_id = %s and password=%s",(login_email,login_password))
            results = cursor.fetchall()
            row_count = cursor.rowcount
            if row_count==0 or results[0][0]=="ADMIN@ADMIN.COM":
                print("***Incorrect Details, Try Again***")
            else:
                login=True
                print(f'Welcome {results[0][2].capitalize()} to [Title]')

#=================================================================================            
                                                 
def Signup():
    signup_name = str(input("Set Name: "))#main name

    i=0
    while i==0:
        #----------------to check email is valid or not
        email_unique = False
        while not email_unique:
            signup_user_email = str(input("Set Email ID: "))#main email
            find_com=signup_user_email.find(".com") 
            find_A=signup_user_email.find('@')
            if find_com==-1 or find_A==-1:
                print("***Invalid Email ID, Please Make Sure Your Email Has '@' and '.com'***")
            elif signup_user_email=="ADMIN@ADMIN.COM" or signup_user_email=="admin@admin.com" :
                print("***Invalid Email ID, This Email Cannot Be Used ***") 
            else:
                i=1
                
            #----------------checks whether email is unique or not
                cursor.execute("SELECT Name,email_id FROM user_table WHERE Name = %s and email_id=%s",
                               (signup_name,signup_user_email))
                results = cursor.fetchall()
                row_count = cursor.rowcount

                if row_count==0: #means the email is unique
                    
                    email_unique = True
                    #-------------checks if passwd and confirm passwd are equal
                    p1_equal_p2= False
                    while not p1_equal_p2:
                        Invalidpass=True
                        while Invalidpass:
                            passwd1 = str(input("Set Password: "))
                            if len(passwd1)>30:
                                print("Invalid Password, Password Length Should Be Less Than 30 Characters")
                            else:
                                Invalidpass=False
                        passwd2 = str(input("Confirm Password: "))
                        if passwd1 == passwd2:
                            signup_passwd = passwd1#main passwd
                            signup_user_address = str(input("Set Address: "))#main address
                            break
                        else:
                            print('***Passwords DO NOT Match***')
                            p1_equal_p2 = False
                            
                    #--------------inserts the signup values into mysql
                    sql = "INSERT INTO user_table (name,password,email_id,address) VALUES (%s,%s,%s,%s)"
                    val =(signup_name,signup_passwd,signup_user_email,signup_user_address)
                    cursor.execute(sql, val)
                    IP_project.commit()
                    print('Your Account Has Been Created Successfully')
                    
                else: #means email is not unique
                    print("***This Email ID Already Exists, Please Try Again***")
                    email_unique = False
        



    
    

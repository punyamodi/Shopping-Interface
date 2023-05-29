
import time



Ids={hash("lol"):hash("lmao")}

#########################################################################################################################################
def Login():
        IDPresent=False
        while IDPresent==False:
                name=input("enter username")
                time.sleep(0.5)

                if "'" in name or '"' in name:
                        print("Invalid UserName")
                else:
                        name=hash(name)
                        if name==0:
                                IDPresent=True
                                break
                        
                            
                        elif name in Ids:
                                IDPresent=False
                                passkey=False
                                while passkey==False:
                                        password=input("Enter Password:")
                                        if "'" in password or '"' in password:
                                                print("Invalid Password")
                                        else:
                                                password=hash(password)
                                                if password==0:
                                                        break
                                                elif password==Ids[name]:
                                                        print("access granted")
                                                        passkey=True
                                                        IDPresent=True
                                                        
                                                else:
                                                        print("Incorrect password")
                                                        pass
                                
                                        
                                        
                                                

                                    
                        else:
                                print("This username does not exit")
                
                        
                    
                
                
                
            
#####################################################################################################################################

def Signup():
            signup=False
            while signup==False:
                Id_name=input("Enter Username:")
                time.sleep(0.5)
                if "'" in Id_name or '"' in Id_name:   ### this is to prevent error whil mysql injections
                        print("Invalid Username")
                        print("cannot use")
                        print("'")
                        print('"')
                else:
                        Id_name=hash(Id_name)
                        if Id_name==0:
                            break
                        else:
                            Id_password=False
                            while Id_password==False:
                                password=input("Enter Password:")
                                time.sleep(0.5)
                                if "'" in password or '"' in password:
                                        print("Invalid Password")
                                        print("cannot use")
                                        print("'")
                                        print('"')
                                else:
                                        password=hash(password)
                                        if password==0:
                                            break
                                        else:
                                            Ids[Id_name]=password
                                            Id_password=True
                                            signup=True
                                            print("Account Created succesfully")
                                        
                        
                                
                              
                
#########################################################################################################################################
stop=False
while stop==False:
    print("""Welcome to DSA
press
1-Login
2-Signup
3-Exit
""")
    try:
        action=int(input("Enter Action:"))
        if action==3:
                stop=True
                break
        elif action==1:
                Login()
        elif action==2:
                Signup()
        else:
                print("invalid Action")
    except:
        pass

    
    







##############################################################################        
##        if action==3:
##            stop=False
############################################################################
##        elif action==1:
    
###########################################################################                   
##        elif action==2:
        
    
                               
###########################################################################
##    except:
##        pass

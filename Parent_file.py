import homescreen_definations as defn


print('''*******************[Title]*******************
Login(press 1)                            Sign up(press 2)''')

startup_input=str(input('''                     Enter the code: '''))


signup_required = True
while signup_required:
    if startup_input == '1': #login 
        print('------------------LOGIN-----------------')
        if defn.Login() == 'admin':
            import admin_and_item_table as admin_ex
        else:
            signup_required=False
            import login_aftemath as logafter
            logafter.login_aftermath()
                  

    elif startup_input == '2': #signup
        print('------------------SIGNUP------------------')
        defn.Signup()
        signup_required = True
        startup_input = '1'

#-----------------------------------------------------


file_data=[]

def welcome_screen():
    user_choice=int(input('****welcome to file world****\n 1.Append content \n 2.new content\n 3.display content\n 4.exit app\n provide option:'))
    
    return user_choice

def user_option(user_input):
    if user_input==1:
       append()
       
    elif user_input==2:
        new()
    
    elif user_input==3:
        display()
    
    elif user_input==4:
        exit
        
    else:
        print('provide a valid input')
    user_option(welcome_screen())


def append():
        add=input('enter file content name:')
        content=input('enter content:')
        file=open(add,'a')
        file.write(content)
        print('file appende sucessfully')
        file.close()
        
def new():
     add=input('enter file content name:')
     content=input('enter content:')
     file =open(add,"w")
     file.write(content)
     print('content saved to file sucessfully') 
     file.close()
     
def display():
   add=input('enter file content name:')
   file=open(add,"r") 
   print(file.read())
   file.close()    
pella=welcome_screen()
user_option(pella)
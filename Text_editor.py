import os

def read_file(file_name):
  with open(file_name,'r') as file:
     return file.read() 
  

def write_file(file_name, content):
    with open(file_name ,'w') as file:
        file.write(content)
        

def user_input():
    print('Enter your text(type SAVE on a new line to save and exit)')    
    lines=[]     
    while True: 
        line=input() 
        if line =='SAVE':
            break
        lines.append(line)
        return ('\n'.join(lines))

def main():
    file_name= input('Enter filename or create anew file: ')
    try:   
        if os.path.exists(file_name): 
            print(read_file(file_name))
        else:
           write_file(file_name,'')
           
        content=user_input() 
        write_file(file_name,content)   
        print(f'{file_name} saved.') 
    except OSError:
        print(f'{file_name} could not be opened')
        return
    
    
if __name__=='__main__':
    main()
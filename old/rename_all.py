import os
  
print(os.getcwd())
COUNT = 1


  
# Function to increment count 
# to make the files sorted.
def increment():
    global COUNT
    COUNT = COUNT + 1
  
  
for f in os.listdir(os.getcwd()):
    f_name, f_ext = os.path.splitext(f)
    increment()
    print(f_name, f_ext)
    if f_ext == '.txt':  
        new_name = '{}.{}'.format(f_name, 'md')
        os.rename(f, new_name)
        print('Renamed to {}'.format(new_name))

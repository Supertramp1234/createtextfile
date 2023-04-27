#text = input('enter a text')
#filename = input('enter a filename')
#textname = filename +".txt"
#f= open(textname,"w+")
#f.write(text)
#f.close()


import os

# Prompt user for input
text = input('Please enter the text: ')
filename = input('Please enter the filename: ')

# Check if filename is valid
if not filename.endswith('.txt'):
    filename += '.txt'

# Check if file already exists
if os.path.exists(filename):
    response = input('The file already exists. Do you want to overwrite the file? (yes/no): ')
    if response.lower() != 'yes':
        print('The file was not overwritten.')
        exit()

# Write file
with open(filename, 'w') as file:
    file.write(text)

# Confirmation message
print(f'The text was successfully saved in {filename}.')

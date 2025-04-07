#Read in the echo.txt file and display it in the terminal using print()
#This is a guided practice. Either follow the video or your instructor in class.

# Open the file in read mode
with open('echo.txt', 'r') as file:
    # Read the contents of the file
    content = file.read()
    # Print the content to the terminal
    print(content)

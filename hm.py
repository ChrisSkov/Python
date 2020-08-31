File_Object = open("look.txt", "r+")
print(File_Object)
str1 = "hmmm"
print(File_Object.readlines())
File_Object.write(str1)
print(File_Object.readlines())
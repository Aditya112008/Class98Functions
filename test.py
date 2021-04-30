print("Hello")
f = open("test.txt", "r")
#print(f.read())
#open (file name , mode) mode can be - r, w, a, x
print(f.read(5))

fileLines = f.readlines()
for line in fileLines:
    print(line)

    introString = "I love coding"
    words = introString.split()
    print(words)
    print(len(words))
    
    def my_function():
        print("Hello I am a Function")

    my_function()

    def greet(name):
        print("Hello " + name)

    greet("Aditya")  

    
def greet(name,country):
    print(name)
    print(country)
    print("hi",name,"your favorite country",country)
    print(f"hi{name}your favorite country is{country}")#you can use these to call the function,f is used as a template
    
greet("ian","america")#or these to also call the function
greet("don","brazil")


def outer():
    print("This is the outer function")

greet("ian","america")#or these to also call the function
greet("don","brazil")    


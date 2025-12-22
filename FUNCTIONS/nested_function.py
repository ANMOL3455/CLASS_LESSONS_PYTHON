#inner functions cannot be called from outside
def data():
    print("This is a data function")
    def information():
        print("This is a information function")
    information()
    #called here in the data block
    
data()
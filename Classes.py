class Laptop:

    #ram ='8 gb'
    #brand = 'Lenovo'
    #hdd ='1 tb'
    #resolution ='1080p'

    def __init__(self, brd, ram, hdd, resolution, space):
        self.brand = brd 
        self.ram = ram 
        self.hdd = hdd
        self.res = resolution
        self.space = space

    def playGame(self):
        if self.ram > 8:
            print('Laptop plays games')
        else:
            print('Not Sufficient RAM')

    def playVedio(self):
        print('Laptop plays videos')

#lappy = Laptop()

#lappy.playGame()

#print(lappy.resolution)

#lappy2 = Laptop()

#print(lappy.resolution)

mylappy = Laptop('ASUS', 8, '1 TB', '1080p', 124)

print(mylappy.brand)
mylappy.playGame()

mylappy2 = Laptop('HP', 16, '2TB', '720p', 450)

print(mylappy2.hdd)
mylappy2.playGame()
print(mylappy2.space)
class TV:
        def __init__(self):
            self.powered_on = False
            self.volume = 0
            self.channel = 0


        def power_on(self):
            self.powered_on = True

        def power_off(self):
            self.powered_on = False

        def increase_volume(self):
            if self.powered_on:
                self.volume += 1


        def decrease_volume(self):
            if self.powered_on and self.volume > 0:
                self.volume -= 1

        def change_channel(self):
            if self.powered_on:
                self.channel +=1

        def __str__(self):
            return f"{self.powered_on}, {self.volume}, {self.channel}"




my_tv = TV()


print(my_tv.powered_on)
print(my_tv.volume)

my_tv.power_on()
print(my_tv.powered_on)



my_tv.increase_volume()
print(my_tv.volume)


my_tv.increase_volume()
print(my_tv.volume)

my_tv.decrease_volume()
print(my_tv.volume)

my_tv.decrease_volume()
print(my_tv.volume)

my_tv.decrease_volume()
print(my_tv.volume)

my_tv.change_channel()
print(my_tv.channel)
my_tv.power_off()
print(my_tv)

my_tv.change_channel()
print(my_tv.channel)

print(my_tv)








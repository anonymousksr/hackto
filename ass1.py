total=250e100
water=199.5e85
useful_rain=(25e8)*(0.75)
tot=water+useful_rain
inc=tot+(0.15* tot)
inc2=inc+(0.05*inc)
dec1=inc2-(0.05*inc2)
final=dec1-(0.15*dec1)
print("The current level of the reservoir is",final,"cu.meters")

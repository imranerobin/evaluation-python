trame ="$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47"

parties = trame.split(",")
heure= parties[1]


#print(parties[0][1:3])


#print(parties)
#print(parties[1])
print(f"{parties[2]} {parties[3]}")
#print(parties[4])


print(f"{heure [0]}{ heure[1]}:{heure [2]}{ heure[3]}:{heure [4]}{ heure[5]}")
#print(f"{heure [2]}{ heure[3]}:")

# 
# print (parties[1] [0:2]+(parties[1] [2:4]+(parties[1] [4:6])))


#print("Heure")

#print(parties[1] [2:4])

#print("Minute")

#print(parties[1] [4:6])
#print("seconde")


print(f"{parties[4]} {parties[5]}")
















# heure ="heure"



# #tableau=trame.split(",")

# #for element in trame:
#    # print(element)
# print(trame)


# #temps= trame + heure[-5:]

# print(trame[:9])
# #print("heure")
# print(trame[:11])
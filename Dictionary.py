dic = {'Jay': 'Veg', 'Saurabh': 'Non-veg', 'Mihir': {'veg': 'dal batti', 'non-veg': 'Chicken'}}
print(dic)

print(dic['Mihir']['veg'])
dic["Karan"]= "wheat"
del dic["Karan"]

#vic = dic
#del vic['Saurabh'] # update o dic as well for that use copy
#vic = dic.copy()
#del vic['Saurabh']
#print(vic)
#print(dic)
print(dic.get('Jay'))
dic.update({'karan' : 'Tota'})
print(dic)
print(dic.items())
print(dic.values())

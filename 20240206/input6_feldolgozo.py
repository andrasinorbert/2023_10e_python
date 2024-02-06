import own_func as of

valtozo=of.beolvas("input6")

print(valtozo)

str_list=valtozo[0].split(" ")
print(str_list)
szam_str_list=str_list[1].split(",")
print(szam_str_list)

szamok=of.strListToCleanToIntList(szam_str_list)

print(szamok)
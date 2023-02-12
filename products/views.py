#functions place in views
#print total number of mobiles
from products.models import mobiles
print(len(mobiles))
#print all mobile names
# for mob in mobiles:
#     # print(mob["name"])
#       print(mob.get("name")) #using get methode is always better
#
# print([mob.get("name") for mob in mobiles])   #using list comprhnsn

#print all samsung mobiles
# for i in mobiles:
#     if i.get("brand") == "samsung":
#         print(i.get("name"))
samsung_mob = [mob.get("name") for mob in mobiles if mob.get("brand")=="samsung"]
print(samsung_mob)
#sort mobiles wrt price order by desc
print(sorted(mobiles,key = lambda m:m.get("price"),reverse=True))
#print costly mobile
# print(max(mobiles,key=lambda m:m.get("price")))
# print(min(mobiles,key=lambda c:c.get("price")))





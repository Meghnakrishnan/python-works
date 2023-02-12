from json import load
with open("db.json","r",encoding="utf-8") as f:
    data = load(f)
print(len(data))
#print movie names under genres crime
print([m.get("title") for m in data if m.get("genres")=="crime"])
#print al movie name
# movie = [m.get("title") for m in data]
# print(movie)
# lengthy_movie=max(data,key=lambda m:int(m.get("runtime")))
# print(lengthy_movie)
#count movie without counter
# mc = {}
# for m in data:
#     year = m.get("year")
#     if year in mc:
#         mc[year]+=1
#     else:
#         mc[year]=1
# print(mc)
# print(max(mc,key=lambda k:mc.get(k)))
# print(max(mc.items(),key=lambda t:t[1]))
'''DECORATORS'''
# def sub(n1,n2):
#     if n1<n2:
#         n1,n2=n2,n1
#     return n1-n2
# def div(n1,n2):
#     if n1<n2:
#         n1,n2=n2,n1
#     return n1/n2
# print(sub(5,10))
# print(div(5,10))

'''
decorators accept another functions as parameter(not variables),ie it point another function
therre will be another funct inside dec function
'''
def smart_dec(fn):
    def wrapper(n1,n2):
        if n1<n2:
            n1,n2=n2,n1
        return fn(n1,n2)
    return wrapper
@smart_dec
def sub(n1,n2):
    return n1-n2
@smart_dec
def div(n1,n2):
    return n1,n2
print(sub(5,10))
print(div(2,10))

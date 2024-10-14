jan = [31,32]
fev = [33,34]
mar = [35,36]
abr = [37,38]
mai = [39,40]
jun = [29,28]
jul = [27,26]
ago = [25,24]
set = [23,22]
out = [21,19]
nov = [18,17]
dez = [17,16]


media_anual = (jan + fev + mar + abr + mai + jun + jul + ago + set + out + nov + dez)
m=sum(media_anual)
x=m/24
print(f"{x:.2f}")
print(max(media_anual))
print(min(media_anual))

media_anual.sort()
print(media_anual)

media_anual.sort(reverse= True)
print(media_anual)
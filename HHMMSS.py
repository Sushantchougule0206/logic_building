#WAP to convert input number of seconds to HH:MM:SS.
time=int(input("Enter the time:"))
HH=0
MM=0
SS=0
while time>0:
  if time>=3600:
    HH=time//3600
    time=time%3600
  elif time<3600 and time>=60:
    MM=time//60
    time=time%60
  else:
    SS=time
    break

print(HH,":",MM,":",SS)
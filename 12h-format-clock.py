def add_time(start, duration,optional=None):
    d_c=0
    if optional!=None:
        optional=optional.lower()
    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    if start[1]==':':
        h_s=start[0]
        h_sm=start[2:4]
    else:
        h_s=start[:2]
        h_sm=start[3:5]
    h_s=int(h_s)
    h_sm=int(h_sm)
    i=1
    h_d=duration[0]
    while duration[i]!=':':
        h_d+=duration[i]
        i+=1
    i+=1
    h_dm=''
    while i<len(duration):
        h_dm+=duration[i]
        i+=1
    h_d=int(h_d)
    h_dm=int(h_dm)
    start=start[-2:]
    if start=='PM':
        am_or_pm='PM'
    else :
        am_or_pm='AM'
    while h_d > 0:
        if h_s == 12:  
            h_s = 0
            if am_or_pm == "PM":
                am_or_pm = "AM"
                d_c+=1
            else:
                am_or_pm = "PM"
        h_s += 1
        h_d -= 1
    if h_dm+h_sm>59:
        h_s+=1
        if h_s==12 and am_or_pm=='PM':
            d_c+=1
            am_or_pm='AM'
        else:
            am_or_pm='PM'
        minutes=h_dm+h_sm-60
    else:
        minutes=h_dm+h_sm
    h_s=str(h_s)
    minutes=str(minutes)
   
    f_h=h_s
   
    if len(minutes)==1:
       f_m='0'+minutes
    else:
        f_m=minutes
    if optional==None and d_c==0:
        new_time=f_h+':'+f_m+' '+am_or_pm
    elif optional!=None and d_c==0:
        a=optional.capitalize()
        new_time=f_h+':'+f_m+' '+am_or_pm+', '+a
    elif d_c==1 and optional==None:
         new_time=f_h+':'+f_m+' '+am_or_pm+' (next day)'
    elif optional!=None and d_c>0:
        optional=days_of_week[(days_of_week.index(optional)+d_c)%len(days_of_week)]
        a=optional.capitalize()
        if d_c==1:
            new_time=f_h+':'+f_m+' '+am_or_pm+', '+a+' (next day)'
        else:
            new_time=f_h+':'+f_m+' '+am_or_pm+', '+a+' ('+str(d_c)+' days later)'
    elif optional==None and d_c>1:
        new_time=f_h+':'+f_m+' '+am_or_pm+' ('+str(d_c)+' days later)'
    return new_time

from tkinter import Tk, Canvas
from datetime import date,datetime

def get_birthdays():
    birthdays =[]
    with open('birthdays.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            day_of_birth = line.split(',')
            birthdate = datetime.strptime(day_of_birth[1],'%d/%m/%Y').date()
            day_of_birth[1] = birthdate
            birthdays.append(day_of_birth)
    return birthdays

def days_to_go(date1,date2):
    time_until = str(date1 - date2)
    days_to = time_until.split(' ')
    return days_to[0]

root= Tk()
c = Canvas(root,width=700,height=800,bg='indigo')
c.pack()
c.create_text(50,25,anchor='w',fill='orange',\
              font='copperBlack 28 italic underline',\
              text= 'COUNTDOWN TO BIRTHDAYS:')

days_of_birthdays = get_birthdays()
today = date.today()

vertically = 50
for day_of_births in days_of_birthdays:
    name = day_of_births[0]
    num_of_days = days_to_go(day_of_births[1],today)
    #if (num_of_days)== '0':
    display = "it is %s days to %s's birthday" %(num_of_days,name)
    #else:
    #   continue
    #display = "it is %s days to %s's birthday" %(num_of_days,name)
    c.create_text(50,vertically,anchor = 'w',fill='gold',\
                  font='arial 14 italic', text = display)
    vertically +=50
    
                    
    
    

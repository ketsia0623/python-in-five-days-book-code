from datetime import datetime, timedelta 

# Current date and time 
now = datetime.now() 
print(now) 

# Date arithmetic 
tmr = now + timedelta(days=1) 
print(tmr) 

# Formatting dates 
formattedDate = now.strftime('%Y-%m-%d %H:%M:%S') 
print(formattedDate) 

# Parsing dates 
parsedDate = datetime.strptime('2023-06-11', '%Y-%m-%d') 
print(parsedDate)
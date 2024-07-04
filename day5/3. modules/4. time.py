import time 

# Current time in seconds since the Epoch(the epoch is the point where the time starts, the return value of time.gmtime(0)) 
current_time = time.time() 
print(current_time)

# Sleep for 2 seconds 
time.sleep(2) 

# Measure time interval 
start_time = time.time() 
# Some code execution 
end_time = time.time() 
print(f"Elapsed time: {end_time - start_time} seconds") 
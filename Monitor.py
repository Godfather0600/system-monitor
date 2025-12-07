import psutil
import os
import time

while True:
  #Asks psutil to measure CPU usage over 1 second.
  cpu_usage= psutil.cpu_percent(interval=1)
  # Gets a structure containing information about total, used, and free RAM.
  mem = psutil.virtual_memory()
  #Extracts the percentage of RAM currently used.
  mem_usage = mem.percent
  #This gives you the total number of running processes
  process_count = len(psutil.pids())
  #Clears the terminal window each loop.
  os.system("cls" if os.name == 'nt' else 'clear')

  print(f"CPU Usage   : {cpu_usage:.2f} %")
  print(f"Memory Usage: {mem_usage:.2f} %")
  print(f"Processes : {process_count}")





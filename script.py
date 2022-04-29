# Sample script for some threat hunting 
import os, time

name = os.popen('whoami').read() # Who am I? 
netstat = os.popen("netstat -n").readlines() # Acquiring some information on the network
hostname = "www.google.com" 
result = os.system("ping " + hostname) # Testing If the C2 server is reachable

print("You are pwned! :)")
print(name)
print(netstat)
print(result)

time.sleep(120)
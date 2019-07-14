# Program to take a break every <no. of minutes> 

import time
import webbrowser
total_breaks = 3
count = 1

while count <= total_breaks:
    time.sleep(5)
    print("This video started on " +time.ctime())
    webbrowser.open("https://www.youtube.com/watch?v=atVof3pjT-I")
    count = count + 1
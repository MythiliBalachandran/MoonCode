# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
#import matplotlib.pyplot as plt
import webbrowser

bio_data = pd.read_csv('/Users/91949/Downloads/temperature_reading - temperature_reading.csv')
print(bio_data.head(4))
# x = bio_data['Time']
#y = bio_data['temp']
#plt.xlabel('Time')
#plt.ylabel('temp')
#plt.plot(x,y)
#plt.show()
f = open("index.html" , "w")
message='''
<html>
<head>
<link rel="stylesheet" href="style.css" >
<title>Temperature-time graph</title>
</head>
<body>
    <div class="container">
         <div class="chart">
             <canvas id="linechart" width="1100" height= "1100"></canvas>
         </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js" integrity="sha512-M7nHCiNUOwFt6Us3r8alutZLm9qMt4s9951uo8jqO4UwJ1hziseL6O3ndFyigx6+LREfZqnhHxYjKRJ8ZQ69DQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="chart.js"></script>   
    
</body>

</html>
'''

f.write(message)
f.close()
webbrowser.open_new_tab("index.html")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

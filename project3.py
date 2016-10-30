import urllib.request
import csv
import codecs
import numpy as np
import matplotlib.pyplot as plt


url = "http://earthquake.usgs.gov/fdsnws/event/1/query?format=csv" \
      "&starttime=2016-07-25&endtime=2016-10-25&longitude=-118.2437" \
      "&latitude=34.0522&maxradius=.2"
response = urllib.request.urlopen(url)
csv_file = csv.reader(codecs.iterdecode(response, 'utf-8'))
magnitude = []
for line in csv_file:
    magnitude.append(line[4])
magnitude.pop(0)
ints = np.array(magnitude).astype(float)
quake_count = len(magnitude)

plt.xlabel('Magnitude')
plt.ylabel('Number of Earthquakes')
plt.title('Number of recent earthquakes')
plt.hist(x=ints)
plt.show()

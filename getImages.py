import csv
import urllib

pobres = open('/Users/rodolfoocampo/Documents/MachineLearning/Projects/PrediccionDePobrezaSatelital/urban_poor.csv', 'rb')

#contsruir url

coord = []

for row in pobres:
    coord.append(row.strip())

for i in range(len(coord)):
    coord_actual = coord[i]
    coord_actual = str(coord_actual)
    coord_actual = coord_actual[1:-1]
    url = "https://maps.googleapis.com/maps/api/staticmap?center=" + coord_actual + "&zoom=18&size=600x300&maptype=satellite&format=jpg&markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318&markers=color:red%7Clabel:C%7C40.718217,-73.998284&key=AIzaSyBti_8tHi_dyAx3HWCC1Ri811eBq1B7xP4"
    num = str(i)
    file_name = "/Users/rodolfoocampo/tf_files/satPhotos/urban_poor" + "grid_poor" + num + ".jpg"
    urllib.urlretrieve(url, file_name)

no_pobres = open('/Users/rodolfoocampo/Documents/MachineLearning/Projects/PrediccionDePobrezaSatelital/not_poor.csv', 'rb')

#contsruir url

coordp = []

for row in no_pobres:
    coordp.append(row.strip())

for i in range(len(coordp)):
    coord_actual = coordp[i]
    coord_actual = str(coord_actual)
    coord_actual = coord_actual[1:-1]
    url = "https://maps.googleapis.com/maps/api/staticmap?center=" + coord_actual + "&zoom=18&size=600x300&maptype=satellite&format=jpg&markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318&markers=color:red%7Clabel:C%7C40.718217,-73.998284&key=AIzaSyBti_8tHi_dyAx3HWCC1Ri811eBq1B7xP4"
    num = str(i)
    file_name = "/Users/rodolfoocampo/tf_files/satPhotos/not_urban_poor/" + "grid_notpoor" + num + ".jpg"
    urllib.urlretrieve(url, file_name)

print "Success"
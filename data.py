import pickle
import shelve

data = {'PH4':4.0, 'PH7':7.0, 'ADC7': 2048.0, 'ADC4': 1270.0}

filename = "conf_data"

fileObject = open(filename, 'wb')
pickle.dump(data, fileObject)
fileObject.close()

fileObject = open (filename, 'r')
data = pickle.load(fileObject)
print data

data ['ADC4']=1280.0

fileObject = open(filename, 'wb')
pickle.dump(data, fileObject)
fileObject.close()

fileObject = open (filename, 'r')
data = pickle.load(fileObject)
print data



s = shelve.open('test_shelf.db')
try:
    s['key1'] = { 'int': 10, 'float':9.5, 'string':'Sample data' }
finally:
    s.close()

s = shelve.open('test_shelf.db')
try:
    existing = s['key1']
finally:
    s.close()

print existing




file = "var_data"

f = open(file, 'r')

data = f.read()
print data
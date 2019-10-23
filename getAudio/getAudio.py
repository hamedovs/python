import csv
import urllib.request

AudioUrl = 'https://ssl.gstatic.com/dictionary/static/sounds/oxford/--_gb_1.mp3'
LocalPath = r'C:\Users\hamed\Desktop\word.mp3'

inF = open(r"C:\Users\hamed\Desktop\words.csv")
reader = csv.reader(inF)
for row in reader:
    NewUrl = AudioUrl.replace('--', row[0] + '--')
    NewLocalPath = LocalPath.replace('word', row[0])
    urllib.request.urlretrieve(NewUrl, NewLocalPath)

print('All files have been downloaded successfully!')

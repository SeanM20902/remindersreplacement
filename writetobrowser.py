import readTODO
import webbrowser
# write to (crude) HTML and open in local browser
# may udpate later w nicer looking css

data = readTODO.readtodo()
raw_string_data = ''
i = 0
for classname in data:
	if classname in readTODO.getclasslist():
		raw_string_data += classname
		raw_string_data += '<br>'
	if data[classname] == []:
		raw_string_data += '<br/>'
	else:
		raw_string_data += '<ul>'
		for item in data[classname]:
			raw_string_data += '<li>'
			raw_string_data += item[0]
		if i < len(data)-1:
			raw_string_data += '<br/>'
		raw_string_data += '</ul>'
	i+=1

with open('HTMLdata.html', 'r+') as f:
	f.truncate(0)
	f.write(f'<html>\n <body> <h1 style = "font-size: 100">TODO</h1>\n \
           <h2 style = "font-size: 75"> {raw_string_data} </h2>\n</body></html>')

url = 'C:\\Users\\Sean\\TODO_proj\\remindersreplacement\\HTMLdata.html'
webbrowser.open(url, new = 2)
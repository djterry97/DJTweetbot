# http://www.gutenberg.org/cache/epub/<num>/pg<num>.txt

import requests as r
i = 10
for i in range(1,60000):
    source = 'http://www.gutenberg.org/cache/epub/'+str(i)+'/pg'+str(i)+'.txt'
    page = r.get(source)
    if page.status_code == 200:
        print('Writing ' + str(i) + ' to \source\...')
        text = page.text
        file = 'sources\\' + str(i) + '.txt'
        book = open(file, 'wb')
        for chunk in page.iter_content(100000):
            book.write(chunk)
        book.close()
    else:
        print(str(i) + ' unavailable.')
        continue


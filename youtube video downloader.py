#this command will import pytube module
import pytube

#let us now create a variable to take input of youtube link
link = input('Enter Youtube Video URL')
#now,let us start process to download the youtube video
yt = pytube.YouTube(link)
yt.streams.first().download()
#after all things done, the command will show 'downloaded'
print('Downloaded',link)
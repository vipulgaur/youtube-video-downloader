
# coding: utf-8

# In[44]:


import pytube

print("\n-----------------------------\nYOUTUBE VIDEO DOWNLOADER\n-----------------------------\n")

link=input("Enter youtube URL here :>>")
location=input("Enter Download Location: >>")
location=location.replace("\\","\\")
print("\n-------------------\nHold On...Processing Video\n-------------------\n")
file=pytube.YouTube(link)
video=file.streams.first()
filename=video.default_filename
print("\n-------------------\nFilename: ",filename ," \n-------------------\n")
print("\n-------------------\nDownloading..!! Be Patient..!!\n-------------------\n")
video.download(output_path=location, filename=filename)
print("\n-------------------\nOolala..! Video Downloaded @", location,"\n-------------------\n")




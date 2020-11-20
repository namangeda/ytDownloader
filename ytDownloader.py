#a program to download youtube videos
"""
    *****                                
         author : naman geda
         time created : 17/11/2020, 23:58
                                         ******
"""                                         
from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=Gh3BRfXwmsE")   #enter the link of video that you want to download
print(yt.title)


stream = yt.streams.filter(progressive=True).all()

print(stream)                                          #printing all the streams that has both audio and video, to help you select appropriate itag number to fill in next line




""""
      ----------
                necessary - comment down all the code below it first , so that only upper code will be executed ,
                            this way you will find appropriate itag number .
                            once you find it fill it in the next line , then execute full code.
                                      
                                                                                                ----------
"""



"""see the tag number from above printed stream and fill here ,
it is basically picking up what resolution
you want, diffrent itag number may has diffrent
resolution size,
coz it differs from video to video so you have to
maually enter it every time a new video arrives
i choose 18 according to prefrence of resolution which is 360 in this case,
maximum resolution allowed is 720"""
d_stream = yt.streams.get_by_itag('18')  


print("downloading video .....")
d_stream.download()                          # by defult this saves video in the directory where this code is saved,  to change it simply put the path inside download('put path here')
print("video is downloaded")



#saving subtitles if available
try:
    print(yt.captions.all)
    caption = yt.captions.get_by_language_code('en')     #getting only the subtitle in english language 
    subtitle = caption.generate_srt_captions()
    file = open("subtitle for this video.txt", "w+")   #creating subtitle file in the directory where this code is saved
    file.write(str(subtitle))
    file.close()
    print("subtitles are saved")
except:
    print("english subtitles not found")

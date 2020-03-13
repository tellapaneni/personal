from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=UKbrwPL3wXE")
yt = yt.streams.first().download('C:\\Users\\ptellapaneni\\Desktop\\Amit_Project\\Videos')
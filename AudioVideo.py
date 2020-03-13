import moviepy.editor

video = moviepy.editor.VideoFileClip("C:\\Users\\ptellapaneni\\Desktop\\SequencingGenome.mp4")
# audioclip = video.audio.write_audiofile("C:\\Users\\ptellapaneni\\Desktop\\SequencingGenome.mp3")
audioclip = moviepy.editor.AudioFileClip("C:\\Users\\ptellapaneni\\Desktop\\SequencingGenome.mp3")
audioclip = audioclip.set_duration(20)
audioclip1 = audioclip.write_audiofile("C:\\Users\\ptellapaneni\\Desktop\\SequencingGenome1.mp3")
video = video.set_audio(audioclip1)
video = video.write_videofile("C:\\Users\\ptellapaneni\\Desktop\\SequencingGenome1.mp4")
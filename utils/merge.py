from moviepy.editor import VideoFileClip, concatenate_videoclips


clip_1 = VideoFileClip("gifs\what.gif")
clip_2 = VideoFileClip("gifs\your.gif")
clip_3 = VideoFileClip("gifs\\name.gif")
final_clip = concatenate_videoclips([clip_1,clip_2,clip_3])
final_clip.write_videofile("final.mp4")
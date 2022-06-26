from moviepy.editor import VideoFileClip, concatenate_videoclips


clip_1 = VideoFileClip("final.mp4")
# clip_2 = VideoFileClip("ASL_Sign\letters\\a.mp4")
# clip_3 = VideoFileClip("ASL_Sign\letters\\r.mp4")
# clip_4 = VideoFileClip("ASL_Sign\letters\e.mp4")
clip_5 = VideoFileClip("you.mp4")
final_clip = concatenate_videoclips([clip_1,clip_5])
final_clip.write_videofile("final.mp4")
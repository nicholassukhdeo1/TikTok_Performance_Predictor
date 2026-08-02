
# this will read the file into the text
# variable
with open("Posts.txt") as f:
    text = f.read()

# sanity check to make sure it read
# print(len(text))


# so right now, text is one huge
# block of text
# we can split it up appropriately
# per video by finding where the
# newlines are, bc thats what
# each vid's data is split by
# in the source data.
blocks = text.split("\n\n")

# sanity check
# print(len(blocks))



def parse_block(block):
    video = {}
    for line in block.split("\n"):
        if ": " in line:

            # take this line, and split it into
            # the relevant field, and split once (maxsplit)
            # and execute the split at the colon.

            #split returns a list of however many
            #things are applicable to the splitting!
            field, value = line.split(": ", 1)
            video[field] = value
    return video

videos = []
for block in blocks:
    videos.append(parse_block(block))

clean_videos = []
for video in videos:
    clean_videos.append({
        "date": video["Date"],
        "likes": int(video["Like(s)"]),
        "views": int(video["Views"]),
        "sound": video["Sound"],
    })

print(clean_videos[0])

import pandas as pd

df = pd.DataFrame(clean_videos)
df.to_csv("tiktok_data.csv", index=False)
print(df.head())


# print(len(videos))
# print(videos[0])
playlist = {
  "title": "Jan 2022",
  "author": "yodkwtf",
  "songs": [
    {"title": "song1", "artist": ['blue'], "duration": 2.5},
    {"title": "song2", "artist": ['kitty', 'djcat'], "duration": 3.25},
    {"title": "song3", "artist": ['garfield'], "duration": 2}
  ]
}

# calculate the total duration of the playlist
total_len = 0

for song in playlist["songs"]:
  total_len += song.get("duration")

print(total_len)
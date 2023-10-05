
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import json
import time
import logging


#  Kat's client ID obtained from Spotify devilopers website
client_id = 'client id goes here'
client_secret = 'client secret goes here'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

# record start time
start = time.time()
print(start)

#create function to get track info
def get_track_info(artist, track):  
    #  Call spotify API to get info on artist and song
    track_info = sp.search(q="artist:" + artist + " track:" + track, type="track")
    
    #  Artist Info
    artist_info=sp.search(q="artist:" + artist, type="artist")

    # Get length to check to see if the "items" key is empty
    track_len=len(track_info['tracks']['items'])
    artist_len=len(artist_info['artists']['items'])
    
    # Get Artist Genres
    if artist_len>0:
        artist_gen=artist_info["artists"]["items"][0]["genres"]
    else:
        artist_gen=''
    
    #  Get track and artist information if data available
    if track_len>0:
        # Get Track Id
        track_id = track_info["tracks"]["items"][0]["id"]
        
        # Get Danceability
        audio=sp.audio_features(track_id)

        if audio[0] is not None:
            track_dance=audio[0]['danceability']
        else:
            track_dance=''
        
        # Info to return to update history file
        
        update["track_id"]=track_id
        update["danceability"]=track_dance
        update["artist_gen"]=artist_gen
        #print(update)
        return update
    else:                           #If no info in items, leave data empty
        
        update["track_id"]=''
        update["danceability"]=''
        update["artist_gen"]=artist_gen
        return update
    
# Set variables to empty and count to 0
artist=''
track=''
count=0
update = dict();

#  Open json file that has history 
with open('Melissahistory1 update 12.json', 'r') as openfile:
    json_object=json.load(openfile)


#  Begin parse through each object and get artist and track names
#[9278:len(json_object)]
for i in json_object:
    #pause loop to reduce API calls in 30 second window
    time.sleep(0.5)
    # open try statement
    
    try:
        #  Assign artist and track names
        artist=i["artistName"]

        track=i["trackName"]

        #  Call function to get track information
        file_update=get_track_info(artist, track)
        
        #update object
        i.update(file_update)
        count=count+1       
    
    except Exception as e: # work on python 2.x
        logging.error('Exception encountered: '+ str(e))
        break

with open('Melissahistory1 update 12.json', 'w') as closefile:
    closefile.write(json.dumps(json_object))

# record end time
end = time.time()
 
# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")



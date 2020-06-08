import sys
import spotipy
import spotipy.util as util


scope = 'user-library-modify playlist-read-private playlist-read-collaborative'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

offsets = list(range(6))

if token:
    ids = []
    tracks = []
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_playlists()
    for item in results['items']:
        if username in item['owner']['id']:
            list_id = item['id']
            ids += [list_id]
    for thing in ids:
        for offset in offsets:
            results = sp.playlist_tracks(thing, offset=offset*100)
            for item in results['items']:
                tracks += [item['track']['uri']]
    tracks = list(dict.fromkeys(tracks))
    for track in tracks:
        print(f"Adding track with ID {track}")
        try:
            sp.current_user_saved_tracks_add(tracks=[track])
        except Exception as e:
            print(e)
            continue
else:
    print("Can't get token for", username)
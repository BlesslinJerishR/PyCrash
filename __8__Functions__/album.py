# 8.7
def make_album(artist_name, album_title, no_of_songs=None):
    album = {
        'Artist': artist_name,
        'Album': album_title,
    }
    if no_of_songs:
        album['Songs'] = no_of_songs
    return album


album = make_album('HipHop Tamizha', 'Na oru alien')
print(album)
album = make_album('HipHop Tamizha', 'Na oru alien', 6)
print(album)


def make_album():
    album_build = True
    while album_build:
        print("Enter 'quit' or 'q' anywhere to exit")
        artist_name = input('What is the name of the artist ? ')
        if artist_name == 'quit' or artist_name == 'q':
            break
        album_title = input('What is the name of the Album ? ')
        if album_title == 'quit' or album_title == 'q':
            break
        songs_no = input('How many songs in that album ? ')
        if songs_no == 'quit' or songs_no == 'q':
            break
        albums = {
            'Artist': artist_name,
            'Album': album_title,
            'Songs': songs_no,
        }
        return albums


albumn = make_album()
print(albumn)

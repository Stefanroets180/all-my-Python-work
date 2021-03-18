def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('metallica', 'black')
print(album)

album = make_album('blink-182', 'nine')
print(album)

album = make_album('the black keys ', 'lets rock')
print(album)

album = make_album('tool', 'fear inoculum ', tracks=10)
print(album)
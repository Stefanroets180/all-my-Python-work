def make_album(artist_name, *album_title, number_of_tracks=''):
    """Make album from informations passed to function."""

    album = {'artist': artist_name, 'album': album_title}

    if number_of_tracks:
        album['n_tracks'] = number_of_tracks
    return album
 

# Infinite loop
while True:
    from make_album import make_album
    print("\nEnter Album's information:")
    print("(enter 'q' at any time to quit)")

    a_name = input("Enter artist_name: ")
    if a_name == 'q':
        break

    a_title = input("Enter album title: ")
    if a_title == 'q':
        break

    n_tracks = input("Enter the number of tracks (Optional): ")
    if n_tracks == 'q':
        break

    album = make_album(a_name, a_title, n_tracks)
    print(album)
import random

class MusicSelector:
    def __init__(self, music_library):
        self.music_library = music_library

    def select_random_music(self):
        return random.choice(self.music_library)

    def select_by_genre(self, genre):
        genre_songs = [song for song in self.music_library if song['genre'] == genre]
        if genre_songs:
            return random.choice(genre_songs)
        else:
            return None

# Example usage:

# Define a music library as a list of dictionaries, each representing a song with its title, artist, and genre.
music_library = [
    {'title': 'Song 1', 'artist': 'Artist 1', 'genre': 'Pop'},
    {'title': 'Song 2', 'artist': 'Artist 2', 'genre': 'Rock'},
    {'title': 'Song 3', 'artist': 'Artist 3', 'genre': 'Pop'},
    {'title': 'Song 4', 'artist': 'Artist 4', 'genre': 'Jazz'},
    {'title': 'Song 5', 'artist': 'Artist 5', 'genre': 'Rock'},
]

# Create a MusicSelector instance with the music library
selector = MusicSelector(music_library)

# Select a random song from the music library
random_song = selector.select_random_music()
print("Random Song:", random_song)

# Select a random song from a specific genre, for example, 'Rock'
rock_song = selector.select_by_genre('Rock')
print("Rock Song:", rock_song)

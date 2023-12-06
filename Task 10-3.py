class PlaylistManager:
    def __init__(self):
        self.playlists = []

    def create_playlist(self, name, genre):
        playlist = Playlist(name, genre)
        self.playlists.append(playlist)
        return playlist

    def search_audio(self, audio_name):
        results = []
        for playlist in self.playlists:
            results.extend(playlist.search_audio(audio_name))
        return results

    def search_playlist(self, playlist_name):
        for playlist in self.playlists:
            if playlist.name == playlist_name:
                return playlist
        return None


class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.audio_files = []
        self.ratings = []

    def add_audio(self, audio_name):
        audio = Audio(audio_name)
        self.audio_files.append(audio)
        return audio

    def search_audio(self, audio_name):
        results = []
        for audio in self.audio_files:
            if audio.name.lower() == audio_name.lower():
                results.append(audio)
        return results

    def add_rating(self, rating):
        self.ratings.append(rating)

    def get_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)


class Audio:
    def __init__(self, name):
        self.name = name
        self.rating = None

    def add_rating(self, rating):
        self.rating = rating


# Example usage:

playlist_manager = PlaylistManager()

# Create playlists
rock_playlist = playlist_manager.create_playlist("Rock Hits", "Rock")
pop_playlist = playlist_manager.create_playlist("Pop Favorites", "Pop")

# Add audio files to playlists
rock_playlist.add_audio("Stairway to Heaven")
rock_playlist.add_audio("Bohemian Rhapsody")
pop_playlist.add_audio("Shape of You")
pop_playlist.add_audio("Uptown Funk")

# Search for audio
search_results = playlist_manager.search_audio("Bohemian Rhapsody")
print("Search Results:", [audio.name for audio in search_results])

# Search for playlist
found_playlist = playlist_manager.search_playlist("Rock Hits")
if found_playlist:
    print("Found Playlist:", found_playlist.name)
else:
    print("Playlist not found")

# Rate playlists and audio
rock_playlist.add_rating(4)
pop_playlist.add_rating(5)
rock_playlist.audio_files[0].add_rating(5)

# Display average ratings
print("Average Rating for Rock Hits:", rock_playlist.get_average_rating())
print("Average Rating for Pop Favorites:", pop_playlist.get_average_rating())

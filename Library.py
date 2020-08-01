class Item:
    def __init__(self, title, isbn):
        self.title = title
        self.ISBN = isbn

    def getinfo(self):
        print("Title: " + self.title + "\n" + "ISBN: " + self.ISBN)


class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def getinfo(self):
        artists = ', '.join(map(str, self.artist))
        print(artists + " - " + self.title + ", duration: " + self.duration)


class Media(Item):
    def __init__(self, title, isbn, tracks, year):
        super().__init__(title, isbn)
        self.tracks = tracks
        self.year = year

    def gettracklist(self):
        for track in self.tracks:
            track.getinfo()


class Video(Media):
    def __init__(self, title, isbn, tracks, year, tech):
        super().__init__(title, isbn, tracks, year)
        self.technology = tech


class VideoFile:
    def __init__(self, video, canDownload):
        self.video = video
        self.canDownload = canDownload

    def download(self, type):
        if self.canDownload:
            # few examples
            if type == 'AVI':
                print(self.video.title + ".avi")
            elif type == 'MOV':
                print(self.video.title + ".mov")
            elif type == 'MP4':
                print(self.video.title + ".mp4")
            else:
                print("Format not supported.")
        else:
            print("This video is not available for download.")


t1 = Track("Angel Eyes", {"ABBA"}, "4:22")

t2 = Track("Heroes", {"David Bowie", "Queen"}, "6:06")

dvd = Video("Best Hits", "1234", [t1, t2], 2020, "DVD")
dvd.gettracklist()

vf = VideoFile(dvd, True)
vf.download("MOV")
vf.download("MP3")

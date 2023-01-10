import sqlite3

class Model:
    _connect = None
    _cursor = None

    def __init__(self):
        self._connect = sqlite3.connect('DisturbedDscography.db')
        self._cursor = self._connect.cursor()

    def getTrackListSQL(self, album_title):
        table = [["Title", "Time"]]
        sql = '''
SELECT 
Tracks.Title,
Tracks.LenTrack
FROM Tracks INNER JOIN Albums
ON Tracks.ID_Album = Albums.ID
WHERE Albums.Title = ?;
'''
        for row in self._cursor.execute(sql, [album_title]):
            line = []
            for colum in row:
                line.append(colum)
                table.append(line)
                return table

    def getAlbumsSQL(self):
            table = []
            for row in self._cursor.execute("SELECT Title FROM Albums;"):
                line = ''
                for colum in row:
                    line += colum
                table.append(line)

            return table

def getImage(self, name):
    return 'cover\\' + name + '.jpg'
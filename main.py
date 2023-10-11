from moisesdb.dataset import MoisesDB

db = MoisesDB(
    data_path='./moisesdb',
    sample_rate=44100
)

n_songs = len(db)
track = db[0]
stems = track.stems
print(stems.keys())
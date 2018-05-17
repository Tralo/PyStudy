# coding:utf-8
import requests
import io
import tarfile

if __name__ == '__main__':
    movie_data_url = "http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz"
    r = requests.get(movie_data_url)
    stream_data = io.BytesIO(r.content)
    tmp = io.BytesIO()
    while True:
        s = stream_data.read(16384)
        if not s:
            break
        tmp.write(s)
    stream_data.close()
    tmp.seek(0)
    tar_file = tarfile.open(fileobj=tmp, mode="r:gz")
    pos = tar_file.extractfile('rt-polaritydata/rt-polarity.pos')
    neg = tar_file.extractfile('rt-polaritydata/rt-polarity.neg')
    pos_data = []
    for line in pos:
        pos_data.append(line.decode('ISO-8859-1').encode('ascii', errors='ignore').decode())
    neg_data = []
    for line in neg:
        neg_data.append(line.decode('ISO-8859-1').encode('ascii', errors='ignore').decode())
    tar_file.close()
    print(len(pos_data))
    print(len(neg_data))
    print(neg_data[0])



import requests
#import qbittorent

movie_name = input("Enter movie name: ")
r = requests.get(url = "https://yts.mx/api/v2/list_movies.json",params={"query_term":movie_name,"limit":50})
jsonapi = r.json()
movie_count=jsonapi['data']['movie_count']
for i in range(min(movie_count,50)):
    print(i+1,"\t",jsonapi['data']['movies'][i]['title_long'])
movie_number = int(input('Enter movie number: '))
i=0
for torrent in jsonapi['data']['movies'][movie_number-1]['torrents']:
    print(i+1,'\t',torrent['quality'],torrent['type'])
    i+=1
movie_quality = int(input('Enter quality: '))
MOVIE_NAME=''
TORRENT_HASH=jsonapi['data']['movies'][movie_number-1]['torrents'][movie_quality-1]['hash']
str=jsonapi['data']['movies'][movie_number-1]['title']+' %28'+str(jsonapi['data']['movies'][movie_number-1]['year'])+'%29+%5B'+jsonapi['data']['movies'][movie_number-1]['torrents'][movie_quality-1]['quality']+'%5D'
for k in range(len(str)):
    char=str[k]
    if char==' ':
        MOVIE_NAME+='+'
    else:
        MOVIE_NAME+=char
magnet_link='magnet:?xt=urn:btih:'+TORRENT_HASH+'&dn='+MOVIE_NAME+'&tr=udp://open.demonii.com:1337/announce&tr=udp://tracker.openbittorrent.com:80&tr=udp://tracker.coppersurfer.tk:6969&tr=udp://glotorrents.pw:6969/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=udp://torrent.gresille.org:80/announce&tr=udp://p4p.arenabg.com:1337&tr=udp://tracker.leechers-paradise.org:6969'
#qb = Client('http://127.0.0.1:8080/')
#qb.download_from_link(magnet_link)
print(magnet_link)
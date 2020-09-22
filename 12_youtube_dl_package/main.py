import youtube_dl

ydl_opt = {
    #'listformats': True, # 다운로드 가능한 모든 포맷 가능
    # 가장 아래쪽에 (best)에 인덱스 번호를 지정하기
    #'format': '18',
    # 베스트 해상도 선택
    #'format': 'best[height<=480]',
    # 베스트 파일 사이즈 선택
    'format': "[filesize<10M]",
    # 다운로드 받을 때 파일의 이름을 자동으로 변경
    'outtmpl': '%(title)s %(resolutions)s.%(ext)s'

}


with youtube_dl.YoutubeDL(ydl_opt) as ydl: # YoutubeDL 객체 생성 --> ydl로 명명
    ydl.download(['https://www.youtube.com/watch?v=GkGjk7OPO78'])



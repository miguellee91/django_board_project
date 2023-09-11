from django.db import models
from datetime import datetime
from django.db import models

# Create your models here.
class Board(models.Model):
    idx = models.AutoField(primary_key=True) #고유 pk 식별자 자동 증가 정수형
    writer = models.CharField(null=False, max_length=50) #작성자
    title = models.CharField(null=False, max_length=200) #제목
    hit = models.IntegerField(default=0) #조회수
    content = models.TextField(null=False) #내용
    post_date = models.DateTimeField(default=datetime.now(), blank=True) #작성일
    filename = models.CharField(null=True,blank=True, default="", max_length=500) #파일이름
    filesize = models.IntegerField(default=0) #파일사이즈
    down = models.IntegerField(default=0) # 다운수

#게시물 조회수를 증가시키는 메서드
    def hit_up(self):
        self.hit += 1
#파일 다운로드 횟수를 증가시키는 메서드
    def down_up(self):
        self.down += 1

#댓글 테이블
class Comment(models.Model):
    #댓글 글번호
    idx = models.AutoField(primary_key=True)
    #게시물 번호
    board_idx = models.IntegerField(null=False)
    writer = models.CharField(null=False,max_length=50)
    content = models.TextField(null=False)
    post_date = models.DateTimeField(default=datetime.now,blank=True)
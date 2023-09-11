from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from board.models import Board


# Create your views here.

def register(request):
    return render(request, "board/register.html")
def list(request):
    boardCount= Board.objects.count()
    boardList= Board.objects.all().order_by("-idx")
    return render(request,"board/list.html",
    {"boardList":boardList, "boardCount":boardCount})


#파일 업로드를 처리
UPLOAD_DIR='c:/Temp/'
@csrf_exempt               #Cross Site Request Forger
def insert(request):
    fname = ''
    fsize = 0
    if 'file' in request.FILES: # HTTP 요청에 'file'이라는 이름의 파일이 첨부되었는지 확인
        file = request.FILES['file'] #HTTP 요청에서 업로드된 파일을 가져옴
        fname = file.name
        fsize = file.size
        fp = open('%s%s' %(UPLOAD_DIR,fname),'wb') #업로드된 파일을 저장할 경로와 파일 이름을 조합하여 파일을 열고, 이진 쓰기 모드('wb')로 파일 열기
        for chunk in file.chunks(): #업로드된 파일을 여러 청크(chunk)로 나눠서 처리
            fp.write(chunk) #디스크에 저장
        fp.close()
    #파일 업로드와 함께 게시물 정보를 받아서 Board 모델을 사용하여 데이터베이스에 저장할 데이터 객체를 생성
    dto=Board(writer=request.POST['writer'], title=request.POST['title'],
        content=request.POST['content'], filename=fname, filesize=fsize)
    dto.save() #데이터베이스에 새로운 데이터 객체를 저장
    print(dto)
    return redirect('/list/')
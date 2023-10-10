from django.shortcuts import render

from board_app.form import DataForm

# Create your views here.
def show_board(request):
    return render(request, 'board_app/board.html') 

def data_form(request):
    # POST 방식으로 전달되었는지 확인 후 변수에 저장
    writes = []

    if request.method == "POST":
        # print(request.POST) # <QueryDict: {'csrfmiddlewaretoken': ['6IgwTtPd3PbMo1fmmy78CejnubpdTGJVAg7Ig0qLCVQaQE9CSfEV0ZFiMHGLxVq2'], 'name': ['22'], 'age': ['33'], 'addr': ['33']}>
        title = request.POST['title']
        body = request.POST['body']
        writes = [{'title':title, 'body':body}]

        return render(request, 'board_app/board_result.html', {'writes':writes})
    else:
        return render(request, 'board_app/board_form.html')
    

def data_form2(request):
    # POST 방식으로 전달되었는지 확인 후 변수에 저장
    writes = []
    form = DataForm

    if request.method == "POST":
        form = DataForm(request.POST)
        print(request.POST.get('title', None))

        if form.is_valid():
            title = request.POST.get('title', None)
            body = request.POST.get('body', None)
            writes = [{'title':title, 'body':body}]
            #index 페이지로 포워딩 : redirect
            return render(request, 'board_app/board_result.html', {'writes':writes})

    else:
        return render(request, 'board_app/board_form2.html', {'form':form}) 
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
# Create your views here.
def index(request):
    myname = "Nguyen Van Hai"
    taisan = ["Điện thoại", "Đồng hồ"]

    context = \
    {
        "name":myname,
        "taisan":taisan
    }
    return render(request, "polls/index.html", context)
def test(request):
    return HttpResponse("<h1>Linh Tinh</h1>")

def question_list(request):
    list_question = Question.objects.all()
    context = \
    {
        "list_question":list_question
    }
    return render(request, "polls/question_list.html", context)

def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, "polls/detail_question.html", {'q':q})

def getQuestionById(request, question_id):
    q = Question(question_id)
    return render(request, "polls/getQuestionById.html", {'q':q})

# Login:
def getLoginForm(request):
    return render(request, "users/getFormLogin.html")
from django.urls import path
from . import views
from polls.Controller.userController import userController
urlpatterns = [
    path('', views.index, name="index"),
    path('test/', views.test, name="test"),
    path('question_list/', views.question_list, name="question_list"),
    path('detail_question/<int:question_id>', views.detailView, name="detail_question"),
    path('getQuestionById/<int:question_id>', views.getQuestionById, name="getQuestionById"),

    # redirect userController
    path('getLoginForm', userController.getLoginForm, name="getLoginForm"),
    path('postLoginForm', userController.postLoginForm, name="postLoginForm"),
]
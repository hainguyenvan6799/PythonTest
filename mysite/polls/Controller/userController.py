from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
class userController:
    def getLoginForm(request):
        return render(request, "users/getFormLogin.html")
    def postLoginForm(request):
        data_user = request.POST["user"]
        data_pass = request.POST["pass"]
        my_user = authenticate(username=data_user, password=data_pass)
        if not(my_user):
            return HttpResponse("User khong ton tai")
        return HttpResponse("Ban vua dang nhap thanh cong")


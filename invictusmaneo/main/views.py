from django.shortcuts import render, redirect
from .forms import LogForm, RegForm
from .models import *

Current_user = []
question_id = 1
def Main(request):
    return render(request, "main/Main.html")

def Game(request):
    global question_id

    user = Data.objects.get(id=Current_user[0])
    Audio = Files.objects.get(id=question_id)
    question = Questions.objects.get(id=question_id)
    images = Images.objects.get(id=question_id)
    context = {
        "el": user,
        "aud": Audio,
        "que": question,
        'im': images,
        'count_id': question_id
    }
    question_id += 1
    if question_id == 11: question_id = 1

    return render(request, "main/game.html", context)



def authorization(request):
    global Current_user
    error = ''
    if request.method == 'POST':
        form = LogForm(request.POST)
        if Data.objects.filter(login=form.data["login"], password=form.data["password"]).exists() and form.is_valid():
            result = Data.objects.get(login=form.data["login"], password=form.data["password"])
            Current_user = []
            current_user_array = [result.id, form.data["login"], form.data["password"]]
            Current_user.extend(current_user_array)
            return redirect("game")
        else:
            error = "Данный пользователь не существует"
    context = {
        "form": LogForm(),
        "error": error
    }
    return render(request, "main/authorization.html", context)

def registration(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("author")
    form = RegForm()
    context = {
        "form": form
    }
    return render(request, "main/registration.html", context)




# Create your views here.

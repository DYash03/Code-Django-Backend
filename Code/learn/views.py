from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from . models import Contact, Editor, Technologies
from django.db.models import Max
# Create your views here.


def home(request):
    return render(request, "learn/index.html")


def tech_list(request):
    technology = Technologies.objects.all()
    MaxView = Technologies.objects.aggregate(Max('views'))[
        'views__max']
    maxvw = Technologies.objects.all().filter(views=MaxView)
    techno = {"tech": technology, "maxvw": maxvw}
    return render(request, "learn/tech_list.html", techno)


def editor(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        program_name = request.POST.get('pname', '')
        source = request.POST.get('source', '')
        email = request.POST.get('email', '')
        description = request.POST.get('desc', '')
        solution = request.POST.get('sol', '')
        Input = request.POST.get('si', '')
        Output = request.POST.get('so', '')
        if len(name) < 2 or len(program_name) < 5 or len(description) < 20 or len(Input) < 2 or len(Output) < 2:
            messages.error(request, "Please fill the details correctly")
        else:
            edit = Editor(name=name, program_name=program_name, source=source, email=email,
                          description=description, solution=solution, Input=Input, Output=Output)
            edit.save()
            messages.success(request, 'Your response is received.')
    return render(request, "learn/editor.html")


def Contactt(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        mob = request.POST.get('mob', '')
        textarea = request.POST.get('textarea', '')
        if len(name) < 2 or len(mob) < 10 or len(textarea) < 5:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email,
                              mob=mob, textarea=textarea)
            contact.save()
            messages.success(request, 'Your response is received.')
    return render(request, "learn/Contact.html")


def technology(request, slug):
    technology = Technologies.objects.get(slug=slug)
    technology.views = technology.views+1
    technology.save()
    techno = {"tech": technology}
    return render(request, "learn/technology.html", techno)


def About(request):
    return render(request, "learn/About.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['fpassword']
        pass2 = request.POST['cpassword']

        if len(username) > 15:
            messages.error(
                request, "Username must be less than 15  characters.")
            return redirect('/')
        if not username.isalnum():
            messages.error(
                request, "Username must only contain letters and numbers.")
            return redirect('/')
        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect('/')
        user = User.objects.create_user(username, email, pass1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(
            request, 'Your account has been successfully created.')
        return redirect('/')
    else:
        return HttpResponse("404 - Not Found")


def handlelogin(request):
    if request.method == "POST":
        logusername = request.POST['logusername']
        logpassword = request.POST['logpassword']

        user = authenticate(username=logusername, password=logpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In.")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials, Please try again.")
            return redirect('/')
    else:
        return HttpResponse("404 - Not Found")


def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out.")
    return redirect('/')


def search(request):
    search = request.GET['search']
    Tlogy = Technologies.objects.all()
    if len(search) > 50:
        technology = Technologies.objects.none()
    else:
        name = Technologies.objects.filter(blog_name__icontains=search)
        description_1 = Technologies.objects.filter(
            description_1__icontains=search)
        technology = name.union(description_1)
    techno = {"tech": technology, "search": search, "Tlogy": Tlogy}
    return render(request, 'learn/search.html', techno)

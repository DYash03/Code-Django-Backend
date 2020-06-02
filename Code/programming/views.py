from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Program, ProgramComment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from programming.templatetags import extras
# Create your views here.


def pro_list(request):
    prog = Program.objects.all()
    pro = {"program": prog}
    return render(request, "programming/pro_list.html", pro)


def program(request, slug):
    prog = Program.objects.get(slug=slug)
    comments = ProgramComment.objects.filter(program=prog, parent=None)
    replies = ProgramComment.objects.filter(
        program=prog).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    pro = {"program": prog, "comments": comments,
           "user": request.user, "replyDict": replyDict}
    return render(request, "programming/program.html", pro)


def pro_category(request, category):
    prog = Program.objects.all().filter(category=category)
    pro = {"program": prog}
    return render(request, 'programming/category.html', pro)


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Program.objects.get(pro_id=postSno)
        ParentSno = request.POST.get("ParentSno")
        if ParentSno == "":
            comment = ProgramComment(comment=comment, user=user, program=post)
            comment.save()
            messages.success(
                request, "Your comment has been posted successfully.")
        else:
            parent = ProgramComment.objects.get(sno=ParentSno)
            comment = ProgramComment(
                comment=comment, user=user, program=post, parent=parent)
            comment.save()
            messages.success(
                request, "Your reply has been posted successfully.")
    return redirect(f'/programming/{post.slug}')


def deleteComment(request, sno):
    if request.method == 'POST':
        comment = ProgramComment.objects.get(sno=sno)
        post = Program.objects.get(name=comment.program)
        comment.delete()
        messages.success(request, "Comment successfully deleted.")
    return redirect(f'/programming/{post.slug}')

from django.shortcuts import render, redirect
from .models import User, Message, Comment
from django.contrib import messages
import bcrypt
from datetime import datetime


def index(request):
   return render(request, 'main/index.html')

def register(request):
   # checking for validation errors
   print('got in to the register function')
   errors = User.objects.basic_validator(request.POST)
   if len(errors) > 0:
      for key, value in errors.items():
         messages.error(request, value)
      return redirect('/') # redirect to the index route in the case that there are errors

   if request.method == 'POST':
      post = request.POST
      fn = post['firstName']
      ln = post['lastName']
      em = post['email']
      pw_hash = bcrypt.hashpw(post['password'].encode(), bcrypt.gensalt())
      print(pw_hash)
      user = User.objects.create(firstName=fn, lastName=ln, email=em, password=pw_hash)
      user.save()
      print(user)
      request.session['userId'] = user.id
      return redirect('/success')


def login(request):
   user = User.objects.filter(email = request.POST['email']) 
   print(user)
   if len(user) < 1:
      messages.error(request, "You could not be logged in")
      return redirect('/')
   user = user[0]
   if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
      request.session['userId'] = user.id
      return redirect('/success')
   messages.error(request, "Please check your email and password")
   return redirect('/')

def success(request):
   if 'userId' not in request.session:
      return redirect('/')
   messages = Message.objects.all().order_by('created_at')
   print(messages)
   comments = Comment.objects.all().order_by('created_at')
   print(comments)
   user = User.objects.get(id=request.session['userId'])
   # messageTime = datetime.strftime(messages.created_at, "%B %d, %Y")

   context = {
      "messages": messages,
      "user": user,
      "comments": comments,
      # "messageTime": messageTime,
   }
   print(context['messages'])
   return render(request, 'main/profile.html', context)

def create_message(request):
   user = User.objects.get(id=request.session['userId'])
   print("got into method post")
   if request.method == 'POST':
      post = request.POST
      message = post["message"]
      sender = User.objects.get(id=request.session['userId'])
      new_msg = Message.objects.create(content=message, user=sender)
      print(new_msg)
      return redirect('/success')

def create_comment(request):
   user = User.objects.get(id=request.session['userId'])
   print("got into method post")
   if request.method == 'POST':
      post = request.POST
      content = post['comment']
      sender = User.objects.get(id=request.session['userId'])
      message = Message.objects.get(id=request.POST['messageId'])
      new_comment = Comment.objects.create(content=content, message= message, user=sender)
      print(new_comment)
      return redirect('/success')

def logout(request):
   request.session.clear()
   return redirect('/')
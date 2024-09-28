from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from .forms import loginform, UserUpdateForm
from home.models import Login, QueryHistory, User,user
from django.http import JsonResponse
from django.contrib.auth import authenticate,login  

import json
import pyttsx3 #pip install pyttsx3
import datetime
import wikipedia #pip install wikipedia
import pywhatkit as yt
import webbrowser
import os
import random


# Create your views here.
def index(request):
    return render(request, 'index.html')


#__________________________________________________________________#

def about(request):
    return render(request, 'about.html')

#__________________________________________________________________#

def history(request):
    # Retrieve all saved queries, optionally filter by user if needed
    query_history = QueryHistory.objects.all().order_by('-timestamp')
    return render(request, 'history.html', {'history': query_history})

#__________________________________________________________________#

def delete_history(request, id):
    # Fetch the specific history record by its ID
    history_record = get_object_or_404(QueryHistory, id=id)

    # Delete the record
    history_record.delete()

    # Redirect back to the history page after deletion
    return redirect('history')

#__________________________________________________________________#

def userprofile(request):
    return render(request, 'userprofile.html')

#__________________________________________________________________#

def submit_text(request):
    if request.method == 'POST':
        # Parse the incoming JSON data
        data = json.loads(request.body)
        query = data.get('result', '')

        # Save the query in the database
        new_query = QueryHistory(user_email=request.user.email if request.user.is_authenticated else "anonymous", query_text=query)
        new_query.save()

        print(f"Text received: {query}")


        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        # print(voices[1].id)
        engine.setProperty('voice', voices[2].id)


        def speak(audio):
            engine.say(audio)
            engine.runAndWait()


        def wishMe():
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                speak("Good Morning!")

            elif hour>=12 and hour<18:
                speak("Good Afternoon!")   

            else:
                speak("Good Evening!")  
            speak("I am Sabrina Sir. Please tell me how may I help you")

        query=query.lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'youtube' in query:
            speak('Searching youtube...')
            query = query.replace("youtube", "")
            results = yt.playonyt(query)
            speak("oppening youtube")

        elif 'open google' in query:
            speak("open google")
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            speak("Hear you go sir")
            music_dir = 'F:\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            ran=random.randint(1, 500)
            os.startfile(os.path.join(music_dir, songs[ran]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak("Opening Visual Studio Code")
            codePath="C:\\Djando\\pro1\\hello\\templates\\signup.html"
            os.startfile(codePath)

        elif 'thank you' in query:
            speak("The pleasure is all mine")

        elif 'what can you do' in query:
            print("I can be of grate use sir. I can tell you time, play musicfor you, search from wikipedia, And also open youtube and google for you, just say open youtube or google")

        elif 'weather today' in query:
            speak("Today will be mostly clowdy")
        
        elif 'your name' in query:
            speak("My name is Sabrina")

        elif 'what technique ' in query:
            speak("I can use Fire style, Water Style, Earth Style, Wind Style, Thunder Style as you say my master ")

        else:
            speak("Sorry i didnt understand, please repeat")

        # Return a response to the client
        return JsonResponse({'status': 'success', 'received_text': query})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


#__________________________________________________________________#


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')  
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        profile_picture=request.POST.get('profile_photo')
        dob=request.POST.get('dob')
        bio=request.POST.get('bio')
        gender=request.POST.get('gender')
        password = request.POST.get('password')
        if user.objects.filter(username=username).exists() or User.objects.filter(email=email):
            messages.error(request,'Username/Email Already Exists')
            return redirect('register')
        user_ = user.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password,bio=bio,date_of_birth=dob,profile_picture=profile_picture,gender=gender)
        user_.save()
        messages.success(request,'User Created Sucessfully')
        return redirect('login')
    return render(request, 'signup.html')


#__________________________________________________________________#
def Login(request):
    form = loginform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            User = authenticate(request,username=username,password=password)
            if User is not None:
                login(request,User)
                return redirect('home')
            else:
                messages.error(request,'invalid credentials')
        else:
            messages.error(request,'error validating form')
    return render(request, 'login.html',{'form':form})



#__________________________________________________________________#

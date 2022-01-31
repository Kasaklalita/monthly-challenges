from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Work for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "april!",
    "may": "may!",
    "june": "june!",
    "july": "july!",
    "august": "august!",
    "september": "september!",
    "october": "october!",
    "november": "november!",
    "december": "december!"
}

# Create your views here.

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month): #<month> from urls.py
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None
}

# Create your views here.

def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args = [month])
    #     list_items += f'<li><a href = "{month_path}">{capitalized_month}</a></li>'
    #
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args = [redirect_month]) #/challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month): #<month> from urls.py
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        raise Http404()
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)

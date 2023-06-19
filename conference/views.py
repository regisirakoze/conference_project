from django.shortcuts import render
from django.http import HttpResponse
import datetime

conferences = [
        {
            "id": 1,
            "name": "Introduction to AU",
            "date": "2021.07.12",
            "location": "Selena Hotel"
        },
        {
            "id": 2,
            "name": "Meet The President",
            "date": "2023.05.15",
            "location": "Intare Conference Arena"
        },
        {
            "id": 3,
            "name": "Umushyikirano 18",
            "date": "2023-27-02",
            "location": "Gabiro Army Camp"
        },

        {
            "id": 4,
            "name": "Umwiherero 2023",
            "date": "2024-05-05",
            "location": "KCC"
        },

        {
            "id": 5,
            "name": "FIFA Summit 2024",
            "date": "2024-07-01",
            "location": "BK Arena"
        },
    ]
def conferences_view(request):
    return render(request, 'conference_list.html', context={"conferences": conferences})

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

users = [
    {
        'id': 1,
        'name': 'John Doe',
        'email': 'johnDoe2gmail.com',
        'age': 25,
    },
    {
        'id': 2,
        'name': 'Jane Doe',
        'email': 'janeDoe2gmail.com',
        'age': 22,
    },
    {
        'id': 3,
        'name': 'Jim Doe',
        'email': 'jimDoe2gmail.com',
        'age': 23,
    },
    {
        'id': 4,
        'name': 'Jill Doe',
        'email': 'jillDoe2gmail.com',
        'age': 24,
    },
    {
        'id': 5,
        'name': 'Jack Doe',
        'email': 'jackDoe2gmail.com',
        'age': 26,
    },

]

def home(request):
    return HttpResponse('<h1>Welcome to the Home Page</h1>')

def list(request):     
    html = '<h1>Users</h1><ul>'
    for user in users:
        html += f'<li><a href="/users/{user["id"]}/">{user["name"]}</a></li>'
    html += '</ul>'
    return HttpResponse(html)

def detail(request, user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user is None:
        return HttpResponse('<h1>User not found</h1>', status=404)
    return HttpResponse(
        f'<h1>{user["name"]}</h1>'
        f'<p>Email: {user["email"]}</p>'
        f'<p>Age: {user["age"]}</p>'
        f'<a href="/users/list/">Back to list</a>'  
    )
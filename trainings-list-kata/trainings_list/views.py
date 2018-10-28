from django.http import HttpResponse


def index(request):
    response = '<html>'
    response += '<h1>Training list</h1>'
    trainings = [
        {'name': 'TDD'},
        {'name': 'Legacy Code'},
    ]
    for training in trainings:
        response += '<p>' + training['name'] + '</p>'
    response += '</html>'
    return HttpResponse(response)
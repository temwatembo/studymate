# importing functionality from Django
from django.shortcuts import render

#
# views
def frontpage(request):
    return render(request, 'core/frontpage.html')
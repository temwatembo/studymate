# importing functionality from Django
from django.shortcuts import render

#
# views
def frontpage(request):
    return render(request, 'basic/front_page.html')
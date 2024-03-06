from django.shortcuts import render

from django.http import HttpResponse
import io

def generate_image(request):

     return render(request, 'data_plotting/demo.html')

def link_1_view(request):

    return HttpResponse()

def link_2_view(request):

    return HttpResponse()

def link_3_view(request):

    return HttpResponse()

def my_image_view(request):
    # for test only
    image_data = open("path/to/your/image.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

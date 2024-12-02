from django.shortcuts import render,get_object_or_404
from .models import Field
def all_blogs(request):
    fields = Field.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'fields':fields})


def detail(request,blog_id):
    blog = get_object_or_404(Field, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
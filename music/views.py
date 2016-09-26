from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from django.http import Http404

# from django.template import loader

from .models import Album

# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    # template= loader.get_template('music/index.html')
    
    # return HttpResponse(template.render(context, request))
    return render(request, 'music/index.html', {'all_albums': all_albums,})

    # html = ""
    # for album in all_albums:
    #     url ='/music/'+str(album.id)+'/'
    #     html += '<a href=" ' + url + '">'+album.album_title+'</a><br/>'
    # return HttpResponse(html)

def detail(request, album_id):
    # return HttpResponse('<h2>Details for album id:'+str(album_id)+' </h2>')
    # try:
    #     album = Album.objects.get(pk=album_id)
    # except  Album.DoesNotExist:
    #     raise Http404("Album doesnot exist")

    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album,})



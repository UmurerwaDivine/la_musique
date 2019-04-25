from django.shortcuts import render
from . models import Profile,Song
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse,Http404,HttpResponseRedirect

@login_required(login_url='/accounts/login/')
def index(request):
      title = 'own'
      songs =Song.objects.all()
      return render(request,'index.html',{"title":title, "songs":songs})
def search_results(request):

    if 'song' in request.GET and request.GET['song']:
        search_input = request.GET.get('song')
        searched_songs = Song.search_by_artist(search_input)
        message = f"{search_input}"

        return render(request, 'search.html', {"message":message, "songs":searched_songs})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

    
@login_required(login_url='/accounts/login/')
def profile(request):
	 current_user = request.user
	 profile = Profile.objects.all()
	

	 return render(request, 'profile.html',{"current_user":current_user,"profile":profile})

def get_song_by_id(request,song_id):
    try: 
        songs = Song.objects.get(id = song_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"details.html", {"song":songs})     


































# Create your views here.

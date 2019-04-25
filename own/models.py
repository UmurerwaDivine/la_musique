from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from audiofield.fields import AudioField
from tinymce.models import HTMLField
import os.path
# Create your models here.
class Profile(models.Model):
	username = models.CharField(default='',max_length=30)
	# profile_pic = models.ImageField(upload_to = "profile/",null=True)
	user=models.ForeignKey(User,null=True)

	def __str__(self):
		return self.username

	def delete_profile(self):
		self.delete()

	def save_profile(self):
		self.save()

# class Album(models.Model):
#     albumName = models.CharField(max_length = 30)
#     artist = models.ForeignKey('Artist')
#     date = models.DateTimeField('Release Date')
#     albumInfo = models.TextField()
#     albumArt = models.ImageField(upload_to="images/albumart/")

#     def __unicode__(self):
#         return self.albumName

class Song(models.Model):
    pic = models.ImageField(upload_to="images/albumart/")
    songName = models.CharField(max_length = 30)
    artistName = models.CharField(max_length = 30,null=True)
    # audio_track = models.FileField(upload_to="songs/")
    audio_track = AudioField(upload_to='songs/', blank=True,
                        ext_whitelist=(".mp3", ".wav", ".ogg"),
                        help_text=("Allowed type - .mp3, .wav, .ogg"))

    lyrics = models.TextField(default='',blank = True)

    def __unicode__(self):
        return self.songName

    @classmethod
    def get_song_by_id(cls,song_id):
        songs= Song.objects.get(id=song_id)
        return songs

    @classmethod
    def search_by_artist(cls, search_input):
        songs = cls.objects.filter(artistName__name__icontains=search_input)
        return songs 

    # @classmethod 
    # def audio_file_player(self):
    
    
    #    if self.audio_track:
    #         file_url = settings.MEDIA_URL + str(self.audio_track)
    #         player_string = '<audio src="%s" controls>Your browser does not support the audio element.</audio>' % (file_url)
    #         return player_string
    #         audio_file_player.allow_tags = True
    #         audio_file_player.short_description = ('Audio file player')  
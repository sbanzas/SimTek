from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    STANDARD = 'ST'
    ADVANCED = 'AD'
    profileTypes = ((STANDARD, 'standard'),(ADVANCED,'advanced'))
    usrData = models.OneToOneField(User,related_name='user_data')
    profileType = models.CharField(max_length=2,choices=profileTypes,default=STANDARD)

class Script(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(UserProfile)
    scriptFile = models.FileField(upload_to='scripts')
    public = models.BooleanField(default=True)
    
    def getName(self):
        return self.name

    def getScriptContent(self):
        return self.scriptFile.open()

class Visualization(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(UserProfile)
    visualizationFile = models.FileField(upload_to='visualizations')
    public = models.BooleanField(default=True)

    def getName(self):
        return self.name

    def getVisualizationContent(self):
        return self.visualizationFile.open()

class Mesh(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(UserProfile)
    meshFile = models.FileField(upload_to='meshes')
    public = models.BooleanField(default=True)
    
    def getName(self):
        return self.name

    def getMeshContent(self):
        return self.meshFile.open()

class Comment(models.Model):
    writter = models.ForeignKey(UserProfile)
    date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True)
    votes = models.IntegerField(default=0)
    votesCons = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    topic = models.CharField(max_length=50)
    text = models.CharField(max_length=500)

    def getAuthor(self):
        return self.writer.usrData.username
    
    def getDate(self):
        return self.date

    def getVotesOk(self):
        return self.votes - self.votesCons

    def getVotesCons(self):
        return self.votesCons

    def getTitle(self):
        return self.title

    def getTopic(self):
        return self.topic

    def getText(self):
        return self.text

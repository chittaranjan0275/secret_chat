from django.db import models


# Create your models here.
class Session(models.Model):
    link_slug = models.CharField(max_length=255)
    key = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s %s' % (self.link_slug, self.key)

class Chat_table(models.Model):
    link_slug = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255)
    chat = models.CharField(max_length=1000,null=True,blank=True)
    read = models.CharField(max_length=100,default=False)

    def __unicode__(self):
        return u'%s %s %s %s' % (self.link_slug, self.uuid, self.chat, self.reaf)
from django.db import models
from django.db.models import permalink


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    #Slug is used by the URL to identify the post It is not unreasonable to have two posts with the same Title.
    #To solve this you could set the slug field to contain the ID of the post ie. 2-my-second-post
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })


class Comment(models.Model):
    username = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    related_post = models.ForeignKey('blog.Blog')

    def __unicode__(self):
        return '%s' % self.username


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })
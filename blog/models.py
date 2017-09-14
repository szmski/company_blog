from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.


class Post(models.Model):
    '''
    Post model with author, title, textarea, created date(checking current time),
    and published date(for example we want to publish post in the future for
    some reasons).
    '''

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        '''
        Publish new post
        '''
        self.published_date = timezone.now()
        self.save()


    def approve_comments(self):
        '''
        Approve post
        '''
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        '''
        Getting absolute url 
        '''
        return reverse('post_detail', kwargs={'pk':pk})

    def __str__(self):
        self.title


class Comments(models.Model):
    '''
    Comments model where our post can have comments from diffrent authors -
    even guests.
    '''

    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        '''
        Approve comment written by user
        '''
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
from django.db import models

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    body = models.CharField(
        'Body', blank=True, null=True, max_length=140, db_index=True
    )

    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )

    likes = models.IntegerField(
        'Likes', blank=True, null=True, db_index=True, default=0
    )
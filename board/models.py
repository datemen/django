from django.db import models
from accounts.models import User

#一番大きいトピック
class First_Topic(models.Model):
    first_topic = models.CharField(max_length=15)

#二番目に大きいトピック
class Second_Topic(models.Model):
    first_topic = models.ForeignKey(First_Topic, on_delete=models.CASCADE, \
            related_name='second_first_topic')
    second_topic = models.CharField(max_length=15)
    
#三番目に大きいトピック
class Third_Topic(models.Model):
    second_topic = models.ForeignKey(Second_Topic, on_delete=models.CASCADE, \
            related_name='third_second_topic')
    third_topic = models.CharField(max_length=15)
    views = models.PositiveIntegerField(default=0)
    talk_count = models.PositiveIntegerField(default=0)
    
#Messageクラス
class Board_Message(models.Model):
    '''
    host = models.ForeignKey(User, on_delete=models.CASCADE, \
            related_name='message_host')
    '''
    screenname = models.CharField(max_length=15)
    content = models.TextField(max_length=1000)
    first_topic = models.ForeignKey(First_Topic, on_delete=models.CASCADE, \
            related_name='message_first_topic')
    second_topic = models.ForeignKey(Second_Topic, on_delete=models.CASCADE, \
            related_name='message_first_topic')
    third_topic = models.ForeignKey(Third_Topic, on_delete=models.CASCADE, \
            related_name='message_first_topic')
    pub_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-pub_date',)
        
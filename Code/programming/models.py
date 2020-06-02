from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
CATEGORY_CHOICES = (
    ('String', 'STRING'),
    ('Array', 'ARRAY'),
    ('List', 'LIST'),
    ('Linked List', 'LINKED LIST'),
    ('Tree', 'TREE'),
    ('Others', 'OTHERS'),
)


class Program(models.Model):
    pro_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    description = models.TextField(max_length=10000)
    recommended = models.CharField(max_length=50)
    asked = models.CharField(max_length=50)
    answer = models.TextField(max_length=2000, default="")
    Input = models.TextField(max_length=1000)
    Output = models.TextField(max_length=1000)
    starting_point = models.TextField(max_length=500, default="")
    pub_date = models.DateField()
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Program, self).save(*args, **kwargs)


class ProgramComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    class Meta:
        verbose_name = 'ProgramComment'
        verbose_name_plural = 'ProgramComments'

    def __str__(self):
        return self.comment[0:13]+"..."+" by "+self.user.username

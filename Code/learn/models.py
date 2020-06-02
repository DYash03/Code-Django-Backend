from django.db import models
from django.utils.text import slugify
# Create your models here.


class Technologies(models.Model):
    tech_id = models.AutoField(primary_key=True)
    blog_name = models.CharField(max_length=70)
    category = models.CharField(max_length=50)
    description_1 = models.TextField(max_length=5000)
    description_2 = models.TextField(max_length=10000)
    description_3 = models.TextField(max_length=5000)
    views = models.IntegerField(default=0)
    ref_link_1 = models.CharField(max_length=100)
    ref_link_2 = models.CharField(max_length=100)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="learn/images")
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'

    def __str__(self):
        return self.blog_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.blog_name)
        super(Technologies, self).save(*args, **kwargs)


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    mob = models.CharField(max_length=50)
    textarea = models.TextField(max_length=10000, default="")

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name+str(self.msg_id)


class Editor(models.Model):
    ed_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    program_name = models.CharField(max_length=100)
    source = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    description = models.TextField(max_length=10000)
    solution = models.TextField(max_length=1500)
    Input = models.TextField(max_length=1000)
    Output = models.TextField(max_length=1000)

    def __str__(self):
        return self.name+str(self.ed_id)

from django.db import models
from django.contrib.auth.models import User
from students.models import Student
from uuslug import slugify


class Subject(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Subject, self).save(*args, **kwargs)


class Course(models.Model):
    owner = models.ForeignKey(User, related_name='courses_created', verbose_name='Professor', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses', verbose_name='Subject', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Title')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    overview = models.TextField(verbose_name='Overview')
    students = models.ManyToManyField(User, related_name='courses_joined', blank=True, verbose_name='Students')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)

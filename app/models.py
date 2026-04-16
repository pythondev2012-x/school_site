from django.db import models

class Banner(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.title


class Lessons(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Lessons"

    def __str__(self):
        return self.name


class Lesson_videos(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name='videos', null=True, blank=True)
    video = models.FileField(upload_to='lessons/videos/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Lesson_videos"

    def __str__(self):
        name = self.lesson.name if self.lesson else "Unknown"
        return f"{name} video"


class Lessons_image(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    image = models.ImageField(upload_to='lessons/images/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Lessons_images"

    def __str__(self):
        name = self.lesson.name if self.lesson else "Unknown"
        return f"{name} image"


class Lessons_collection(models.Model):
    lesson = models.ManyToManyField(Lessons, related_name='collections', blank=True)
    title = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='collection_covers/', null=True, blank=True)

    def __str__(self):
        return self.title


class Blog_category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Blog_categories"

    def __str__(self):
        return self.name


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Blog_category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title


class Leaderboard(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='leaderboard/', null=True, blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name


class Teachers(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    telegram = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='teachers/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Teachers"

    def __str__(self):
        return self.name
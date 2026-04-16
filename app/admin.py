from django.contrib import admin
from . import models
from unfold.admin import ModelAdmin

@admin.register(models.Banner)
class BannerAdmin(ModelAdmin):
    pass

@admin.register(models.Lessons)
class LessonsAdmin(ModelAdmin):
    pass

@admin.register(models.Leaderboard)
class LeaderboardAdmin(ModelAdmin):
    pass

@admin.register(models.Contacts)
class ContactsAdmin(ModelAdmin):
    pass

@admin.register(models.Blog_category)
class BlogCategoryAdmin(ModelAdmin):
    pass

@admin.register(models.Lessons_collection)
class LessonsCollectionAdmin(ModelAdmin):
    pass

@admin.register(models.Blogs)
class BlogsAdmin(ModelAdmin):
    pass

@admin.register(models.Teachers)
class TeachersAdmin(ModelAdmin):
    pass

@admin.register(models.Lesson_videos)
class LessonVideosAdmin(ModelAdmin):
    pass

@admin.register(models.Lessons_image)
class LessonsImagesAdmin(ModelAdmin):
    pass


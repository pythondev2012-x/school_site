import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . import models

def home(request):
    banners = models.Banner.objects.order_by('-id')[:3]
    lessons_collection = models.Lessons_collection.objects.all()
    blogs = models.Blogs.objects.order_by('-id')[:3][::-1]
    leaders = models.Leaderboard.objects.order_by('-id')[:3][::-1]
    teachers = models.Teachers.objects.all()
    lessons = models.Lessons.objects.all()

    context = {
        'banners': banners,
        'lessons': lessons,
        'lessons_collection': lessons_collection,
        'blogs': blogs,
        'leaders': leaders,
        'teachers': teachers,
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        message_text = request.POST.get('message')
        phone_number = request.POST.get('phone') or request.POST.get('number')

        try:
            models.Contacts.objects.create(
                name=name,
                email=email,
                message=f"Manzil: {address} | Xabar: {message_text}",
                number=phone_number
            )

            bot_token = "8757257839:AAEhhOWI6RoVht_ok1tx5lL_-gMT69cHRsI"
            chat_id = "5427482207"

            telegram_msg = (
                f"🚀 *Yangi Murojaat!*\n\n"
                f"👤 *Ism:* {name}\n"
                f"📍 *Manzil:* {address}\n"
                f"📞 *Tel:* {phone_number}\n"
                f"📧 *Email:* {email}\n"
                f"📝 *Xabar:* {message_text}"
            )

            telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            payload = {
                "chat_id": chat_id,
                "text": telegram_msg,
                "parse_mode": "Markdown"
            }

            requests.post(telegram_url, json=payload, timeout=10)
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi!")

        except Exception as e:
            print(f"Error: {e}")
            messages.error(request, "Xatolik yuz berdi.")

        return redirect('home')

    return render(request, 'index.html', context=context)

def blog_detail(request, id):
    blog = get_object_or_404(models.Blogs, id=id)
    categories = models.Blog_category.objects.all()
    return render(request, 'blog_detail.html', {'blog': blog, 'categories': categories})

def blog_category_list(request, id):
    category = get_object_or_404(models.Blog_category, id=id)
    blogs = models.Blogs.objects.filter(category=category).order_by('-id')
    categories = models.Blog_category.objects.all()
    return render(request, 'blog_list.html', {'category': category, 'blogs': blogs, 'categories': categories})

def lesson_detail(request, id):
    collection = get_object_or_404(models.Lessons_collection, id=id)
    return render(request, 'lesson.html', {'collection': collection})

def teacher_detail(request, id):
    teacher = get_object_or_404(models.Teachers, id=id)
    return render(request, 'teachers_detail.html', {'teacher': teacher})
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from .models import Teacher, Post

def index(request):
    return render(request, 'base.html')

def show_data(request):
    return render(request, 'teachers/show_data.html')

def add_post(request):
    name = None
    hourly_rate = None
    message = " не удалось добавить в базу!"
    try:
        name = request.GET['name']
        hourly_rate = int(request.GET['hourly_rate'])
        m_type = "succes"
        assert not Post.objects.filter(name__iexact=name)
        message = " была успешно добавлена!"
    except:
        m_type = 'error'
    return render(request, 'teachers/add_post.html', 
        {'name': name, 'hourly_rate': hourly_rate, 'm_type': m_type, 'message': message} )

def add_thing(request):
    teacher = {'data': None, 'name': 'Преподаватель', 'id': 'teacher'}
    work_place = {'data': None, 'name': 'Место работы', 'id': 'work_place'}
    name = {'data': None, 'name': 'Название', 'id': 'name'}
    hours = {'data': None, 'name': 'Суммарные часы', 'id': 'hours'}
    message = " не удалось добавить в базу!"
    try:
        teacher['data'] = request.GET['teacher']
        work_place['data'] = request.GET['work_place']
        name['data'] = request.GET['name']
        hours['data'] = int(request.GET['hours'])
        assert Teacher.objects.filter(fio__iexact=teacher['data']).count() != 0
        m_type = "succes"
        message = " был успешно добавлен!"
    except:
        m_type = 'error'
    fields = [
        teacher, 
        work_place,
        name,
        hours
    ]
    return render(request, 'teachers/add_thing.html', 
        {'fields': fields, 'm_type': m_type, 'message': message} )

def add_teacher(request):
    post = {'data': None, 'name': 'Должность', 'id': 'post'}
    fio = {'data': None, 'name': 'ФИО', 'id': 'fio'}
    phone = {'data': None, 'name': 'Телефон', 'id': 'phone'}
    home_address = {'data': None, 'name': 'Адресс', 'id': 'home_address'}
    characteristic = {'data': None, 'name': 'Характеристика', 'id': 'characteristic'}
    message = " не был добавлен в базу!"
    try:
        post['data'] = request.GET['post']
        fio['data'] = request.GET['fio']
        phone['data'] = request.GET['phone']
        home_address['data'] = request.GET['home_address']
        characteristic['data'] = request.GET['characteristic']
        assert Teacher.objects.filter(fio__iexact=fio['data']).count() == 0
        assert Post.objects.filter(name__iexact=post['data']).count() != 0
        m_type = "succes"
        message = " был успешно добавлен!"
    except:
        m_type = 'error'
    fields = [
        post, 
        fio,
        phone,
        home_address,
        characteristic
    ]
    return render(request, 'teachers/add_teacher.html', 
        {'fields': fields, 'm_type': m_type, 'message': message} )
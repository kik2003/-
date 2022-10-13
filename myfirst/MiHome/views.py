# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Record
from .forms import RecordForm
import sqlite3
from pathlib import Path

def id_save():
    BASE_DIR = Path(__file__).resolve().parent.parent
    db = sqlite3.connect(f'{BASE_DIR}\db.sqlite3')
    for value in db.execute("SELECT id FROM MiHome_record"):
        id_max = value
    id_save = int(id_max[0]) + 1
    return id_save

def work_with_the_databasework_with_the_database(id_save,name_save,number_save,d_1,time_save):
    BASE_DIR = Path(__file__).resolve().parent.parent
    db = sqlite3.connect(f'{BASE_DIR}\db.sqlite3')
    sql = db.cursor()

    sql.execute(f"INSERT INTO MiHome_record VALUES (?,?,?,?,?)",
                (id_save, name_save, number_save, d_1, time_save))
    db.commit()
def f():
    BASE_DIR = Path(__file__).resolve().parent.parent
    db = sqlite3.connect(f'{BASE_DIR}\db.sqlite3')

    for value in db.execute("SELECT * FROM MiHome_record"):
        print(value)
def ff(reguest,name_save,number_save,d_1,time_save):
    if reguest.method == "POST":
        error = ''
        if not name_save == '':
            work_with_the_databasework_with_the_database(id_save(),name_save,number_save,d_1,time_save)
    else:
        error = 'ви не корекно заповнели перевірте :)'

def index(reguest):
    global i_receive
    global d_1
    i_delete = []
    i_receive = []
    error = ''
    record = Record.objects.order_by('time')
    form = RecordForm(reguest.POST)
    for i_i in range(9,18):
        i_1 = i_i
        i_2 = '00'
        i_3 = 30
        d_1 =f'{i_1}:{i_2}'
        d_2 =f'{i_1}:{i_3}'
        i_receive.append(d_1)
        i_receive.append(d_2)

    n = -1
    k = form.data
    k_2 = k.dict()
    try:
        d_1 = k_2['data']
    except KeyError:
        d_1 = ''

    for tt in i_receive:
        tt = tt+':00'
        if len(tt) == 7:
            tt = '0' + tt
        n = n + 1
        for el in record:
            if str(d_1) == str(el.data) and str(tt) == str(el.time):
                i_delete.append(i_receive[n])

            elif str(d_1) == '' :
                i_receive=[]
    for i_delete in i_delete:
        print(i_delete)
        i_receive.remove(i_delete)

    context = {
        'i_receive': i_receive,
        'form': form,
        'error': error
    }
    return render(reguest, 'MiHome/mi.html',context)

def g_9_00(reguest):
        global d_1
        time_save = '9:00:00'
        error = ''
        form = RecordForm(reguest.POST)

        k = form.data
        k_2 = k.dict()
        try:
            name_save = k_2['name']
        except KeyError:
            name_save = ''
        try:
            number_save = k_2['number']
        except KeyError:
            number_save = ''
        ff(reguest, name_save, number_save, d_1, time_save)
        context = {
            'form': form,
            'error': error
        }
        return render(reguest, 'MiHome/9-00.html', context)

def g_9_30(reguest):
    global d_1
    time_save = '9:30:00'
    error = ''
    form = RecordForm(reguest.POST)

    k = form.data
    k_2 = k.dict()
    try:
        name_save = k_2['name']
    except KeyError:
        name_save = ''
    try:
        number_save = k_2['number']
    except KeyError:
        number_save = ''
    ff(reguest, name_save, number_save, d_1, time_save)
    context = {
        'form': form,
        'error': error
    }
    return render(reguest, 'MiHome/9-00.html', context)

def g_10_00(reguest):
    global d_1
    time_save = '10:00:00'
    error = ''
    form = RecordForm(reguest.POST)

    k = form.data
    k_2 = k.dict()
    try:
        name_save = k_2['name']
    except KeyError:
        name_save = ''
    try:
        number_save = k_2['number']
    except KeyError:
        number_save = ''
    ff(reguest, name_save, number_save, d_1, time_save)
    context = {
        'form': form,
        'error': error
    }
    return render(reguest, 'MiHome/9-00.html', context)

def g_10_30(reguest):
    global d_1
    time_save = '10:30:00'
    error = ''
    form = RecordForm(reguest.POST)

    k = form.data
    k_2 = k.dict()
    try:
        name_save = k_2['name']
    except KeyError:
        name_save = ''
    try:
        number_save = k_2['number']
    except KeyError:
        number_save = ''
    ff(reguest, name_save, number_save, d_1, time_save)
    context = {
        'form': form,
        'error': error
    }
    return render(reguest, 'MiHome/9-00.html', context)

def g_11_00(reguest):
    global d_1
    time_save = '11:00:00'
    error = ''
    form = RecordForm(reguest.POST)

    k = form.data
    k_2 = k.dict()
    try:
        name_save = k_2['name']
    except KeyError:
        name_save = ''
    try:
        number_save = k_2['number']
    except KeyError:
        number_save = ''
    ff(reguest, name_save, number_save, d_1, time_save)
    context = {
        'form': form,
        'error': error
    }
    return render(reguest, 'MiHome/9-00.html', context)

def g_11_30(reguest):
    global d_1
    time_save = '11:30:00'
    error = ''
    form = RecordForm(reguest.POST)

    k = form.data
    k_2 = k.dict()
    try:
        name_save = k_2['name']
    except KeyError:
        name_save = ''
    try:
        number_save = k_2['number']
    except KeyError:
        number_save = ''
    ff(reguest, name_save, number_save, d_1, time_save)
    context = {
        'form': form,
        'error': error
    }
    return render(reguest, 'MiHome/9-00.html', context)

def g_12_00(reguest):
    global d_1
    time_save = '12:00:00'
    error = ''
    form = RecordForm(reguest.POST)

    k = form.data
    k_2 = k.dict()
    try:
        name_save = k_2['name']
    except KeyError:
        name_save = ''
    try:
        number_save = k_2['number']
    except KeyError:
        number_save = ''
    ff(reguest, name_save, number_save, d_1, time_save)
    context = {
        'form': form,
        'error': error
    }
    return render(reguest, 'MiHome/9-00.html', context)

def g_12_30(reguest):
    global d_1
    time_save = '12:30:00'
    error = ''
    form = RecordForm(reguest.POST)

    k = form.data
    k_2 = k.dict()
    try:
        name_save = k_2['name']
    except KeyError:
        name_save = ''
    try:
        number_save = k_2['number']
    except KeyError:
        number_save = ''
    ff(reguest, name_save, number_save, d_1, time_save)
    context = {
        'form': form,
        'error': error
    }
    return render(reguest, 'MiHome/9-00.html', context)

def g_13_00(reguest):
    global d_1
    time_save = '13:00:00'
    error = ''
    form = RecordForm(reguest.POST)

    k = form.data
    k_2 = k.dict()
    try:
        name_save = k_2['name']
    except KeyError:
        name_save = ''
    try:
        number_save = k_2['number']
    except KeyError:
        number_save = ''
    ff(reguest, name_save, number_save, d_1, time_save)
    context = {
        'form': form,
        'error': error
    }
    return render(reguest, 'MiHome/9-00.html', context)

def g_13_30(reguest):
    global d_1
    time_save = '13:30:00'
    error = ''
    form = RecordForm(reguest.POST)

    k = form.data
    k_2 = k.dict()
    try:
        name_save = k_2['name']
    except KeyError:
        name_save = ''
    try:
        number_save = k_2['number']
    except KeyError:
        number_save = ''
    ff(reguest, name_save, number_save, d_1, time_save)
    context = {
        'form': form,
        'error': error
    }
    return render(reguest, 'MiHome/9-00.html', context)

def g_14_00(reguest):
    global d_1
    time_save = '14:00:00'
    error = ''
    form = RecordForm(reguest.POST)

    k = form.data
    k_2 = k.dict()
    try:
        name_save = k_2['name']
    except KeyError:
        name_save = ''
    try:
        number_save = k_2['number']
    except KeyError:
        number_save = ''
    ff(reguest, name_save, number_save, d_1, time_save)
    context = {
        'form': form,
        'error': error
    }
    return render(reguest, 'MiHome/9-00.html', context)

def g_14_30(reguest):
    global d_1
    time_save = '14:30:00'
    error = ''
    form = RecordForm(reguest.POST)

    k = form.data
    k_2 = k.dict()
    try:
        name_save = k_2['name']
    except KeyError:
        name_save = ''
    try:
        number_save = k_2['number']
    except KeyError:
        number_save = ''
    ff(reguest, name_save, number_save, d_1, time_save)
    context = {
        'form': form,
        'error': error
    }
    return render(reguest, 'MiHome/9-00.html', context)

def g_15_00(reguest):
    global d_1
    time_save = '15:00:00'
    error = ''
    form = RecordForm(reguest.POST)

    k = form.data
    k_2 = k.dict()
    try:
        name_save = k_2['name']
    except KeyError:
        name_save = ''
    try:
        number_save = k_2['number']
    except KeyError:
        number_save = ''
    ff(reguest, name_save, number_save, d_1, time_save)
    context = {
        'form': form,
        'error': error
    }
    return render(reguest, 'MiHome/9-00.html', context)

def g_15_30(reguest):
    global d_1
    time_save = '15:30:00'
    error = ''
    form = RecordForm(reguest.POST)

    k = form.data
    k_2 = k.dict()
    try:
        name_save = k_2['name']
    except KeyError:
        name_save = ''
    try:
        number_save = k_2['number']
    except KeyError:
        number_save = ''
    ff(reguest, name_save, number_save, d_1, time_save)
    context = {
        'form': form,
        'error': error
    }
    return render(reguest, 'MiHome/9-00.html', context)

def g_16_00(reguest):
    global d_1
    time_save = '16:00:00'
    error = ''
    form = RecordForm(reguest.POST)

    k = form.data
    k_2 = k.dict()
    try:
        name_save = k_2['name']
    except KeyError:
        name_save = ''
    try:
        number_save = k_2['number']
    except KeyError:
        number_save = ''
    ff(reguest, name_save, number_save, d_1, time_save)
    context = {
        'form': form,
        'error': error
    }
    return render(reguest, 'MiHome/9-00.html', context)

def g_16_30(reguest):
    global d_1
    time_save = '16:30:00'
    error = ''
    form = RecordForm(reguest.POST)

    k = form.data
    k_2 = k.dict()
    try:
        name_save = k_2['name']
    except KeyError:
        name_save = ''
    try:
        number_save = k_2['number']
    except KeyError:
        number_save = ''
    ff(reguest, name_save, number_save, d_1, time_save)
    context = {
        'form': form,
        'error': error
    }
    return render(reguest, 'MiHome/9-00.html', context)

def g_17_00(reguest):
    global d_1
    time_save = '17:00:00'
    error = ''
    form = RecordForm(reguest.POST)

    k = form.data
    k_2 = k.dict()
    try:
        name_save = k_2['name']
    except KeyError:
        name_save = ''
    try:
        number_save = k_2['number']
    except KeyError:
        number_save = ''
    ff(reguest, name_save, number_save, d_1, time_save)
    context = {
        'form': form,
        'error': error
    }
    return render(reguest, 'MiHome/9-00.html', context)

def g_17_30(reguest):
    global d_1
    time_save = '17:30:00'
    error = ''
    form = RecordForm(reguest.POST)

    k = form.data
    k_2 = k.dict()
    try:
        name_save = k_2['name']
    except KeyError:
        name_save = ''
    try:
        number_save = k_2['number']
    except KeyError:
        number_save = ''
    ff(reguest, name_save, number_save, d_1, time_save)
    context = {
        'form': form,
        'error': error
    }
    return render(reguest, 'MiHome/9-00.html', context)

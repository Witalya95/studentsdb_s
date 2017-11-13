from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


from django.views.generic.base import TemplateView


from students.models import Student, Group, Exam
from students.forms import GroupsForm, ExamForm, StudentForm, ContactForm


# Create your views here.
def index(request):
    return render(request, 'students/index.html')


def student_list(request):
    students = Student.objects.all()

    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    # paginate students
    paginator = Paginator(students, 2)
    page = request.GET.get('page')

    try:
        students = paginator.page(page)

    except PageNotAnInteger:
        students = paginator.page(1)

    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    context = {'students': students}
    return render(request, 'students/student_list.html', context)


def group_list(request):

    groups = Group.objects.all()
    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()
    context = {'groups': groups}
    return render(request, 'students/group_list.html', context)


def exam_list(request):

    exams = Exam.objects.all()
    context = {'exams':exams}
    return render(request, 'students/exam_list.html', context)

@login_required
def add_student(request):
    if request.method != 'POST':
        form = StudentForm()

    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(u'%s?status_message=Студента додано!' %reverse('students:student_list'))

    context = {'form': form}
    return render(request, 'students/add_student.html', context)

@login_required
def add_exam(request):
    if request.method != 'POST':
        form = ExamForm()
    else:
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(u'%s?status_message=Іспит додано!' %reverse('students:exam_list'))

    context = {'form': form}
    return render(request, 'students/add_exam.html', context)


@login_required
def delete_exam(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    exam.delete()
    return HttpResponseRedirect(u'%s?status_message=Іспит видалено!' %reverse('students:exam_list'))


@login_required
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return HttpResponseRedirect(u'%s?status_message=Студента видалено!' %reverse('students:student_list'))


@login_required
def edit_exam(request, exam_id):
    exam = Exam.objects.get(id=exam_id)

    if request.method != 'POST':
        form = ExamForm(instance=exam)

    else:
        if request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(u'%s?status_message=Зміни скасовано' %reverse('students:exam_list'))
        elif request.POST.get('save_button') is not None:
            form = ExamForm(instance=exam, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(u'%s?status_message=Зміни збережено!' % reverse('students:exam_list'))

    context = {'exam':exam, 'form':form}
    return render(request, 'students/edit_exam.html', context)

@login_required
def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)

    if request.method != 'POST':
        form = StudentForm(instance=student)

    else:
        if request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(u'%s?status_message=Зміни скасовано' %reverse('students:student_list'))
        elif request.POST.get('save_button') is not None:
            form = StudentForm(instance=student, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(u'%s?status_message=Зміни збережено!' %reverse('students:student_list'))

    context = {'student': student, 'form': form}
    return render(request, 'students/edit_student.html', context)

@login_required
def add_group(request):

    if request.method != 'POST':
        form = GroupsForm()
    else:
        form = GroupsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(u'%s?status_message=Групу додано!' %reverse('students:group_list'))

    context = {'form': form}
    return render(request,'students/add_group.html', context)

@login_required
def edit_group(request, group_id):
    group = Group.objects.get(id=group_id)

    if request.method != 'POST':
        form = GroupsForm(instance=group)
    else:
        if request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(u'%s?status_message=Зміни скасовано' %reverse('students:group_list'))
        elif request.POST.get('save_button') is not None:
            form = GroupsForm(instance=group, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(u'%s?status_message=Зміни збережено!' %reverse('students:group_list'))

    context = {'group': group, 'form': form}
    return render(request, 'students/edit_group.html', context)


def journal(request):

    return render(request, 'students/journal.html')


def contact_admin(request):
    ADMIN_EMAIL = 'admin@studentsdb.com'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            massage = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject, massage, from_email, [ADMIN_EMAIL])
            except Exception:
                return HttpResponseRedirect(
                    u'%s?status_message=Під час відправки листа виникла непередбачувана ' \
                    u'помилка. Спробуйте скористатись даною формою пізніше.' % reverse('students:contact_admin'))

            else:
                return HttpResponseRedirect(u'%s?status_message=Повідомлення успішно надіслане!' %reverse('students:contact_admin'))

    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'students/contact_admin.html', context)



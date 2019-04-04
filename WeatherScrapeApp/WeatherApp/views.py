from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .forms import StudentForm
from .models import Student
from .viewmodels import alertViewModel




# Create your views here.
# def index(request):
#     student_list = Student.objects.order_by('id')[:5]
#     context = {'student_list': student_list}
#     return render(request, 'WeatherApp/index.html', context)

# class IndexView(generic.ListView):
#     template_name = 'WeatherApp/index.html'
#     context_object_name = 'student_list'
#
#     def get_queryset(self):
#         return Student.objects.order_by('id')[:5]


# def detail(request, student_id):
#     student = get_object_or_404(Student, pk=student_id)
#     return render(request, 'WeatherApp/detail.html', {'student': student})
# class DetailView(generic.DetailView):
#     model = Student
#     template_name = 'WeatherApp/detail.html'


# def list_students(request):
#     students = Student.objects.all()
#     return render(request, 'WeatherApp/students.html', {'students': students})
class IndexView(generic.ListView):
    template_name = 'WeatherApp/students.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.order_by('id')


def alerts(request, student_id):
    student = Student.objects.get(id = student_id)
    alert = student.get_alert()
    print(alert.summary)
    context = {
        "student": student,
        "alert": alert,
    }
    return render(request, "WeatherApp/alert.html", context)

# def alert_view(request, id):
#     student = Student.objects.get(id=id)
#     alerts = student.get_alert()
#     print(alerts)
#     return render(request, 'WeatherApp/alert.html', {'student': student, 'alerts': alerts})


def create_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_students')

    return render(request, 'WeatherApp/students-form.html', {'form': form})


def update_student(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('list_students')

    return render(request, 'WeatherApp/students-form.html', {'form': form, 'student': student})


def delete_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('list_students')

    return render(request, 'WeatherApp/student-delete-confirm.html', {'student': student})






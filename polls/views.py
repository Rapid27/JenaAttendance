from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Employee , FingerprintIdentity , DailyAttendance
from datetime import datetime
from django.db.models.base import ObjectDoesNotExist
from django.views.decorators.clickjacking import xframe_options_exempt


#Landing page

def index(request):
    
    return render(request , 'polls/index.html')
#employee listing page , this page must display the daily checkin of each and every employee and their datasets 
class EmployeeListView(ListView):

    model = FingerprintIdentity
    template_name = 'polls/list.html'
    context_object_name = 'employees'
    paginate_by = 5

    
    
    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        test_day = DailyAttendance.objects.all()[0]#create an ordered list
        
        employees = test_day.daily_attendee.all()#create an ordered list
        page = self.request.GET.get('page')
        paginator = Paginator(employees, self.paginate_by)
        try:
            employees = paginator.page(page)
        except PageNotAnInteger:
            employees = paginator.page(1)
        except EmptyPage:
            employees = paginator.page(paginator.num_pages)
        context['employees'] = employees
        return context
@xframe_options_exempt    
def testPost(request):
    
    test_day = DailyAttendance.objects.all()[0]
    
   
    try:
        fingerprint_id = request.POST["finger_id"]
    except (KeyError):
        return render(request, 'polls/testPost.html', {'error_message':"session has been started",})
    
    if  FingerprintIdentity.objects.filter(received_value = fingerprint_id).exists():
       
        member = FingerprintIdentity.objects.get(received_value = fingerprint_id)
        #code for checkin and checkout management here
        if not member in test_day.daily_attendee.all():
            
            member.update_entry_time()
            member.reset_exit_time()
            member.save()
            test_day.daily_attendee.add(member)
            success_message = "check in successful"
            
            return render(request, 'polls/message.html', {'success_message': success_message,})
            
        else:
            test_day.daily_attendee.remove(member)
            member.update_exit_time()
            member.save()
            test_day.daily_attendee.add(member)
            success_message = "check out successful"
            
            return render(request , 'polls/message.html', {'success_message': success_message,})
            
            
        #deal with the attendance data so as to display it the page
        
        
            
    
        
        
        
        
    else :
        #code for enrolling management
        #must add code to return a usefull error message to the user
        new_member = Employee.objects.order_by("-pub_date")[0] #need to make the code more flexible inorder to attend to different people adding at the same time
        if not FingerprintIdentity.objects.filter(Jena_Employee= new_member).exists():# this is to avoid changing data for already enrolled members
            q = FingerprintIdentity(received_value= fingerprint_id , Jena_Employee=new_member)
            q.save()
            
            return render(request, 'polls/message.html', {'success_message': 'enrollment successful',})
        #the obove enrolling code caters for both doesNotexist scenarios, that is if some not completely registered tries to checkin, this system just ignores
        else:
            return render(request, 'polls/message.html', {'success_message': 'Employee does not exit visit IT',})
        
def upload_data(request):
    return render(request , 'polls/testPost.html' )# temporary view to run tests
        




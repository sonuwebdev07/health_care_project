from django.http import HttpResponse, JsonResponse
from service.models import Department
from service.models import DoctorDetail
from service.models import AppointmentDetail
from django.shortcuts import render

def homePage(request):

    department_details=Department.objects.all()
    
    if request.method=="POST":
        d_department_name=request.POST['d_name']
        d_doctor_name=request.POST['d_doctor_name']
        d_date=request.POST['d_date']
        d_time=request.POST['d_time']
        d_full_name=request.POST['d_full_name']
        d_phone=request.POST['d_phone']
        d_message=request.POST['d_message']
        print(d_department_name,d_doctor_name,d_date,d_time,d_full_name,d_phone,d_message)
        all_data=AppointmentDetail(app_department_name=d_department_name,app_doctor_name=d_doctor_name,app_date=d_date,app_time=d_time,full_name=d_full_name,mobile_num=d_phone,message=d_message)
        all_data.save()
    return render(request,'index.html',{'department_details':department_details})

def aboutPage(request):
    return render(request,'about.html')

def servicePage(request):

    department_details=Department.objects.all()

    return render(request,'service.html',{'department_details':department_details})

def contactPage(request):
    return render(request,'contact.html')

def allDoctorPage(request,id):

   all_doctor=DoctorDetail.objects.filter(department_name_id=id)

   return render(request,'all_doctor.html',{'all_doctor':all_doctor})

def singleDoctorDetails(request,id):

    single_doctor=DoctorDetail.objects.get(id=id)
    
    return render(request,'department_details.html',{'single_doctor':single_doctor}) 

def appointmentPage(request,id):
    my_list=[]
    msg=''

    doctor_detail=DoctorDetail.objects.filter(id=id).values()
    dict1={}
    dict1['doc_name']=doctor_detail[0]['doctor_full_name']
    doc_department_id=doctor_detail[0]['department_name_id']

    department_details=Department.objects.filter(id=doc_department_id).values()
    dict1['department_name']=department_details[0]['department_name']

    my_list.append(dict1)

    if request.method=="POST":
        a_department_name=request.POST['a_department_name']
        a_doctor_name=request.POST['a_doctor_name']
        a_date=request.POST['a_date']
        a_time=request.POST['a_time']
        full_name=request.POST['full_name']
        phone=request.POST['phone']
        message=request.POST['message']
        #print(a_department_name,a_doctor_name,a_date,a_time,full_name,phone,message)
        data=AppointmentDetail(app_department_name=a_department_name,app_doctor_name=a_doctor_name,app_date=a_date,app_time=a_time,full_name=full_name,mobile_num=phone,message=message)
        data.save()

    return render(request,'appointment.html',{'my_list':my_list})

def get_doctor_department_name_ajax(request):
    if request.method == "POST":
        subject_id = request.POST['subject_id']
        try:
            department_details=Department.objects.filter(department_name=subject_id).values()                
            topics = DoctorDetail.objects.filter(department_name = department_details[0]['id'])
            print(department_details[0]['id'])
        except Exception:
                data={}
                data['error_message'] = 'error'
                return JsonResponse(data)
        return JsonResponse(list(topics.values('id', 'department_name','doctor_full_name')), safe = False) 
    return render(request,'index.html')  
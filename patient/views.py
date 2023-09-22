# Create your views here.
from django.shortcuts import render,redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from .forms import PatientForm
from . import models
from django.conf import settings
import os
def patient_add(request):

    if request.method =='POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect(reverse('patient:list'))
    else:
        form  = PatientForm()
    return render(request, 'patient/add.html', context={'form':form})


def patient_list(request):
    all_patient = models.Patient.objects.all()
    context = {'patient': all_patient}

    if request.method == 'POST':
        # POST 요청 처리
        patient_number = request.POST.get('patient_number')  # 환자 번호 가져오기
        try:
            patient_to_delete = models.Patient.objects.get(patient_num=patient_number)
            patient_to_delete.delete()
            print(patient_to_delete)
        except models.Patient.DoesNotExist:
            pass  # 환자가 없으면 무시

    return render(request, 'patient/list.html', context=context)

def patient_common(request):
    return render(request, 'patient/patient_common.html')

def patient_detail(request, pk):
    patient = get_object_or_404(models.Patient, pk=pk)
    #해당하는 object를 template에 보내줌
    error_message = None
    #사용자가 nii file을 업로드할 경우
    if request.method == 'POST':
        if 'formFile' in request.FILES:
            uploaded_file = request.FILES['formFile']
            file_name = uploaded_file.name

            # 저장 경로를 설정
            save_path = os.path.join(settings.MEDIA_ROOT, 'uploaded_files', file_name)

            # 디렉터리가 존재하지 않으면 생성
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            with open(save_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            print(file_name, "uploaded!")

        else:
            error_message = "파일을 선택해 주세요"
    return render(request, 'patient/patient_detail.html', {'patient': patient, 'error_message': error_message})


def search_results(request):
    query = request.GET.get('q')
    results = models.Patient.objects.filter(first_name__icontains=query)  # 검색 로직을 수정하세요

    return render(request, 'patient/search_results.html', {'results': results, 'query': query})
from django.http import HttpResponse
from django.shortcuts import render

import joblib

def home(request):
    return render(request,"home.html")


def result(request):


    cls  =joblib.load('finalized_model.sav')
    lis = []
    lis.append(request.GET['Pregnancies'])
    lis.append(request.GET['Glucose'])
    lis.append(request.GET['BloodPressure'])
    lis.append(request.GET['SkinThickness'])
    lis.append(request.GET['Insulin'])
    lis.append(request.GET['BMI'])
    lis.append(request.GET['DiabetesPedigreeFunction'])
    lis.append(request.GET['Age'])

    ans = cls.predict([lis])
    return render(request,"result.html",{'ans' : ans})
	

from django.shortcuts import render, redirect
# Importing Requires Libraries
import pandas as pd 
# import logging # logging libraries is used to make log file 
import pickle # pickle is used to load the machine Learning Model
import numpy as np

import warnings
warnings.filterwarnings("ignore")
from .models import Diabetes
# import joblib

# from App import prediction
model = pickle.load(open('./models/KNeighborsClassifiermodel.sav', 'rb'))
Scalar = pickle.load(open('./models/KNeighborsClassifierscalar.sav', 'rb'))



def index(request):
    return render(request,'Home/index.html')


def diabetes(request):
    return render(request,'Diabetes/diabetes.html')


def diabetesresult(request):
    if request.method == 'POST':
        # try:
            
            Patient_name = request.POST['Patient_name']
            Gender = request.POST['Gender']
            Glucose = int(request.POST['Glucose'])
            Blood_Pressure = int(request.POST['Blood_Pressure'])
            Skin_thickness = int(request.POST['Skin_thickness'])
            Insulin = int(request.POST['Insulin'])
            BMI = float(request.POST['BMI'])
            Diabetes_Pedigree_Function = float(request.POST['Diabetes_Pedigree_Function'])
            Age = int(request.POST['Age'])
            
            

            if Gender == 'male':
                Pregnancy = 0
               
            else:
                Pregnancy = request.POST['Pregnancy']
            

            # dont touch this data
            data = {
                    "Pregnancy" : Pregnancy,
                    "Glucose" : Glucose,
                    "Blood_Pressure" : Blood_Pressure,
                    "Skin_thickness" : Skin_thickness,
                    "Insulin" : Insulin,
                    "BMI"  : BMI,
                    "Diabetes_Pedigree_Function" : Diabetes_Pedigree_Function,
                    "Age" : Age
                    
            }

            
      


            data = pd.DataFrame(data, index = [1,])
            
            scaled_data = Scalar.transform(data)
            pred = model.predict(scaled_data)
            prob = model.predict_proba(scaled_data) # predicting the probablity of the class

            pred = pred[0]
            prob = (prob[0][1]*100)
            patient_info = Diabetes(Patient_name=Patient_name,Age=Age,Gender=Gender,Glucose=Glucose,Skin_thickness=Skin_thickness,Blood_Pressure=Blood_Pressure,Insulin=Insulin, BMI=BMI,Diabetes_Pedigree_Function=Diabetes_Pedigree_Function, Probablity_percent= prob,Pregnancy=Pregnancy)
            patient_info.save()
            return render(request,'Diabetes/diabetesresult.html',context = {'Patient_name':Patient_name,'Age':Age,'Gender':Gender,'Report':pred,'Probablity':prob})
            
        
        # except:
        #     return render(request,'Diabetes/diabetesresult.html')
            


    else:
        return redirect('Home/index.html')
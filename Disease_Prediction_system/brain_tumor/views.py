from django.shortcuts import render, redirect
# Importing Requires Libraries
import pandas as pd 
# import logging # logging libraries is used to make log file 
import pickle # pickle is used to load the machine Learning Model
import numpy as np

import warnings
warnings.filterwarnings("ignore")
from .models import Braintumor

# Create your views here.

def braintumorresult():
    if request.method == 'POST':
    
        file = request.files['img']
        name = request.form['name']
        gender = request.form['gender']
        age = int(request.form['age'])
        if file:
            filename = secure_filename(file.filename)
            x = datetime.datetime.now()
            print(str(x)+filename)
            filename = str(x.year)+str(x.minute)+str(x.second)+filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        images = image.load_img('static/img/upload/'+filename,target_size=(150,150))
        images = image.img_to_array(images)# changing in array
        images = np.expand_dims(images,axis = 0)
        images = images/255 # scaling the data
        model = load_model("brain_tumor_76_valscore_model.h5")
        result = model.predict_classes(images)
        prob = model.predict_proba(images)
        
        prob = round(prob[0][0]*100,2)
        img = os.path.join(app.config['UPLOAD_FOLDER'], filename)
       
                     
        return render_template('braintumorresult.html',title = 'Brain Tumor Result',result = {"report":result,"image":img,'name':name,'age':age,'gender':gender,'probablity':prob})

    else:
        return redirect('index.html',title = 'Home')
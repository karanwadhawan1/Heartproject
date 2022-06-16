from token import EXACT_TOKEN_TYPES
from django.shortcuts import render,HttpResponse
from django.http import FileResponse, Http404
import pickle 
import numpy as np
from django.contrib import messages
 

classifier=pickle.load(open('./model/classifiermodel.pkl','rb'))


# Create your views here.
def index(request):
    
    data={'predict':2}
    if request.method=='POST':
            rac=[]
            try:
                n1=eval(request.POST.get('BMI'))
                n2=eval(request.POST.get('Smoking'))
                n3=eval(request.POST.get('AlcoholDrinking'))
                n4=eval(request.POST.get('Stroke'))
                n5=eval(request.POST.get('DiffWalking'))
                n6=eval(request.POST.get('Sex'))
                n7=eval(request.POST.get('Diabetic'))
                n8=eval(request.POST.get('PhysicalActivity'))
                n9=eval(request.POST.get('SleepTime'))
                n10=eval(request.POST.get('Asthma'))
                n11=eval(request.POST.get('KidneyDisease'))
                n12=eval(request.POST.get('SkinCance'))
                n13=eval(request.POST.get('AgeCategory'))
                n14=eval(request.POST.get('GenralHealth'))
                n15=eval(request.POST.get('Race'))
                n16=eval(request.POST.get('PhysicalHealth'))
                n17=eval(request.POST.get('MentalHealth'))
            except :
                messages.info(request,'Please fill all columns and value should be a numeric!')
                return render(request,'index.html',data)
            else:
                
                rac=[]
                final = []
                for i in range(0,6):
                    if i==n15-1:   
                        rac.append(1)
                    else:
                        rac.append(0)
                new_list=[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,rac,n16,n17]
                
                def my_fun(temp_list):
                    for ele in temp_list:
                        if type(ele) == list:
                            my_fun(ele)
                        else:
                            final.append(ele)

                my_fun(new_list)
                
                arr1=np.array(final).reshape(1,22)
                prediction =classifier.predict(arr1)
                
                if(prediction[0]==0):
                    data['predict']=1
                else:
                    data['predict']=0   
                    
                    
                messages.success(request,'The form is submited. Please see your result below!')


    
    #print(final)
    return render(request,'index.html',data)
    
        
def about(request):
    try:
        return HttpResponse(open('./model/Heart disease file .pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()


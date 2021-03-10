from django.shortcuts import render
import pandas as pd
from .models import Predict


# Create your views here.

def prediction(request):
    model = pd.read_pickle('new_model.pickle')
    classification = None
    if request.method == 'POST':
        glucose = request.POST['glucose']
        insulin = request.POST['insulin']
        bmi = request.POST['bmi']
        age = request.POST['age']

        result = model.predict([[glucose, insulin, bmi, age]])
        classification = result[0]
        print(classification)
        Predict.objects.create(user=request.user, glucose=glucose, insulin=insulin, bmi=bmi, age=age,
                               result=classification)
    return render(request, 'predict/predict.html', {'detector': classification})


def history(request):
    h = Predict.objects.filter(user=request.user)
    return render(request, 'predict/history.html', {'h': h})

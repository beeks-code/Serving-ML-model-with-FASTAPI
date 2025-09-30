from fastapi import FastAPI
from fastapi.responses import JSONResponse,Response
import pandas as pd
from validator import user,APIResponse
from ML.model import predict,MODEL_VERSION,model
app=FastAPI()

@app.get("/home")
def home():
    return {"message":"This is Insurance prediction API"}

@app.get("")
def health_check():
    return {
        "status":"ok",
        "Model_Version":MODEL_VERSION,
        "Model_loaded": True if predict else False
    }

@app.post('/predict',response_model=APIResponse)
def predict_premium(data: user):

    input_dict = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    try:
        prediction = predict(input_dict)
        return JSONResponse(status_code=200, content={'Prediction': prediction})
    except Exception as e:
        return JSONResponse(status_code=500,content={"message":str(e)})
        

    

    
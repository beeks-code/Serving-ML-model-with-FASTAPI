import pickle
import pandas as pd
with open("config\model.pkl","rb") as f:
    model=pickle.load(f)

class_predict=model.classes_.tolist()

def predict(data:dict):
    input_df = pd.DataFrame([data])
    pred=model.predict(input_df)[0]
    probab=model.predict_proba(input_df)[0]
    max_porb=max(probab)
    dict={key: value for key, value in zip(class_predict,probab)}
    return {
        "Predicted_class":pred,
        "Confidence":max_porb,
        "Probability":dict
        
    }
MODEL_VERSION=1.0
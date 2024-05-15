from tools import *
import joblib
import xgboost as xgb


df = pd.read_csv("./data/df_future.csv")
data = df.copy()

data['date'] = pd.to_datetime(data['date'])
data = create_features(data)

loaded_model = joblib.load("model.pkl")

predict = loaded_model.predict(data)

df['sales_quantity'] = predict

df.to_csv("./data/df_predict.csv")
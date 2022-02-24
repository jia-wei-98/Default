#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
import joblib


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        income = request.form.get("income")
        age = request.form.get("age")
        loan = request.form.get("loan")
        model_name = request.form.get("Model")
        print (income,age,loan,model_name)
        model = joblib.load(model_name)
        pred = model.predict ([[float(income), float(age),float(loan)]])
        if int(pred) == 0:
            s = "The client is predicted to not default."
            return (render_template("index.html", result = s ))
        else:
            s = "The client is predicted to default."
            return (render_template("index.html", result = s ))
    else:
        return (render_template("index.html", result = "2"))


# In[4]:


if __name__ == "__main__":
    app.run()


# In[ ]:





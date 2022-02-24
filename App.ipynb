{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a2da59f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask\n",
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "16683d4d",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "282445fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import request, render_template\n",
    "\n",
    "@app.route(\"/\", methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method == \"POST\":\n",
    "        income = request.form.get(\"income\")\n",
    "        age = request.form.get(\"age\")\n",
    "        loan = request.form.get(\"loan\")\n",
    "        model_name = request.form.get(\"Model\")\n",
    "        print (income,age,loan,model_name)\n",
    "        model = joblib.load(model_name)\n",
    "        pred = model.predict ([[float(income), float(age),float(loan)]])\n",
    "        if int(pred) == 0:\n",
    "            s = \"The client is predicted to not default.\"\n",
    "            return (render_template(\"index.html\", result = s ))\n",
    "        else:\n",
    "            s = \"The client is predicted to default.\"\n",
    "            return (render_template(\"index.html\", result = s ))\n",
    "    else:\n",
    "        return (render_template(\"index.html\", result = \"2\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a6ffde3e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [24/Feb/2022 11:57:33] \"GET / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10000 20 2000 Random\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [24/Feb/2022 11:57:43] \"POST / HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ac1a020d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

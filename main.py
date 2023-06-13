from flask import Flask, render_template, request, redirect, url_for, Response
import tensorflow as tf
import numpy as np
import os
import pandas as pd
 
app = Flask(__name__)

path = "model" 
model = tf.saved_model.load(path)


age = tf.constant([18], dtype=tf.int64)
level = tf.constant([1], dtype=tf.int64)
user_id = tf.constant([14], dtype=tf.int64)
gender = tf.constant(["Laki-laki"], dtype=tf.string)

# Pass a user id in, get top predicted movie titles back.
query = {"age": age,"gender": gender,"level": level,"user_id":user_id}

@app.route('/')
def home():
   
    #query = {"age": np.array([90]),"gender": np.array(["Laki-laki"]),"level": np.array([3]),"user_id":np.array([10])}
    scores, titles = loaded(query)
    titles = titles[0][:3]
    titles = titles.numpy().tolist()
    
    for a in titles:
        print(a)
    return render_template('home.html',title = titles)
    

 
 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

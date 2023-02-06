![](https://github.com/silvilio/EDA-ML-Prediction-Madrid/blob/main/portadas_gitHub.png)

<p align="center">
  <a href="#english">
    <img src="https://raw.githubusercontent.com/lipis/flag-icon-css/master/flags/4x3/gb.svg" alt="English" width="32" height="32">
  </a>
  <a href="#spanish">
    <img src="https://raw.githubusercontent.com/lipis/flag-icon-css/master/flags/4x3/es.svg" alt="Spanish" width="32" height="32">
  </a>
</p>

# English  

This project is an exploratory data analysis (EDA) of Airbnb in Madrid, with the aim of identifying patterns and trends in rental prices. Data has been collected and pre-processed for various home characteristics, such as location, availability, and number of reviews. In turn, visualization techniques have been used to display, explore and understand the data, and some factors that influence the rental price of homes on Airbnb in Madrid have been identified.

In addition, an automatic learning model has been trained to predict the rental price of a home on Airbnb in Madrid based on its characteristics. A Fast Machine Learning technique has been used to improve the accuracy of the model quickly. The trained model has proven to be effective in price prediction and provides a useful tool for homeowners and travelers looking to book a home on Airbnb in Madrid.

--- 

## WEB APP STREAMLIT: 
In the following links you can take a look at the app created for this project in Streamlit.

### [SEE THE APP](https://silvilio-eda-ml-prediction-madrid-airbnb-madrid-app-izk2tg.streamlit.app/)
### [SEE THE APP CODE](https://github.com/silvilio/EDA-ML-Prediction-Madrid/blob/main/airbnb_madrid_app.py)

Here you can see a preview of what you can find inside the Streamlit app.

![](https://github.com/silvilio/EDA-ML-Prediction-Madrid/blob/main/Im%C3%A1genes/app.gif)

---

## MACHINE LEARNING
In this project, the Fast Machine Learning method has been chosen to train a prediction model accurately and reducing the training time.
Of all the different models this system tested, the best model turned out to be the <b>Light Gradient Boosting Machine (LightGBM)</b>.
Because? Of all, it was the one with the smallest mean absolute error (MAE) and the smallest mean square error (MSE). In addition, it also had the best performance in the coefficient of determination (R2).

### Model: Light Gradient Boosting Machine (LightGBM)
Light Gradient Boosting Machine (LightGBM) is a supervised machine learning algorithm. In this case, we use it to predict the rental price of Airbnb properties in Madrid. This is accomplished by training the model on data from the dataset, such as reviews, neighborhood, room type, minimum night nights, and availability.

Once trained, the model can predict the price of an Airbnb rental based on its characteristics and input data. This can help landlords set realistic rental prices for their Airbnb listings.

<img src="https://github.com/silvilio/EDA-ML-Prediction-Madrid/blob/main/Im%C3%A1genes/captura3.PNG" alt="Classification" style="width: 50%; height: auto;" />

A value of 0.4816 for R2 indicates that the model explains approximately 48% of the variability in Airbnb apartment prices. It can be said that the model has a good predictability with an R2 close to 0.5, indicating that the model explains around 50% of the variability in Airbnb apartment prices.

<img src="https://github.com/silvilio/EDA-ML-Prediction-Madrid/blob/main/Im%C3%A1genes/captura1.PNG" alt="Classification" style="width: 50%; height: auto;" />

Furthermore, the errors obtained are acceptable, with a MAE and RMSE of 19.3011 and 26.6900 respectively, which suggests that the model behaves in a stable and consistent manner in its price prediction. A value of 19.3011 means that, on average, the model is predicting the price of Airbnb apartments with an error of 19.3011 currency units.

<img src="https://github.com/silvilio/EDA-ML-Prediction-Madrid/blob/main/Im%C3%A1genes/captura2.PNG" alt="Classification" style="width: 50%; height: auto;" />

In summary, the LightGBM model is a good fit for the project and can be considered a suitable option for Airbnb apartment price prediction. You can continue to investigate other modeling techniques or improve the features to further improve the performance of the model.

---

### [DOWNLOAD DATASET](https://github.com/silvilio/EDA-ML-Prediction-Madrid/blob/main/airbnb_anuncios.csv)
Here you can download the dataset used for the project.




# Spanish

Este proyecto es un análisis exploratorio de datos (EDA) de Airbnb en Madrid, con el objetivo de identificar patrones y tendencias en los precios de alquiler. Se han recopilado y preprocesado datos de diversas características de las viviendas, como la ubicación, la disponibilidad y la cantidad de comentarios. A su vez, se ha utilizado técnicas de visualización para mostrar, explorar y comprender los datos, y se han identificado algunos factores que influyen en el precio de alquiler de las viviendas en Airbnb en Madrid.

Además, se ha entrenado un modelo de aprendizaje automático para predecir el precio de alquiler de una vivienda en Airbnb en Madrid según sus características. Se ha utilizado una técnica de Fast Machine Learning para mejorar la precisión del modelo de forma rápida. El modelo entrenado ha demostrado ser efectivo en la predicción de precios y proporciona una herramienta útil para los propietarios de viviendas y los viajeros que buscan reservar una vivienda en Airbnb en Madrid.


--- 

## WEB APP STREAMLIT: 
En los siguientes enlaces puedes echar un vistazo a la app creada para este proyecto en Streamlit. 

### [VER LA APP](https://silvilio-eda-ml-prediction-madrid-airbnb-madrid-app-izk2tg.streamlit.app/)
### [VER EL CÓDIGO DE LA APP](https://github.com/silvilio/EDA-ML-Prediction-Madrid/blob/main/airbnb_madrid_app.py)

Aquí puedes ver un adelanto de lo que te puedes encontrar dentro de la app de Streamlit.

![](https://github.com/silvilio/EDA-ML-Prediction-Madrid/blob/main/Im%C3%A1genes/app.gif)

---

## MACHINE LEARNING
En este proyecto se ha elegido usar el método de Fast Machine Learning para entrenar un modelo de predicción de manera precisa y reduciendo el tiempo de entrenamiento.
De todos los diferentes modelos que analizó este sistema, el mejor modelo resultó ser <b>Light Gradient Boosting Machine (LightGBM)</b>.
¿Por qué? De todos era el que tenía el menor error medio absoluto (MAE) y el menor error cuadrático medio (MSE). Además, también tenía el mejor rendimiento en el coeficiente de determinación (R2).

### Model: Light Gradient Boosting Machine (LightGBM)
Light Gradient Boosting Machine (LightGBM) es un algoritmo de aprendizaje automático supervisado. En este caso, lo usamos para predecir el precio de alquiler de las propiedades de Airbnb en Madrid. Esto se logra mediante el entrenamiento del modelo con los datos del dataset, como las reviews, el barrio, el tipo de habitación, el número de noches mínimas y la disponibilidad.

Una vez entrenado, el modelo puede predecir el precio de un alquiler de Airbnb según sus características y datos de entrada. Esto puede ayudar a los propietarios a establecer precios de alquiler realistas para sus propiedades de Airbnb.

<img src="https://github.com/silvilio/EDA-ML-Prediction-Madrid/blob/main/Im%C3%A1genes/captura3.PNG" alt="Classification" style="width: 50%; height: auto;" />

Un valor de 0.4816 para el R2 indica que el modelo explica aproximadamente el 48% de la variabilidad de los precios de los pisos de Airbnb. Se puede decir que el modelo tiene una buena capacidad de predicción con un R2 cercano a 0.5, lo que indica que el modelo explica alrededor del 50% de la variabilidad en los precios de los pisos de Airbnb.

<img src="https://github.com/silvilio/EDA-ML-Prediction-Madrid/blob/main/Im%C3%A1genes/captura1.PNG" alt="Classification" style="width: 50%; height: auto;" />

Además, los errores obtenidos son aceptables, con un MAE y RMSE de 19.3011 y 26.6900 respectivamente, lo que sugiere que el modelo se comporta de manera estable y consistente en su predicción de precios. Un valor de 19.3011 significa que, en promedio, el modelo está prediciendo el precio de los pisos de Airbnb con un error de 19.3011 unidades monetarias.

<img src="https://github.com/silvilio/EDA-ML-Prediction-Madrid/blob/main/Im%C3%A1genes/captura2.PNG" alt="Classification" style="width: 50%; height: auto;" />

En resumen, el modelo LightGBM es un buen ajuste para el proyecto y se puede considerar una opción adecuada para la predicción de precios de pisos de Airbnb. Se pueden seguir investigando otras técnicas de modelado o mejorando los features para mejorar aún más el desempeño del modelo.

---

### [DESCARGA DATASET](https://github.com/silvilio/EDA-ML-Prediction-Madrid/blob/main/airbnb_anuncios.csv)
Aquí puedes descargar el dataset utilizado para el proyecto.

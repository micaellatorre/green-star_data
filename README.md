# **Green Star Data**  

**Green Star Data** es un repositorio dedicado al desarrollo de modelos de **machine learning** para la predicción del rendimiento en cultivos de **cannabis medicinal**. Forma parte del ecosistema de [**Green Star**](https://www.green-star.app), una aplicación diseñada para la recopilación y análisis de datos de ciclos de cultivo, con el objetivo de ofrecer información valiosa a cultivadores y facilitar la toma de decisiones basadas en datos.  

Este proyecto se centra en la creación de un **dataset estructurado** a partir de datos históricos y de cultivadores reales, aplicando técnicas avanzadas de **preprocesamiento**, **oversampling** y **modelado predictivo** para abordar la tarea de clasificación del rendimiento.  

## **📁 Estructura del Proyecto**

El repositorio está organizado en los siguientes directorios clave:  

green-star_data/<br/>
│<br/>
├── data/<br/>
│&emsp;├── history/                  &emsp;# Historial de datasets utilizados<br/>
│&emsp;└── preprocessed/             &emsp;# Historial de datasets preprocesados<br/>
│<br/>
├── scripts/<br/>
│&emsp;├── preprocessing/                &emsp;# Limpieza y preprocesamiento del dataset<br/>
│&emsp;│&emsp;├── user_processing.py        &emsp;# Identificador único autoincremental del usuario<br/>
│&emsp;│&emsp;├── tipo_de_simulacion.py     &emsp;# Numerar el tipo de simulación<br/>
│&emsp;│&emsp;├── cultivador_rating.py      &emsp;# Cálculo del puntaje del cultivador<br/>
│&emsp;│&emsp;├── geolocation_processing.py &emsp;# Desgloce de lat y lon<br/>
│&emsp;│&emsp;├── dli_calc.py               &emsp;# Cálculo de DLI por etapa del cultivo<br/>
│&emsp;│&emsp;├── var_coding.py             &emsp;# Codificación de variables categóricas<br/>
│&emsp;│&emsp;├── dates_transform.py        &emsp;# Transformación de fechas a características numéricas<br/>
│&emsp;│&emsp;├── categorize_yield.py       &emsp;# Categorizar la variable objetivo<br/>
│&emsp;│&emsp;└── main.py<br/>
│&emsp;│<br/>
│&emsp;├── oversampling/             &emsp;# Técnicas de oversampling<br/>
│&emsp;│&emsp;├── random_oversampling.py&emsp;# Random Oversampling sencillo<br/>
│&emsp;│&emsp;├── smote.py              &emsp;# SMOTE (Synthetic Minority Oversampling Technique)<br/>
│&emsp;│&emsp;├── adasyn.py             &emsp;# ADASYN (Adaptive Synthetic Sampling)<br/>
│&emsp;│&emsp;├── cluster_based.py      &emsp;# Cluster-Based Oversampling<br/>
│&emsp;│&emsp;├── knn_interpolation.py  &emsp;# KNN Interpolation<br/>
│&emsp;│&emsp;└── main.py<br/>
│&emsp;│<br/>
│&emsp;├── training/                 &emsp;# Modelos de Entrenamiento<br/>
│&emsp;│&emsp;├── linear_regression.py  &emsp;# Entrenamiento con regresión lineal<br/>
│&emsp;│&emsp;├── random_forest.py      &emsp;# Entrenamiento con Random Forest<br/>
│&emsp;│&emsp;├── xgboost.py            &emsp;# Entrenamiento con XGBoost<br/>
│&emsp;│&emsp;└── main.py<br/>
│&emsp;│<br/>
│&emsp;└── analysis/                     &emsp;# Scripts de evaluación<br/>
│&emsp;&nbsp;&emsp;├── comparative_analysis.py   &emsp;# Comparación de métricas entre técnicas de oversampling<br/>
│&emsp;&nbsp;&emsp;├── feature_importance.py     &emsp;# Evaluación de los campos más relevantes para RF y XGB<br/>
│&emsp;&nbsp;&emsp;├── svm_feature_importance.py &emsp;# Evaluación de los campos más relevantes para SVM<br/>
│&emsp;&nbsp;&emsp;├── model_evaluation.py       &emsp;# Evaluación de métricas y matrices de confusión<br/>
│&emsp;&nbsp;&emsp;└── visualization.py          &emsp;# Ploteo de las métricas comparativas<br/>
│<br/>
├── outputs/<br/>
│&emsp;├── oversampled/              &emsp;# Resultados para cada técnica de oversampling<br/>
│&emsp;│&emsp;├── random/<br/>
│&emsp;│&emsp;├── smote/<br/>
│&emsp;│&emsp;├── adasyn/<br/>
│&emsp;│&emsp;└── cluster_based/<br/>
│&emsp;│<br/>
│&emsp;├── trained/                  &emsp;# Resultados del entrenamiento para cada técnica<br/>
│&emsp;│&emsp;├── random_forest/<br/>
│&emsp;│&emsp;├── svm/<br/>
│&emsp;│&emsp;└── xgboost/<br/>
│&emsp;│<br/>
│&emsp;├── figures/                  &emsp;# Gráficos generados<br/>
│&emsp;└── metrics/                  &emsp;# Métricas de evaluación<br/>
│<br/>
└── README.md                     &emsp;# Descripción del proyecto<br/>

## **🔬 Técnicas Implementadas**  

### **📌 Preprocesamiento de Datos**  
✔️ Normalización y transformación de variables  
✔️ Eliminación de valores atípicos  
✔️ Codificación de variables categóricas  

### **📌 Oversampling**  
✔️ **Random Oversampling**  
✔️ **SMOTE (Synthetic Minority Oversampling Technique)**  
✔️ **ADASYN (Adaptive Synthetic Sampling)**  
✔️ **Cluster-Based Oversampling**  
✔️ **KNN Interpolation**

### **📌 Modelos de Machine Learning**  
✔️ **Random Forest**  
✔️ **Support Vector Machine (SVM)**  
✔️ **XGBoost**  

### **📌 Evaluación y Comparación**  
✔️ **Análisis de importancia de variables**  
✔️ **Matrices de confusión**  
✔️ **Métricas de rendimiento**: Accuracy, Precision, Recall, F1-Score  

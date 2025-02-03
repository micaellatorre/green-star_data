### **Green Star Data**  

**Green Star Data** es un repositorio dedicado al desarrollo de modelos de **machine learning** para la predicción del rendimiento en cultivos de **cannabis medicinal**. Forma parte del ecosistema de **Green Star**, una aplicación diseñada para la recopilación y análisis de datos de ciclos de cultivo, con el objetivo de ofrecer información valiosa a cultivadores y facilitar la toma de decisiones basadas en datos.  

Este proyecto se centra en la creación de un **dataset estructurado** a partir de datos históricos y de cultivadores reales, aplicando técnicas avanzadas de **preprocesamiento**, **oversampling** y **modelado predictivo** para abordar la tarea de clasificación del rendimiento.  

### **Estructura del Proyecto**  

El repositorio está organizado en los siguientes directorios clave:  

green-star_data/
│
├── data/
│   ├── history/                    # Historial de datasets utilizados
│   └── preprocessed/               # Historial de datasets preprocesados
│   
├── scripts/
│   ├── preprocessing/                  # Limpieza y preprocesamiento del dataset
│   │   ├── user_processing.py          # Identificador único autoincremental del usuario
│   │   ├── tipo_de_simulacion.py       # Numerar el tipo de simulación
│   │   ├── cultivador_rating.py        # Cálculo del puntaje del cultivador
│   │   ├── geolocation_processing.py   # Desgloce de lat y lon
│   │   ├── dli_calc.py                 # Cálculo de DLI por etapa del cultivo
│   │   ├── var_coding.py               # Codificación de variables categóricas
│   │   ├── dates_transform.py          # Transformación de fechas a características numéricas
│   │   ├── categorize_yield.py         # Categoriazar la variable objetivo
│   │   └── main.py
│   │
│   ├── oversampling/               # Tecnicas de oversampling
│   │   ├── random_oversampling.py  # Random Oversampling sencillo
│   │   ├── smote.py                # SMOTE (Synthetic Minority Oversampling Technique)
│   │   ├── adasyn.py               # ADASYN (Adaptive Synthetic Sampling)
│   │   ├── cluster_based.py        # Cluster-Based Oversampling
│   │   ├── knn_interpolation.py    # KNN Interpolation
│   │   └── main.py
│   │
│   ├── training/                   # Modelos de Entrenamiento
│   │   ├── linear_regression.py    # Entrenamiento con regresión lineal
│   │   ├── random_forest.py        # Entrenamiento con Random Forest
│   │   ├── xgboost.py              # Entrenamiento con XGBoost
│   │   └── main.py
│   │
│   └── analysis/                       # Scripts de evaluación
│       ├── comparative_analysis.py     # Comparación de métricas entre técnicas de oversampling
│       ├── feature_importance.py       # Evaluación de los campos mas relevantes para RF y XGB
│       ├── svm_feature_importance.py   # Evaluación de los campos mas relevantes para SVM
│       ├── model_evaluation.py         # Evaluación de métricas y matrices de confusión
│       └── visualization.py            # Ploteo de las metricas comparativas
│
├── outputs/
│   ├── oversampled/                # Resultados para cada tecnica de oversampling
│   │   ├── random/
│   │   ├── smote/
│   │   ├── adasyn/
│   │   └── cluster_based/
│   │
│   ├── trained/                    # Resultados del entrenamiento para cada tecnica
│   │   ├── random_forest/
│   │   ├── svm/
│   │   └── xgboost/
│   │
│   ├── figures/                    # Gráficos generados
│   └── metrics/                    # Métricas de evaluación
│
└── README.md                       # Descripción del proyecto

### **Técnicas Implementadas**  

- **Preprocesamiento de Datos:** Normalización, eliminación de outliers y transformación de variables.  
- **Oversampling:** Aplicación de **SMOTE, ADASYN y Cluster-Based Oversampling** para balancear las clases.  
- **Entrenamiento de Modelos:** Evaluación de distintos enfoques de clasificación (**Random Forest, SVM, XGBoost**).  
- **Evaluación y Comparación:** Métricas como **Accuracy, Precision, Recall y F1-Score**, además de análisis de importancia de variables y matrices de confusión.  

### **Integración con Green Star**  

Los modelos entrenados en **Green Star Data** serán integrados en la aplicación **Green Star** mediante una **API**, permitiendo:  

- La **predicción automática** del rendimiento de un cultivo en función de sus características.  
- La generación de **recomendaciones personalizadas** para mejorar el rendimiento.  
- La posibilidad de escalar el modelo con **datos en tiempo real** y sensores IoT en el futuro.  

Este proyecto representa un paso significativo hacia la aplicación de **inteligencia artificial en la agricultura de precisión**, optimizando la producción de cannabis medicinal mediante herramientas basadas en datos.

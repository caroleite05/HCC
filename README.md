# HCC

### ***PREDICTION ABOUT THE SURVIVAL OF PATIENTS WITH HEPATOCELLULAR CARCINOMA***

<img width="669" alt="Captura de ecrã 2024-05-21, às 21 08 59" src="https://github.com/caroleite05/HCC/assets/166618304/02f97056-fa55-4117-b0ed-1d78d501a2ed">

<br>
<br>

***Introduction***
<br>
HCC (hepatocellular carcinoma) is the most common and serious type of liver cancer and originates in the liver cells (liver parenchymal cells). Therefore, more effective screening and early diagnosis of this disease are necessary to reduce its potential risks and save patients' lives. To this end, our project is developing supervised learning techniques to better understand the important variables to consider and thus predict patient survival. 

To this end, we used several algorithms and methods. We performed a detailed data analysis, including preprocessing, exploratory analysis, and target definition. For classification, we applied the KNN and Decision Tree algorithms, and to address class imbalances, we applied the SMOTE technique. Furthermore, we tested with different data configurations and divided the data into training and test sets for validation. The importance of variables was assessed to understand which characteristics most influence patient survival. We also performed a visual comparison of the results obtained with KNN and Decision Tree, using graphs to interpret the models' performance. Finally, we adjusted the parameters (tuning) to optimize the algorithms' performance.

<br>

***Files used:***
  - **hcc_dataset.csv:** initial data set
  - **hcc_dataset_filled.csv:** already filled data set
  - **HCC.ipynb:** code implemented with the applied models
  - **app.py:** implementation of an application to predict whether a person will "die" or "live" after 1 year of diagnosis according to their data

<br>

***Requirements:***
To run the program, it's recommended to use the Anaconda environment, so that the project view can contain the Python libraries used in its development. These libraries are:
  - Pandas
  - Numpy
  - Scikit-learn
  - Matplotlib e searborn
  - Jupyter notebook

To access the forecast application, you must type the following command in the terminal:
<br>
   > **streamlit run app.py**

<br>

***References***
<br>
DR-SALCEDO. GitHub - Dr-Salcedo/hepatocellular_carcinoma_one_year_survival: Classification model for 1 year survival rates in patients with HCC (hepatocellular carcinoma). Available at: <https://github.com/Dr-Salcedo/hepatocellular_carcinoma_one_year_survival>. Accessed on: September 28, 2025..

<br>

## Authors 

* **Beatriz Pereira** - *Bioinformatics - FCUP* - [Beapereirax](https://github.com/Beapereirax) 
* **Carolina Leite** - *Bioinformatics - FCUP* - [caroleite05](https://github.com/caroleite05)
* **Inês Santos** - *Bioinformatics - FCUP* - [up202305589](https://github.com/up202305589)

<br>

## Link to the course:
This course is part of the **second semester** of the **first year** of the **Bachelor's Degree in Bioinformatics** at **FCUP, ICBAS and FFUP** in the academic year 2023/2024. You can find more information about this course at the following link:

###

[![Link to Course](https://img.shields.io/badge/Link%20to%20Course-blue?style=for-the-badge)](https://sigarra.up.pt/fcup/pt/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=529873) <br>
[![FCUP](https://img.shields.io/badge/FCUP-lightgrey?style=for-the-badge)](https://www.up.pt/fcup/pt/)
[![ICBAS](https://img.shields.io/badge/ICBAS-lightgrey?style=for-the-badge)](https://www.up.pt/icbas/pt/)
[![FFUP](https://img.shields.io/badge/FFUP-lightgrey?style=for-the-badge)](https://sigarra.up.pt/ffup/pt/web_page.Inicial)

###


*Elementos de Inteligência Artificial e Ciência de Dados - FCUP - 2023/2024*

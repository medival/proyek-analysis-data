## Aotizhongxin Air Quality and Weather Dashboard

### File Structures
```
.
├── dashboard
│   ├── dashboard.py
│   └── data_aotizhongxin.csv
├── data
|   └── data_aotizhongxin.csv
├── screenshots
|   ├── Screenshots (91).png
|   ├── Screenshots (92).png
|   ├── Screenshots (93).png
|   └── Screenshots (94).png
├── README.md
├── notebook.ipynb
└── requirements.txt
```
### Analysis
  1. Data Wrangling
     - Gathering Data
     - Assessing Data
     - Cleaning Data
  2. Exploratory Data Analysis (EDA)
     - Statistik Dataset
     - Explore Statistik Rata Rata Arah Mata Angin per Tahun
     - Korelasi Matrix Antar Fitur
     - Statistik Polutan
     - Statistik Polusi Per Bulan
     - Statistik Distribusi Arah Angin
     - Statistik Kecepatan Angin
     - Statistik Outlier Pada Polutan
  3. Visualisasi & Explanatory Analysis
     - Pertanyaan 1
     - Pertanyaan 2
     - Pertanyaan 3

### Getting Started
#### Setup Environment - Shell/Terminal
```
cd submisson
pipenv install
pipenv shell
pip install -r requirements.txt
```

#### Run steamlit app
```
streamlit run dashboard.py
```

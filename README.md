# Netflix Recommendation System

A hybrid movie recommendation system built using the Netflix Prize Dataset. The project combines Item-Based Collaborative Filtering (KNN) and Singular Value Decomposition (SVD) to generate personalized movie recommendations.

## Live Dashboard

🔗 https://z3robyte18-netflix-recommendation-system-app-hjkorv.streamlit.app/

---

# Repository Contents

## Data Processing Pipeline

- Raw Netflix data parsing
- Data cleaning and preprocessing
- User and movie filtering
- Dataset export

## Model Training Pipeline

- Item-Based Collaborative Filtering (KNN)
- Singular Value Decomposition (SVD)
- Hybrid Recommendation Model

## Evaluation Scripts

Models are evaluated using:

- RMSE (Root Mean Squared Error)
- MAP@10 (Mean Average Precision @10)

## Recommendation Generation Module

- Top-N movie recommendations
- Hybrid recommendation scoring
- Explainable recommendations

---

# Results

| Model | RMSE | MAP@10 |
|---------|---------|---------|
| ItemCF | 1.0062 | - |
| SVD | 0.9403 | 0.7347 |
| Hybrid | 0.9385 | 0.7350 |

**Best Model:** Hybrid Recommendation System

---

# Repository Structure

```text
Netflix-Recommendation-System/
├── app.py
├── README.md
├── requirements.txt
├── results.json
├── knn_model.pkl
├── svd_model.pkl
├── netflix_filtered.csv
├── movie_titles.csv
├── model_comparison.csv
├── top_recommendations.csv
├── explainable_recommendations.csv
├── hybrid_recommendations.csv
└── Netflix_Recommendation_System.ipynb
```

---


#  How to Reproduce Results

### Option 1: Use the Live Dashboard

Access the deployed application directly:

🔗 **Live Dashboard:**  
https://z3robyte18-netflix-recommendation-system-app-hjkorv.streamlit.app/

### Option 2: Run Locally

#### Clone Repository

```bash
git clone https://github.com/z3robyte18/Netflix-Recommendation-System.git
```

#### Navigate to Project Directory

```bash
cd Netflix-Recommendation-System
```

#### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Run the Notebook

Open and execute:

```text
Netflix_Recommendation_System.ipynb
```

#### Launch Dashboard

```bash
streamlit run app.py
```

---


#  Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Surprise
- Streamlit
- Matplotlib
- Pickle
- Git
- GitHub


---

#  Author Details

- **Name:** Himani Rohaj
- **Program:** BS-MS (Mathematics and Computing), IIT Roorkee
- **Project Type:** Machine Learning + Recommendation Systems + Web Application
- **GitHub:** https://github.com/z3robyte18



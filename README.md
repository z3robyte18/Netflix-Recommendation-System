#  Netflix Recommendation System

A Hybrid Recommendation System built using the Netflix Prize Dataset that combines:

- Item-Based Collaborative Filtering (KNN)
- Matrix Factorization (SVD)
- Hybrid Recommendation Engine
- Explainable Recommendations
- Interactive Streamlit Dashboard

The objective of this project is to generate personalized movie recommendations for users by leveraging collaborative filtering and latent factor models while evaluating performance using RMSE and MAP@10 metrics.

---

##  Project Overview

Recommendation systems are a core component of modern streaming platforms such as Netflix, Amazon Prime, and Disney+.

This project implements and compares multiple recommendation approaches:

1. Item-Based Collaborative Filtering (KNN)
2. Singular Value Decomposition (SVD)
3. Hybrid Recommendation Model

The final hybrid model combines the strengths of both approaches to improve recommendation quality and ranking performance.

---

##  Dataset

### Netflix Prize Dataset

The Netflix Prize dataset contains movie ratings provided by Netflix users.

Dataset Characteristics:

| Metric | Value |
|----------|----------|
| Users | 404,478 |
| Movies | 17,770 |
| Ratings | 100 Million+ |
| Rating Scale | 1–5 |

For computational efficiency, a filtered subset of approximately 5 million ratings was used.

### Data Files

- combined_data_1.txt
- combined_data_2.txt
- combined_data_3.txt
- combined_data_4.txt
- movie_titles.csv

---

##  Data Processing Pipeline

The following preprocessing steps were performed:

### Step 1: Raw Data Parsing

Netflix data is stored in a custom format.

Converted raw files into structured records:

- UserID
- MovieID
- Rating
- Date

### Step 2: Data Cleaning

- Removed invalid records
- Handled missing values
- Converted dates to datetime format

### Step 3: Filtering

To reduce sparsity:

- Retained users with at least 5 ratings
- Retained movies with at least 50 ratings

### Step 4: Dataset Export

Generated:

- netflix_5m.csv
- netflix_filtered.csv

---

##  Model Training Pipeline
### 1. Item-Based Collaborative Filtering (ItemCF)

**Algorithm:** KNNBasic with Cosine Similarity

```python
from surprise import KNNBasic

sim_options = {
    "name": "cosine",
    "user_based": False
}

knn_model = KNNBasic(sim_options=sim_options)
```

#### Advantages

- Easy to interpret
- Finds similar movies
- Generates intuitive recommendations

#### Limitations

- Struggles with sparse data
- Suffers from cold-start problems
- Similarity computation becomes expensive for large datasets

### 2. Singular Value Decomposition (SVD)

**Algorithm:**

```python
from surprise import SVD

svd_model = SVD(
    n_factors=100,
    n_epochs=20,
    random_state=42
)
```

#### Advantages

- Learns latent user preferences
- Handles sparse data effectively
- Produces more accurate recommendations
- Captures hidden relationships between users and movies

#### Limitations

- Less interpretable than neighborhood-based methods
- Requires retraining when new ratings are added
- Computationally expensive during training


### 3. Hybrid Recommendation Model

**Final Prediction:**

```python
hybrid_score = (
    0.7 * svd_prediction +
    0.3 * itemcf_prediction
)
```

**Hybrid Score = 0.7 × SVD + 0.3 × ItemCF**

This combines:

- Latent preference learning from SVD
- Neighborhood-based similarity from KNN

#### Advantages

- Better prediction accuracy
- Improved recommendation quality
- Combines strengths of both models



# Evaluation

## Metrics Used

1. RMSE (Root Mean Squared Error)
2. MAP@10 (Mean Average Precision @10)

---

## RMSE Comparison

| Model | RMSE |
|--------|--------|
| Item-Based CF | 1.0062 |
| SVD | 0.9403 |
| Hybrid | 0.9385 |

---

## MAP@10 Comparison

| Model | MAP@10 |
|--------|--------|
| SVD | 0.7347 |
| Hybrid | 0.7350 |




# Results

## Best Model

**Hybrid Recommendation System**

**Performance:**

- RMSE = **0.9385**
- MAP@10 = **0.7350**

The hybrid model achieved the lowest prediction error and the highest recommendation ranking quality.

---

# Sample Recommendations

**For User ID: 1488844**

| Movie | Hybrid Score |
|--------|--------|
| ABC Primetime: Mel Gibson's The Passion of the Christ | 4.05 |
| Dil Chahta Hai | 3.95 |
| Lord of the Rings: Return of the King | 3.88 |
| Monarch of the Glen: Series 2 | 3.84 |
| Homicide: Life on the Street: Season 7 | 3.84 |

---



# Explainable Recommendations

### Example

**Dil Chahta Hai**

**Recommended because:**

- Similar users rated it highly
- Strong latent preference match identified by SVD
- High hybrid recommendation score

This improves transparency and user trust.

---




# Dashboard

An interactive Streamlit dashboard was developed to visualize model performance and recommendations.

### Features

- Dataset overview
- Model comparison (ItemCF, SVD, Hybrid)
- RMSE and MAP@10 performance metrics
- Top movie recommendations
- Explainable recommendation module
- Hybrid model evaluation summary

### Live Dashboard

🔗 **Deployed Application:**  
https://z3robyte18-netflix-recommendation-system-app-hjkorv.streamlit.app/

### Run Locally

```bash
streamlit run app.py
```


---


#  Repository Structure

```text
Netflix-Recommendation-System/
│
├── app.py                              # Streamlit dashboard
├── README.md                           # Project documentation
├── requirements.txt                    # Dependencies
├── results.json                        # Evaluation results
│
├── knn_model.pkl                       # ItemCF model (Git LFS)
├── svd_model.pkl                       # SVD model (Git LFS)
│
├── movie_titles.csv                    # Movie metadata
├── netflix_filtered.csv                # Processed Netflix dataset
│
├── model_comparison.csv                # RMSE & MAP@10 comparison
├── top_recommendations.csv             # Top recommendations
├── explainable_recommendations.csv     # Explainability outputs
├── hybrid_recommendations.csv          # Hybrid model predictions
│
└── Netflix_Recommendation_System.ipynb # Complete pipeline
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


#  Future Improvements

- Neural Collaborative Filtering
- Content-Based Filtering
- Real-Time Recommendation API
- Personalized User Profiles
- Advanced Explainability Features
- Cloud Deployment (AWS/GCP)
- Interactive Dashboard Enhancements


#  Key Achievements

- Processed and analyzed Netflix Prize dataset
- Built Item-Based Collaborative Filtering model
- Implemented Matrix Factorization using SVD
- Developed a Hybrid Recommendation Engine
- Achieved RMSE of 0.9385
- Achieved MAP@10 of 0.7350
- Generated explainable recommendations
- Built and deployed an interactive Streamlit dashboard


#  Author Details

- **Name:** Himani Rohaj
- **Program:** BS-MS (Mathematics and Computing), IIT Roorkee
- **Project Type:** Machine Learning + Recommendation Systems + Web Application
- **GitHub:** https://github.com/z3robyte18


---

#  Conclusion

This project demonstrates the design and implementation of a hybrid movie recommendation system using Item-Based Collaborative Filtering and Singular Value Decomposition (SVD) on the Netflix Prize dataset. By combining neighborhood-based recommendations with latent factor modeling, the hybrid approach achieved superior performance with an RMSE of **0.9385** and a MAP@10 of **0.7350**.

The project also includes explainable recommendations and a deployed Streamlit dashboard, making the system both effective and user-friendly. The results highlight the advantages of hybrid recommendation systems in improving recommendation accuracy and ranking quality.

---

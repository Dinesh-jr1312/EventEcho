# 🎉 EventEcho – AI-Powered Event Planning Assistant

EventEcho is an AI-powered event planning assistant that combines a recommender system with a Large Language Model (LLM) to help users generate complete event plans based on their preferences.

This project was developed for the CAIE (Computing Applications in Artificial Intelligence) module.

---

## 🚀 Live Demo

You can try the live application here:  
👉 **https://ginette-unisolationist-nonconsumptively.ngrok-free.dev**

---

## ✨ Features

- **Real-World Vendor Dataset**: Cleaned and engineered dataset with 680+ vendors across multiple categories
- **TF-IDF Recommender System**: Intelligent text-based recommendation engine using scikit-learn
- **HuggingFace LLM Integration**: Powered by Microsoft Phi-3 model for creative event planning
- **Interactive Web UI**: Built with Gradio for seamless user interaction
- **End-to-End AI Pipeline**: Complete journey from query → recommendations → intelligent plan generation
- **Budget Estimation**: Smart cost breakdown based on event type and guest count
- **Persistent Booking System**: CSV-based storage for event bookings

---

## 🧠 System Architecture

```
User Input (Event Details)
        ↓
TF-IDF Vectorization & Query Processing
        ↓
Cosine Similarity-based Vendor Ranking
        ↓
Top 5 Vendor Recommendations
        ↓
LLM Prompt Engineering
        ↓
Creative Event Plan Generation
        ↓
Formatted Output (Plan + Budget + Vendors)
```

**AI Components:**
1. **Content-Based Recommender**: TF-IDF vectorization with cosine similarity
2. **LLM Integration**: HuggingFace Inference API with few-shot prompting
3. **Smart Budget Estimation**: Dynamic cost calculation based on event parameters

---

## 📁 Project Structure

```
EventEcho/
├── app.py                          # Main Gradio application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── data/
│   ├── vendors_final.csv           # Full dataset (680+ vendors)
│   ├── sample_vendors.csv          # Sample dataset for demo (50 vendors)
│   └── raw/                        # Original raw datasets
│       ├── Catering_Dataset.csv
│       ├── chefmozaccepts.csv
│       ├── chefmozcuisine.csv
│       └── ... (other source files)
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb      # Data preprocessing & EDA
│   ├── 02_recommender.ipynb        # TF-IDF model development
│   └── 03_llm_integration.ipynb     # LLM integration notebook
│
├── src/                            # Utility modules (optional)
│
└── screenshots/                    # UI demonstration images
    ├── ui_demo.png
    ├── example_output.png
    └── budget_breakdown.png
```

---

## ⚙️ How to Run Locally

### Prerequisites
- Python 3.9+
- pip or conda

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/EventEcho.git
cd EventEcho
```

### 2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add HuggingFace API Token

Open `app.py` and update line 60 with your HuggingFace token:

```python
client = InferenceClient(
    model="microsoft/Phi-3-mini-4k-instruct",
    token="your_hf_token_here"
)
```

Get your free token from: https://huggingface.co/settings/tokens

### 5. Run the Application
```bash
python app.py
```

The app will launch at: **http://127.0.0.1:7860**

### 6. (Optional) Create Public URL with ngrok
```bash
pip install pyngrok
python -c "from pyngrok import ngrok; print(ngrok.connect(7860))"
```

---

## 📊 Dataset Overview

The dataset consists of **cleaned and merged public vendor datasets** including:

- **Categories**: Catering, Wedding Venues, Event Planning, Entertainment
- **Data Sources**: 
  - Catering_Dataset.csv
  - Chef Moz restaurant data (cuisines, hours, parking, payment)
  - Venues for event bookings
  - User reviews and ratings

**Key Fields:**
- `name`: Vendor business name
- `category`: Service category (catering, venue, etc.)
- `location`: Geographic location
- `rating`: Customer rating
- `services`: Detailed service description

**Data Cleaning Pipeline:**
- Removed duplicates
- Handled missing values
- Standardized location formats
- Merged multiple data sources
- Removed outliers

📥 **Sample Dataset**: For easy testing, `data/sample_vendors.csv` contains 50 diverse vendors representing all categories.

---

## 🧪 Example Usage

### Input:
```
Event Type: Wedding
Guests: 150
Budget Level: Standard
Location: City Center
Special Requests: "Elegant outdoor ceremony with garden theme"
```

### System Returns:

**1. Recommended Vendors:**
```
• The Garden Venue (Wedding Venue) - City Center
• Elegant Catering Co. (Catering) - City Center
• Floral Designs Studio (Decorations) - Nearby
• Symphony Band Entertainment (Entertainment) - Available
• Event Planning Pro (Planning) - City Center
```

**2. Creative Event Plan:**
- Event Concept & Theme
- Detailed Timeline (8 weeks to day-of)
- Vendor Coordination Strategy
- Decoration Ideas
- Guest Experience Flow
- Contingency Plans

**3. Budget Breakdown:**
```
Per Guest Cost: $120.00
Total Estimate: $18,000.00

Breakdown:
- Venue/Catering (55%): $9,900
- Decorations (15%): $2,700
- Entertainment (15%): $2,700
- Misc/Contingency (15%): $2,700
```

---

## 🔬 AI/ML Implementation Details

### Recommender System
**Algorithm**: TF-IDF (Term Frequency-Inverse Document Frequency) + Cosine Similarity

```python
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X = vectorizer.fit_transform(df["text"])
similarities = cosine_similarity(query_vector, X)
```

**Why TF-IDF?**
- Captures semantic relevance of vendor descriptions
- Scales well with larger datasets
- Handles multiple vendor attributes (name, category, location, services)
- Computationally efficient for real-time recommendations

### LLM Integration
**Model**: Microsoft Phi-3-mini-4k-instruct (via HuggingFace API)

**Prompting Strategy:**
- Few-shot examples of event plans
- System prompt establishing event planner persona
- Context injection with recommended vendors
- Temperature tuning (0.7) for creative but coherent output

**Capabilities:**
- Creative event conceptualization
- Timeline generation
- Risk mitigation strategies
- Personalized recommendations

---

## 📈 Key Results

✅ **Recommendation Quality**: Tested on diverse event types with relevant vendor matches
✅ **Plan Generation**: Produces comprehensive, actionable event plans  
✅ **User Experience**: Intuitive Gradio interface with real-time responses  
✅ **Scalability**: Efficient performance with 680+ vendors in dataset

---

## ⚠️ Limitations & Future Work

### Current Limitations:
- Free HuggingFace API has rate limits
- Dataset limited to public sources
- Recommendations depend on vendor description quality
- No real-time vendor availability checking
- Simplified budget model

### Future Enhancements:
- Integration with real vendor APIs (Yelp, Google Maps)
- User authentication & saved event history
- Advanced filtering (date availability, certifications)
- Multi-language support
- Deployment on Hugging Face Spaces for permanent public access
- Advanced NLP models (BERT for better semantic understanding)

---

## 🏆 CAIE Assessment Alignment

This project demonstrates:

✅ **Data Engineering**: Real-world dataset cleaning, merging, and preprocessing  
✅ **Machine Learning**: TF-IDF recommender system with similarity metrics  
✅ **AI Integration**: LLM API usage for intelligent plan generation  
✅ **Software Development**: Full-stack application with UI/backend  
✅ **Project Management**: Clear documentation, version control, reproducibility  

---

## 👤 Author

**Dinesh Selva Rajoo**  
CAIE Final Project – January 2026

---

## 📝 License

This project is provided as-is for educational purposes.

---

## 🤝 Contributing

This is a completed CAIE submission. For improvements or extensions, please create a fork of this repository.

---

## 📞 Support

For issues or questions:
1. Check existing GitHub Issues
2. Ensure all dependencies from `requirements.txt` are installed
3. Verify HuggingFace token is valid and has API access
4. Check that data files exist in the `data/` directory

---

**Made with ❤️ for CAIE**

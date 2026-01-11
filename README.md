# 🎓 UC Schools Admission Rankings Dashboard

A beautiful, mobile-friendly Streamlit app for exploring UC admission statistics for California high schools.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)

## ✨ Features

### 📊 Rankings Table
- View top 50 schools ranked by admit rate
- Filter by UC campus (All UC, UC Berkeley, UCLA, UCSD)
- Filter by school type (Public/Private)
- Filter by city
- Color-coded admit rate badges
- Visual progress bars

### 🔍 School Details
- Comprehensive admission statistics
- Demographic breakdown charts
- Applied/Admitted/Enrolled by demographic group
- Interactive visualizations

### ⚖️ Comparison Tool
- Compare 2-3 schools side-by-side
- Visual comparison charts
- Admit rate comparison

### 📈 Analytics
- Top 10 schools by admit rate
- Admit rate distribution histogram
- Public vs Private breakdown
- City-level analysis
- Demographic admit rate comparisons

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   cd streamlitapp
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   Navigate to `http://localhost:8501`

## ☁️ Deploy to Streamlit Cloud

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Add UC Schools Admission Rankings app"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your repository
   - Set the main file path to `streamlitapp/app.py`
   - Click "Deploy"

## 📁 Project Structure

```
streamlitapp/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── data/
│   └── UC_Schools_Admission_Rankings.csv  # Data file
└── .streamlit/
    └── config.toml       # Streamlit configuration
```

## 📱 Mobile Friendly

The app is fully responsive and works great on mobile devices:
- Responsive card layouts
- Touch-friendly controls
- Optimized for small screens

## 🎨 Customization

### Theme
Edit `.streamlit/config.toml` to customize colors:

```toml
[theme]
primaryColor = "#0066CC"
backgroundColor = "#0E1117"
secondaryBackgroundColor = "#1E2530"
textColor = "#FAFAFA"
```

### Data
Replace `data/UC_Schools_Admission_Rankings.csv` with your own data file. The app expects columns like:
- School, City, County, Private_Public, College
- Applied, Admitted, Enrolled, Admit_Rate_%
- Demographic columns (Asian_Applied, Asian_Admitted, etc.)

## 📊 Data Source

This app uses UC admission data for California high schools, including:
- Overall admission statistics
- Demographic breakdowns (Asian, Hispanic/Latinx, White, African American, International, etc.)
- Statistics for different UC campuses (Berkeley, UCLA, UCSD)

## 🛠️ Technologies Used

- **Streamlit** - Web app framework
- **Pandas** - Data manipulation
- **Plotly** - Interactive visualizations
- **Python 3.8+** - Programming language

## 📄 License

MIT License - feel free to use and modify!

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

Made with ❤️ for California students and educators


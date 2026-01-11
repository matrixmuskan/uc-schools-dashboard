"""
UC Schools Admission Rankings Dashboard
A comprehensive Streamlit app for exploring UC admission data
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np


# Page configuration
st.set_page_config(
    page_title="UC Schools Admission Rankings",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for mobile-friendly, modern design
st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main container */
    .main .block-container {
        padding: 1rem 1rem 3rem 1rem;
        max-width: 1400px;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #1a365d 0%, #2c5282 50%, #2b6cb0 100%);
        padding: 2rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }
    
    .main-header h1 {
        color: #fff;
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    .main-header p {
        color: #bee3f8;
        font-size: 1rem;
        margin: 0.5rem 0 0 0;
    }
    
    /* School cards */
    .school-card {
        background: linear-gradient(145deg, #1e2530 0%, #252d3a 100%);
        border-radius: 12px;
        padding: 1.25rem;
        margin-bottom: 1rem;
        border: 1px solid #2d3748;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .school-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        border-color: #4299e1;
    }
    
    .school-name {
        font-size: 1.1rem;
        font-weight: 600;
        color: #fff;
        margin-bottom: 0.5rem;
    }
    
    .school-city {
        font-size: 0.85rem;
        color: #a0aec0;
        margin-bottom: 0.75rem;
    }
    
    .school-stats {
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
        margin-bottom: 0.75rem;
    }
    
    .stat-item {
        background: #2d3748;
        padding: 0.4rem 0.75rem;
        border-radius: 8px;
        font-size: 0.8rem;
    }
    
    .stat-label {
        color: #718096;
        font-weight: 400;
    }
    
    .stat-value {
        color: #fff;
        font-weight: 600;
        margin-left: 0.25rem;
    }
    
    /* Badges */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .badge-public {
        background: linear-gradient(135deg, #276749 0%, #38a169 100%);
        color: #fff;
    }
    
    .badge-private {
        background: linear-gradient(135deg, #744210 0%, #d69e2e 100%);
        color: #fff;
    }
    
    .badge-rate-high {
        background: linear-gradient(135deg, #22543d 0%, #48bb78 100%);
        color: #fff;
    }
    
    .badge-rate-medium {
        background: linear-gradient(135deg, #744210 0%, #ecc94b 100%);
        color: #1a202c;
    }
    
    .badge-rate-low {
        background: linear-gradient(135deg, #742a2a 0%, #fc8181 100%);
        color: #fff;
    }
    
    /* Progress bar */
    .progress-container {
        background: #2d3748;
        border-radius: 10px;
        height: 8px;
        overflow: hidden;
        margin-top: 0.5rem;
    }
    
    .progress-bar {
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
    }
    
    .progress-high {
        background: linear-gradient(90deg, #38a169 0%, #68d391 100%);
    }
    
    .progress-medium {
        background: linear-gradient(90deg, #d69e2e 0%, #f6e05e 100%);
    }
    
    .progress-low {
        background: linear-gradient(90deg, #e53e3e 0%, #fc8181 100%);
    }
    
    /* Filter buttons */
    .stButton > button {
        border-radius: 20px;
        padding: 0.5rem 1.25rem;
        font-weight: 500;
        transition: all 0.2s ease;
        border: 2px solid transparent;
    }
    
    .stButton > button:hover {
        transform: scale(1.02);
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(145deg, #2d3748 0%, #1a202c 100%);
        border-radius: 12px;
        padding: 1.25rem;
        text-align: center;
        border: 1px solid #4a5568;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #63b3ed;
    }
    
    .metric-label {
        font-size: 0.85rem;
        color: #a0aec0;
        margin-top: 0.25rem;
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.25rem;
        font-weight: 600;
        color: #fff;
        margin: 1.5rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #4299e1;
    }
    
    /* Comparison cards */
    .comparison-card {
        background: linear-gradient(145deg, #1e2530 0%, #252d3a 100%);
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid #2d3748;
        height: 100%;
    }
    
    .comparison-header {
        text-align: center;
        padding-bottom: 1rem;
        border-bottom: 1px solid #4a5568;
        margin-bottom: 1rem;
    }
    
    /* Detail modal */
    .detail-section {
        background: #1e2530;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .detail-title {
        font-size: 1rem;
        font-weight: 600;
        color: #63b3ed;
        margin-bottom: 1rem;
    }
    
    /* Mobile responsive */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 1.5rem;
        }
        
        .school-stats {
            flex-direction: column;
            gap: 0.5rem;
        }
        
        .metric-value {
            font-size: 1.5rem;
        }
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: #1a202c;
        padding: 0.5rem;
        border-radius: 12px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #2b6cb0 0%, #4299e1 100%);
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        background: #2d3748;
        border-radius: 8px;
    }
    
    /* Multiselect styling */
    .stMultiSelect > div > div {
        background: #2d3748;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    """Load and preprocess the CSV data"""
    try:
        # Try relative path first (for deployment)
        df = pd.read_csv("data/UC_Schools_Admission_Rankings.csv")
    except:
        try:
            # Try parent directory path
            df = pd.read_csv("../Finance/UC-Schools/UC_Schools_Admission_Rankings.csv")
        except:
            # Fallback for local development
            df = pd.read_csv("/Users/muskan.kukreja/Documents/mk-git-test/Finance/UC-Schools/UC_Schools_Admission_Rankings.csv")
    
    # Clean column names
    df.columns = df.columns.str.strip()
    
    # Ensure numeric columns are properly typed
    numeric_cols = ['Applied', 'Admitted', 'Enrolled', 'Admit_Rate_%', 
                   'African_American_Applied', 'African_American_Admitted', 'African_American_Admit_Rate_%',
                   'Hispanic_Latinx_Applied', 'Hispanic_Latinx_Admitted', 'Hispanic_Latinx_Admit_Rate_%',
                   'Asian_Applied', 'Asian_Admitted', 'Asian_Admit_Rate_%',
                   'White_Applied', 'White_Admitted', 'White_Admit_Rate_%',
                   'International_Applied', 'International_Admitted', 'International_Admit_Rate_%']
    
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    
    return df


def get_rate_color(rate):
    """Return color class based on admit rate"""
    if rate >= 70:
        return "high"
    elif rate >= 40:
        return "medium"
    else:
        return "low"


def get_rate_badge_color(rate):
    """Return badge color hex based on admit rate"""
    if rate >= 70:
        return "#48bb78"
    elif rate >= 40:
        return "#ecc94b"
    else:
        return "#fc8181"


def render_school_card(school, idx, show_details=False):
    """Render a school card with all information"""
    rate_class = get_rate_color(school['Admit_Rate_%'])
    type_class = "public" if school['Private_Public'] == "Public" else "private"
    
    card_html = f"""
    <div class="school-card">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 0.5rem;">
            <div>
                <div class="school-name">#{idx} {school['School']}</div>
                <div class="school-city">📍 {school['City']}, {school['County']} County</div>
            </div>
            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                <span class="badge badge-{type_class}">{school['Private_Public']}</span>
                <span class="badge badge-rate-{rate_class}">{school['Admit_Rate_%']:.1f}%</span>
            </div>
        </div>
        <div class="school-stats">
            <div class="stat-item">
                <span class="stat-label">Applied:</span>
                <span class="stat-value">{int(school['Applied']):,}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Admitted:</span>
                <span class="stat-value">{int(school['Admitted']):,}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Enrolled:</span>
                <span class="stat-value">{int(school['Enrolled']):,}</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">UC Campus:</span>
                <span class="stat-value">{school['College']}</span>
            </div>
        </div>
        <div class="progress-container">
            <div class="progress-bar progress-{rate_class}" style="width: {min(school['Admit_Rate_%'], 100)}%;"></div>
        </div>
    </div>
    """
    return card_html


def render_metric_card(value, label, icon=""):
    """Render a metric card"""
    return f"""
    <div class="metric-card">
        <div class="metric-value">{icon} {value}</div>
        <div class="metric-label">{label}</div>
    </div>
    """


def create_demographic_chart(school):
    """Create a demographic breakdown chart for a school"""
    demographics = {
        'Asian': school.get('Asian_Admit_Rate_%', 0),
        'Hispanic/Latinx': school.get('Hispanic_Latinx_Admit_Rate_%', 0),
        'White': school.get('White_Admit_Rate_%', 0),
        'African American': school.get('African_American_Admit_Rate_%', 0),
        'International': school.get('International_Admit_Rate_%', 0)
    }
    
    # Filter out zero values
    demographics = {k: v for k, v in demographics.items() if v > 0}
    
    if not demographics:
        return None
    
    fig = go.Figure(data=[
        go.Bar(
            x=list(demographics.keys()),
            y=list(demographics.values()),
            marker_color=['#4299e1', '#48bb78', '#ed8936', '#9f7aea', '#f56565'],
            text=[f'{v:.1f}%' for v in demographics.values()],
            textposition='outside'
        )
    ])
    
    fig.update_layout(
        title=dict(text="Admission Rate by Demographics", font=dict(size=14, color='#fff')),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#a0aec0'),
        yaxis=dict(
            title="Admit Rate (%)",
            gridcolor='#2d3748',
            range=[0, max(demographics.values()) * 1.2]
        ),
        xaxis=dict(title="", tickangle=-45),
        height=350,
        margin=dict(l=40, r=40, t=60, b=80)
    )
    
    return fig


def create_demographic_applications_chart(school):
    """Create a chart showing applications by demographics"""
    demographics = {
        'Asian': school.get('Asian_Applied', 0),
        'Hispanic/Latinx': school.get('Hispanic_Latinx_Applied', 0),
        'White': school.get('White_Applied', 0),
        'African American': school.get('African_American_Applied', 0),
        'International': school.get('International_Applied', 0)
    }
    
    # Filter out zero values
    demographics = {k: v for k, v in demographics.items() if v > 0}
    
    if not demographics:
        return None
    
    fig = go.Figure(data=[
        go.Pie(
            labels=list(demographics.keys()),
            values=list(demographics.values()),
            hole=0.4,
            marker_colors=['#4299e1', '#48bb78', '#ed8936', '#9f7aea', '#f56565']
        )
    ])
    
    fig.update_layout(
        title=dict(text="Applications by Demographics", font=dict(size=14, color='#fff')),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#a0aec0'),
        height=350,
        margin=dict(l=20, r=20, t=60, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=-0.2)
    )
    
    return fig


def main():
    # Load data
    df = load_data()
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎓 UC Schools Admission Rankings</h1>
        <p>Explore admission statistics for California high schools applying to UC campuses</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Main navigation tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Rankings", "🔍 School Details", "⚖️ Compare Schools", "📈 Analytics"])
    
    # ===== TAB 1: RANKINGS =====
    with tab1:
        # Filter section
        st.markdown('<div class="section-header">🎯 Filters</div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            uc_filter = st.selectbox(
                "UC Campus",
                options=["All UC", "UC Berkeley", "UCLA", "UCSD"],
                key="uc_filter"
            )
        
        with col2:
            type_filter = st.selectbox(
                "School Type",
                options=["All", "Public", "Private"],
                key="type_filter"
            )
        
        with col3:
            cities = ["All Cities"] + sorted(df['City'].unique().tolist())
            city_filter = st.selectbox(
                "City",
                options=cities,
                key="city_filter"
            )
        
        # Apply filters
        filtered_df = df.copy()
        
        if uc_filter != "All UC":
            filtered_df = filtered_df[filtered_df['College'] == uc_filter]
        
        if type_filter != "All":
            filtered_df = filtered_df[filtered_df['Private_Public'] == type_filter]
        
        if city_filter != "All Cities":
            filtered_df = filtered_df[filtered_df['City'] == city_filter]
        
        # Sort by admit rate and get top 50
        filtered_df = filtered_df.sort_values('Admit_Rate_%', ascending=False).head(50)
        
        # Summary metrics
        st.markdown('<div class="section-header">📈 Summary</div>', unsafe_allow_html=True)
        
        metric_cols = st.columns(4)
        
        with metric_cols[0]:
            st.markdown(render_metric_card(
                f"{len(filtered_df)}",
                "Schools Shown",
                "🏫"
            ), unsafe_allow_html=True)
        
        with metric_cols[1]:
            avg_rate = filtered_df['Admit_Rate_%'].mean() if len(filtered_df) > 0 else 0
            st.markdown(render_metric_card(
                f"{avg_rate:.1f}%",
                "Avg Admit Rate",
                "📊"
            ), unsafe_allow_html=True)
        
        with metric_cols[2]:
            total_applied = filtered_df['Applied'].sum()
            st.markdown(render_metric_card(
                f"{int(total_applied):,}",
                "Total Applied",
                "📝"
            ), unsafe_allow_html=True)
        
        with metric_cols[3]:
            total_admitted = filtered_df['Admitted'].sum()
            st.markdown(render_metric_card(
                f"{int(total_admitted):,}",
                "Total Admitted",
                "✅"
            ), unsafe_allow_html=True)
        
        # Rankings list
        st.markdown('<div class="section-header">🏆 Top Schools by Admit Rate</div>', unsafe_allow_html=True)
        
        if len(filtered_df) == 0:
            st.warning("No schools match your filter criteria. Try adjusting your filters.")
        else:
            for idx, (_, school) in enumerate(filtered_df.iterrows(), 1):
                st.markdown(render_school_card(school, idx), unsafe_allow_html=True)
                
                # Add a button to view details
                if st.button(f"View Details →", key=f"detail_btn_{idx}_{school['School']}"):
                    st.session_state['selected_school'] = school['School']
                    st.session_state['selected_college'] = school['College']
    
    # ===== TAB 2: SCHOOL DETAILS =====
    with tab2:
        st.markdown('<div class="section-header">🔍 School Detail View</div>', unsafe_allow_html=True)
        
        # School selector
        col1, col2 = st.columns(2)
        
        with col1:
            uc_campus = st.selectbox(
                "Select UC Campus",
                options=df['College'].unique().tolist(),
                key="detail_uc"
            )
        
        campus_schools = df[df['College'] == uc_campus]['School'].unique().tolist()
        
        with col2:
            selected_school = st.selectbox(
                "Select School",
                options=sorted(campus_schools),
                key="detail_school"
            )
        
        if selected_school:
            school_data = df[(df['School'] == selected_school) & (df['College'] == uc_campus)].iloc[0]
            
            # School header
            rate_color = get_rate_badge_color(school_data['Admit_Rate_%'])
            st.markdown(f"""
            <div class="detail-section">
                <h2 style="color: #fff; margin: 0 0 0.5rem 0;">{school_data['School']}</h2>
                <p style="color: #a0aec0; margin: 0;">
                    📍 {school_data['City']}, {school_data['County']} County | 
                    🎓 {school_data['Private_Public']} School |
                    🏛️ {school_data['College']}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Key metrics
            metric_cols = st.columns(4)
            
            with metric_cols[0]:
                st.metric("Admit Rate", f"{school_data['Admit_Rate_%']:.1f}%")
            with metric_cols[1]:
                st.metric("Applied", f"{int(school_data['Applied']):,}")
            with metric_cols[2]:
                st.metric("Admitted", f"{int(school_data['Admitted']):,}")
            with metric_cols[3]:
                st.metric("Enrolled", f"{int(school_data['Enrolled']):,}")
            
            # Demographic charts
            st.markdown('<div class="section-header">👥 Demographic Breakdown</div>', unsafe_allow_html=True)
            
            chart_col1, chart_col2 = st.columns(2)
            
            with chart_col1:
                demo_rate_chart = create_demographic_chart(school_data)
                if demo_rate_chart:
                    st.plotly_chart(demo_rate_chart, use_container_width=True)
                else:
                    st.info("No demographic admit rate data available for this school.")
            
            with chart_col2:
                demo_app_chart = create_demographic_applications_chart(school_data)
                if demo_app_chart:
                    st.plotly_chart(demo_app_chart, use_container_width=True)
                else:
                    st.info("No demographic application data available for this school.")
            
            # Detailed demographic table
            st.markdown('<div class="section-header">📋 Detailed Demographics</div>', unsafe_allow_html=True)
            
            demo_data = {
                'Demographic': ['Asian', 'Hispanic/Latinx', 'White', 'African American', 'International', 'Pacific Islander', 'American Indian'],
                'Applied': [
                    int(school_data.get('Asian_Applied', 0)),
                    int(school_data.get('Hispanic_Latinx_Applied', 0)),
                    int(school_data.get('White_Applied', 0)),
                    int(school_data.get('African_American_Applied', 0)),
                    int(school_data.get('International_Applied', 0)),
                    int(school_data.get('Pacific_Islander_Applied', 0)),
                    int(school_data.get('American_Indian_Applied', 0))
                ],
                'Admitted': [
                    int(school_data.get('Asian_Admitted', 0)),
                    int(school_data.get('Hispanic_Latinx_Admitted', 0)),
                    int(school_data.get('White_Admitted', 0)),
                    int(school_data.get('African_American_Admitted', 0)),
                    int(school_data.get('International_Admitted', 0)),
                    int(school_data.get('Pacific_Islander_Admitted', 0)),
                    int(school_data.get('American_Indian_Admitted', 0))
                ],
                'Admit Rate (%)': [
                    school_data.get('Asian_Admit_Rate_%', 0),
                    school_data.get('Hispanic_Latinx_Admit_Rate_%', 0),
                    school_data.get('White_Admit_Rate_%', 0),
                    school_data.get('African_American_Admit_Rate_%', 0),
                    school_data.get('International_Admit_Rate_%', 0),
                    school_data.get('Pacific_Islander_Admit_Rate_%', 0),
                    school_data.get('American_Indian_Admit_Rate_%', 0)
                ]
            }
            
            demo_df = pd.DataFrame(demo_data)
            demo_df = demo_df[demo_df['Applied'] > 0]  # Only show demographics with data
            
            if len(demo_df) > 0:
                st.dataframe(
                    demo_df.style.format({'Admit Rate (%)': '{:.1f}%'}),
                    use_container_width=True,
                    hide_index=True
                )
            else:
                st.info("No detailed demographic data available for this school.")
    
    # ===== TAB 3: COMPARISON TOOL =====
    with tab3:
        st.markdown('<div class="section-header">⚖️ School Comparison Tool</div>', unsafe_allow_html=True)
        st.markdown("Select 2-3 schools to compare their admission statistics side-by-side.")
        
        # School selection
        col1, col2 = st.columns(2)
        
        with col1:
            compare_uc = st.selectbox(
                "Select UC Campus for Comparison",
                options=["All UC", "UC Berkeley", "UCLA", "UCSD"],
                key="compare_uc"
            )
        
        if compare_uc == "All UC":
            compare_schools_list = df['School'].unique().tolist()
        else:
            compare_schools_list = df[df['College'] == compare_uc]['School'].unique().tolist()
        
        with col2:
            selected_schools = st.multiselect(
                "Select Schools (2-3)",
                options=sorted(compare_schools_list),
                max_selections=3,
                key="compare_schools"
            )
        
        if len(selected_schools) >= 2:
            # Create comparison data
            compare_data = []
            for school_name in selected_schools:
                if compare_uc == "All UC":
                    school_info = df[df['School'] == school_name].iloc[0]
                else:
                    school_info = df[(df['School'] == school_name) & (df['College'] == compare_uc)].iloc[0]
                compare_data.append(school_info)
            
            # Side-by-side comparison
            cols = st.columns(len(compare_data))
            
            for i, (col, school) in enumerate(zip(cols, compare_data)):
                with col:
                    rate_class = get_rate_color(school['Admit_Rate_%'])
                    st.markdown(f"""
                    <div class="comparison-card">
                        <div class="comparison-header">
                            <h3 style="color: #fff; font-size: 1rem; margin: 0;">{school['School']}</h3>
                            <p style="color: #a0aec0; font-size: 0.8rem; margin: 0.5rem 0 0 0;">
                                📍 {school['City']} | {school['Private_Public']}
                            </p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.metric("Admit Rate", f"{school['Admit_Rate_%']:.1f}%")
                    st.metric("Applications", f"{int(school['Applied']):,}")
                    st.metric("Admissions", f"{int(school['Admitted']):,}")
                    st.metric("Enrolled", f"{int(school['Enrolled']):,}")
            
            # Comparison chart
            st.markdown('<div class="section-header">📊 Visual Comparison</div>', unsafe_allow_html=True)
            
            # Create comparison bar chart
            comparison_metrics = ['Applied', 'Admitted', 'Enrolled']
            fig = go.Figure()
            
            colors = ['#4299e1', '#48bb78', '#ed8936']
            
            for i, school in enumerate(compare_data):
                fig.add_trace(go.Bar(
                    name=school['School'][:20] + '...' if len(school['School']) > 20 else school['School'],
                    x=comparison_metrics,
                    y=[school['Applied'], school['Admitted'], school['Enrolled']],
                    marker_color=colors[i],
                    text=[f"{int(v):,}" for v in [school['Applied'], school['Admitted'], school['Enrolled']]],
                    textposition='outside'
                ))
            
            fig.update_layout(
                barmode='group',
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#a0aec0'),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
                yaxis=dict(gridcolor='#2d3748'),
                height=400,
                margin=dict(l=40, r=40, t=60, b=40)
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Admit rate comparison
            fig2 = go.Figure()
            
            school_names = [s['School'][:15] + '...' if len(s['School']) > 15 else s['School'] for s in compare_data]
            admit_rates = [s['Admit_Rate_%'] for s in compare_data]
            
            fig2.add_trace(go.Bar(
                x=school_names,
                y=admit_rates,
                marker_color=[get_rate_badge_color(r) for r in admit_rates],
                text=[f"{r:.1f}%" for r in admit_rates],
                textposition='outside'
            ))
            
            fig2.update_layout(
                title=dict(text="Admit Rate Comparison", font=dict(size=14, color='#fff')),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#a0aec0'),
                yaxis=dict(title="Admit Rate (%)", gridcolor='#2d3748', range=[0, max(admit_rates) * 1.2]),
                height=350,
                margin=dict(l=40, r=40, t=60, b=80)
            )
            
            st.plotly_chart(fig2, use_container_width=True)
        
        elif len(selected_schools) == 1:
            st.info("Please select at least 2 schools to compare.")
        else:
            st.info("👆 Select 2-3 schools from the dropdown above to start comparing.")
    
    # ===== TAB 4: ANALYTICS =====
    with tab4:
        st.markdown('<div class="section-header">📈 Analytics & Visualizations</div>', unsafe_allow_html=True)
        
        # Analytics filter
        analytics_uc = st.selectbox(
            "Filter by UC Campus",
            options=["All UC", "UC Berkeley", "UCLA", "UCSD"],
            key="analytics_uc"
        )
        
        if analytics_uc == "All UC":
            analytics_df = df.copy()
        else:
            analytics_df = df[df['College'] == analytics_uc].copy()
        
        # Remove duplicates for overall analytics (keep best rate per school)
        analytics_unique = analytics_df.loc[analytics_df.groupby('School')['Admit_Rate_%'].idxmax()]
        
        # Row 1: Top 10 schools chart and distribution
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🏆 Top 10 Schools by Admit Rate")
            
            top_10 = analytics_df.nlargest(10, 'Admit_Rate_%')
            
            fig = go.Figure(data=[
                go.Bar(
                    y=[s[:20] + '...' if len(s) > 20 else s for s in top_10['School']],
                    x=top_10['Admit_Rate_%'],
                    orientation='h',
                    marker_color=[get_rate_badge_color(r) for r in top_10['Admit_Rate_%']],
                    text=[f"{r:.1f}%" for r in top_10['Admit_Rate_%']],
                    textposition='outside'
                )
            ])
            
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#a0aec0'),
                xaxis=dict(title="Admit Rate (%)", gridcolor='#2d3748'),
                yaxis=dict(autorange="reversed"),
                height=400,
                margin=dict(l=150, r=60, t=20, b=40)
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### 📊 Admit Rate Distribution")
            
            fig = go.Figure(data=[
                go.Histogram(
                    x=analytics_df['Admit_Rate_%'],
                    nbinsx=20,
                    marker_color='#4299e1',
                    opacity=0.8
                )
            ])
            
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#a0aec0'),
                xaxis=dict(title="Admit Rate (%)", gridcolor='#2d3748'),
                yaxis=dict(title="Number of Schools", gridcolor='#2d3748'),
                height=400,
                margin=dict(l=60, r=40, t=20, b=40)
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        # Row 2: Public vs Private and By City
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🏫 Public vs Private Schools")
            
            type_stats = analytics_unique.groupby('Private_Public').agg({
                'School': 'count',
                'Admit_Rate_%': 'mean',
                'Applied': 'sum'
            }).reset_index()
            
            fig = go.Figure(data=[
                go.Pie(
                    labels=type_stats['Private_Public'],
                    values=type_stats['School'],
                    hole=0.4,
                    marker_colors=['#48bb78', '#ed8936']
                )
            ])
            
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#a0aec0'),
                height=350,
                margin=dict(l=20, r=20, t=20, b=20)
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Stats below
            for _, row in type_stats.iterrows():
                st.markdown(f"""
                **{row['Private_Public']}**: {int(row['School'])} schools | 
                Avg Rate: {row['Admit_Rate_%']:.1f}% | 
                Total Apps: {int(row['Applied']):,}
                """)
        
        with col2:
            st.markdown("### 🌆 Top Cities by Average Admit Rate")
            
            city_stats = analytics_unique.groupby('City').agg({
                'Admit_Rate_%': 'mean',
                'School': 'count'
            }).reset_index()
            
            city_stats = city_stats[city_stats['School'] >= 2]  # At least 2 schools
            city_stats = city_stats.nlargest(10, 'Admit_Rate_%')
            
            fig = go.Figure(data=[
                go.Bar(
                    x=city_stats['City'],
                    y=city_stats['Admit_Rate_%'],
                    marker_color='#9f7aea',
                    text=[f"{r:.1f}%" for r in city_stats['Admit_Rate_%']],
                    textposition='outside'
                )
            ])
            
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#a0aec0'),
                xaxis=dict(tickangle=-45),
                yaxis=dict(title="Avg Admit Rate (%)", gridcolor='#2d3748'),
                height=350,
                margin=dict(l=60, r=40, t=20, b=100)
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        # Row 3: Demographic comparison across all schools
        st.markdown('<div class="section-header">👥 Overall Demographic Admit Rates</div>', unsafe_allow_html=True)
        
        # Calculate average demographic rates
        demo_cols = {
            'Asian': 'Asian_Admit_Rate_%',
            'Hispanic/Latinx': 'Hispanic_Latinx_Admit_Rate_%',
            'White': 'White_Admit_Rate_%',
            'African American': 'African_American_Admit_Rate_%',
            'International': 'International_Admit_Rate_%'
        }
        
        demo_avgs = {}
        for demo_name, col_name in demo_cols.items():
            if col_name in analytics_df.columns:
                non_zero = analytics_df[analytics_df[col_name] > 0][col_name]
                if len(non_zero) > 0:
                    demo_avgs[demo_name] = non_zero.mean()
        
        if demo_avgs:
            fig = go.Figure(data=[
                go.Bar(
                    x=list(demo_avgs.keys()),
                    y=list(demo_avgs.values()),
                    marker_color=['#4299e1', '#48bb78', '#ed8936', '#9f7aea', '#f56565'],
                    text=[f"{v:.1f}%" for v in demo_avgs.values()],
                    textposition='outside'
                )
            ])
            
            fig.update_layout(
                title=dict(text="Average Admit Rate by Demographics (Schools with Data)", font=dict(size=14, color='#fff')),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#a0aec0'),
                yaxis=dict(title="Average Admit Rate (%)", gridcolor='#2d3748'),
                height=400,
                margin=dict(l=60, r=40, t=60, b=60)
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        # Summary statistics
        st.markdown('<div class="section-header">📋 Summary Statistics</div>', unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Schools", len(analytics_unique))
        with col2:
            st.metric("Avg Admit Rate", f"{analytics_df['Admit_Rate_%'].mean():.1f}%")
        with col3:
            st.metric("Highest Rate", f"{analytics_df['Admit_Rate_%'].max():.1f}%")
        with col4:
            st.metric("Lowest Rate", f"{analytics_df['Admit_Rate_%'].min():.1f}%")


if __name__ == "__main__":
    main()


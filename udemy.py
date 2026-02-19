import streamlit as st
import pandas as pd
import plotly.express as px


# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Udemy Analysis Dashboard",
    layout="wide"
)

st.title(" Udemy Analysis Dashboard")
st.image('data:image/png;base64,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')
# ---------------- Data Loading ----------------


df = pd.read_csv("Udemy Courses.csv")

# ---------------- Sidebar ----------------
analysis_section = st.sidebar.radio(
    "Select Analysis",
    options=[
        "Full Dataset",
        'Univariate Analysis',
        "Number of Courses per Subject",
        "free vs paid",
        "Top 7 most famous courses",
        "Pricing Analysis",
        "customers profesional level"
    ]
)

# ---------------- Main Content ----------------
st.subheader(analysis_section)

if analysis_section == "Full Dataset":
    st.write(f"Complete dataset ({df.shape[0]} rows)")
    st.dataframe(df)

elif analysis_section== 'Univariate Analysis':

    st.title('Univariate Analysis')

    for col in df.columns:
        if col =='course_title' or col =='course_id':
            continue

        st.plotly_chart(px.histogram(data_frame= df, x= col, title= f'the distrbution of {col}'))


elif analysis_section == "Number of Courses per Subject":
    st.write("Number of Courses per Subject (bivariate Analysis)")

    subject_courses =df.groupby('subject', as_index=False)['course_id'].count().sort_values(by='course_id', ascending=True)
    subject_courses=subject_courses.rename(columns={'course_id': 'course_count'})


    fig1 = px.bar(
        subject_courses,
        x='subject',
        y='course_count',
        text_auto=True,
        title='Number of Courses per Subject'
    )

    st.plotly_chart(fig1, use_container_width=True)

elif analysis_section == "free vs paid":
    st.write("free vs paid  (bivariate Analysis)")
    free_vs_paid=df.groupby('is_paid',as_index=False)['course_id'].count()
    free_vs_paid=free_vs_paid.rename(columns={'is_paid':'is_the_course_paid?','course_id':'Number_of_courses'})
    fig2=px.bar(data_frame=free_vs_paid,
       x='is_the_course_paid?',
       y='Number_of_courses',
       title='free VS Paid')
    st.plotly_chart(fig2, use_container_width=True)

elif analysis_section == "Top 7 most famous courses":
    st.write("Top 7 most famous courses  (bivariate Analysis)")
    top_7=(df.sort_values(by='num_subscribers',ascending=False).head(7))
    top_7 = top_7.reset_index(drop=True)
    fig3=px.bar(data_frame=top_7,
       y='course_title',
       x='num_subscribers',
       color_discrete_sequence=['#1f77b4'],
       #color_discrete_sequence=px.colors.qualitative.Set2,
       title='TOP 7 courses')
    st.plotly_chart(fig3, use_container_width=True)

elif analysis_section == "Pricing Analysis":
    st.write("Pricing analysis")
    df['price'] = df['price'].apply(lambda x : '0' if x == 'Free' else x)
    df['price'] = pd.to_numeric(df['price'] , errors = 'coerce')
    cheap_courses = df[df['price'] <= 100]
    expensive_courses = df[df['price'] > 100]
    cheap_mean = cheap_courses.groupby('subject')['price'].mean()
    cheap_count = cheap_courses.groupby('subject')['course_id'].count()
    expensive_mean = expensive_courses.groupby('subject')['price'].mean()
    expensive_count = expensive_courses.groupby('subject')['course_id'].count()
    price_summary = pd.DataFrame({
    'cheap_course_count': cheap_count,
    'cheap_avg_price': cheap_mean,
    'expensive_course_count': expensive_count,
    'expensive_avg_price': expensive_mean
    }).reset_index()
    st.dataframe(price_summary)




elif analysis_section == "customers profesional level":
    st.write("customers profesional level  (bivariate Analysis)")
    peak_pop_per_level=df.groupby('level',as_index=False)['num_subscribers'].sum()
    fig4=px.pie(data_frame=peak_pop_per_level,
       names='level',
       values='num_subscribers',
       color_discrete_sequence=["#b3b7ae"],
       title='number of subscribers per level')
    st.plotly_chart(fig4, use_container_width=True)



import pandas as pd
from ucimlrepo import fetch_ucirepo

def calculate_demographic_data(df, print_data=True):
    # Ensure 'salary' column exists (rename if needed)
    if 'salary' not in df.columns and len(df.columns) > 0:
        # The last column is typically the target (salary)
        target_col = df.columns[-1]
        df = df.rename(columns={target_col: 'salary'})
    
    # Clean column names (strip whitespace)
    df.columns = df.columns.str.strip()
    
    # 1. Number of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Percentage with advanced education earning >50K
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(advanced_education)]
    lower_education = df[~df['education'].isin(advanced_education)]

    higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)

    # 5. Minimum hours per week
    min_work_hours = df['hours-per-week'].min()

    # 6. Percentage of people working min hours with >50K salary
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage_min_workers = round((min_workers['salary'] == '>50K').mean() * 100, 1)

    # 7. Country with highest percentage of people earning >50K
    country_salary = df[df['salary'] == '>50K'].groupby('native-country')['salary'].count()
    country_total = df.groupby('native-country')['salary'].count()
    country_percentage = (country_salary / country_total * 100).fillna(0)
    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(country_percentage.max(), 1)

    # 8. Most popular occupation for those earning >50K in India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].mode()[0]

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelor's degrees: {percentage_bachelors}%")
        print(f"Percentage with advanced education earning >50K: {higher_education_rich}%")
        print(f"Percentage without advanced education earning >50K: {lower_education_rich}%")
        print("Minimum hours per week:", min_work_hours)
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage_min_workers}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupation in India for those earning >50K:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage_min_workers': rich_percentage_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

if __name__ == "__main__":
    # Fetch dataset directly from UCI
    adult = fetch_ucirepo(id=2)
    df = pd.concat([adult.data.features, adult.data.targets], axis=1)
    
    # Debug: print column names to see actual structure
    print("Column names:", df.columns.tolist())
    print("First few rows:")
    print(df.head())
    print()

    calculate_demographic_data(df)
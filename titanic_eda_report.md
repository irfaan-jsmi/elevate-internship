# Titanic EDA Report

## Introduction
This report presents an exploratory data analysis of the Titanic dataset to understand passenger characteristics and factors associated with survival.

## Dataset Overview
The dataset contains 891 rows and 12 columns. It includes demographic, ticket, cabin, and travel-related variables.

## Cleaning Process
Missing values in Age were filled using the median, Embarked was filled using the mode, and Cabin was replaced with Unknown. Duplicate rows were removed, and important categorical fields were converted to category types.

## Visualizations and Observations
### Countplot of Survived
- The dataset has more passengers who did not survive than survived.
- This indicates an imbalanced target variable with survival as the minority class.
- The plot confirms that Titanic disaster outcomes were heavily skewed toward fatalities.

### Countplot of Passenger Class
- Third class has the highest passenger count.
- First class has the smallest group, which suggests the cabin hierarchy was unevenly distributed.
- This class imbalance is useful to consider when comparing survival across classes.

### Countplot of Sex
- There are more male passengers than female passengers.
- The gender split is clearly unbalanced, which may influence survival patterns.
- This makes sex an important variable to study against survival.

### Histogram of Age
- Most passengers are concentrated in the young adult range.
- The age distribution is right-skewed with fewer older passengers.
- A few very young passengers are present, showing the dataset includes children as well.

### Histogram of Fare
- Fare is strongly right-skewed, meaning most tickets were relatively low cost.
- A small number of passengers paid very high fares.
- The long right tail suggests the presence of high-value outliers.

### Boxplot of Age
- The median age sits around the adult range, close to the middle of the distribution.
- The boxplot shows a moderate spread with some younger and older outliers.
- The overall age variation is reasonable and not extremely dispersed.

### Boxplot of Fare
- Fare has many upper outliers, which matches the strong right skew seen earlier.
- The median fare is far below the extreme values, indicating large price differences between passengers.
- This is one of the clearest skewed variables in the dataset.

### Survival by Gender
- Females show a noticeably higher survival count than males.
- Males dominate the non-survived group, which suggests gender was strongly related to rescue priority.
- This supports the well-known Titanic pattern of women and children first.

### Survival by Passenger Class
- First-class passengers had the best survival outcome.
- Third-class passengers had the highest death count and lowest survival count.
- Passenger class appears to be a strong proxy for access, location, and evacuation priority.

### Survival by Embarked
- Port S contains the largest number of passengers, so it dominates the chart.
- Survival patterns differ across ports, but the effect looks less dramatic than sex or class.
- Embarked may be indirectly related to survival because it can reflect ticket class and passenger mix.

### Scatterplot of Age vs Fare
- There is no strong linear relationship between age and fare.
- High-fare outliers appear across several age groups.
- Survival seems more concentrated among higher fares, which hints at class-driven survival differences.

### Correlation Heatmap
- Survived is positively associated with Fare and negatively associated with Pclass.
- Pclass and Fare show a meaningful inverse relationship.
- Most other numeric correlations are weak, which suggests survival depended more on social and class factors than simple numeric patterns.

### Pairplot for Numerical Columns
- Fare shows the clearest separation pattern compared with the other variables.
- The numerical features are mostly weakly linearly related, aside from the visible class-fare structure.
- The pairplot reinforces that outliers and skewness are important characteristics in this dataset.

## Final Findings
Gender, passenger class, and fare were the strongest visible patterns related to survival. The dataset is also skewed and contains significant outliers, especially in Fare.

## Conclusion
The Titanic dataset reveals that survival was strongly influenced by social class and gender. These insights make the dataset ideal for introductory analytics and feature-based storytelling.

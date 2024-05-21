import pandas as pd  

fruit_sales = pd.DataFrame({
    'Apples': [35, 41],  # Sales figures for apples
    'Bananas': [21, 34]  # Sales figures for bananas
})

# Add an index to the DataFrame to label the rows
fruit_sales.index = [‘2017 Sales’, ‘2018 Sales’]

fruit_sales.to_csv('fruit_sales.csv')

print(fruit_sales)


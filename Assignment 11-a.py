import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('sales_data.csv')

# a) Line Plot - Total Profit
plt.figure()
plt.plot(data['month'], data['total_profit'], marker='o')
plt.title('Total Profit Per Month')
plt.xlabel('Month')
plt.ylabel('Profit')
plt.grid()
plt.show()

# b) Multiline Plot - All Products
plt.figure()
plt.plot(data['month'], data['facecream'], label='Face Cream')
plt.plot(data['month'], data['facewash'], label='Face Wash')
plt.plot(data['month'], data['toothpaste'], label='Toothpaste')
plt.plot(data['month'], data['bathingsoap'], label='Bathing Soap')
plt.plot(data['month'], data['shampoo'], label='Shampoo')
plt.plot(data['month'], data['moisturizer'], label='Moisturizer')

plt.title('Product Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.show()

# c) Bar Chart - Face Cream & Face Wash
plt.figure()
width = 0.3
plt.bar(data['month'] - width/2, data['facecream'], width=width, label='Face Cream')
plt.bar(data['month'] + width/2, data['facewash'], width=width, label='Face Wash')

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Face Cream vs Face Wash')
plt.legend()
plt.show()

# d) Pie Chart - Total Sales per Product
total_sales = [
    data['facecream'].sum(),
    data['facewash'].sum(),
    data['toothpaste'].sum(),
    data['bathingsoap'].sum(),
    data['shampoo'].sum(),
    data['moisturizer'].sum()
]

labels = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']

plt.figure()
plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.title('Total Sales Distribution')
plt.show()
import pandas  as pd
print(pd.__version__)
df = pd.read_excel('alphonsineanalysis.xlsx')
df['INV_DATE'] = pd.to_datetime(df['INV_DATE'])
filtered_data_2020 = df[df['INV_DATE'].dt.year == 2020]
print(filtered_data_2020)
total_sales = df['TOTAL_SALE'].sum()
total_sales_by_rep = df.groupby('SALESREP')['TOTAL_SALE'].sum()
highest_sales_rep = total_sales_by_rep.idxmax()
highest_total_sales = total_sales_by_rep.max()
print(f'The sales representative with the highest total sales is: {highest_sales_rep}')
print(f' Sales Amount: ${total_sales:.2f}')
average_unit_price = df['UNIT_PRICE'].mean()

print(f'Average Unit Price of Products Sold: ${average_unit_price:.2f}')
distinct_customer_count = df['CUSTOMER_ID'].nunique()

print(f'Number of Distinct Customers: {distinct_customer_count}')
total_sales = df['SALES_TAX'].sum()

print(f'Total Sales : ${total_sales :.2f}')
total_sales_by_product = df.groupby('PROD_CODE')['TOTAL_SALE'].sum()
highest_sales_product = total_sales_by_product.idxmax()
highest_total_sales = total_sales_by_product.max()

print(f'The product with the highest total sales is: {highest_sales_product}')
print(f'Total Sales Amount: ${highest_total_sales:.2f}')
average_quantity = df['QTY'].mean()
print(f'Average Quantity per Transaction: {average_quantity:.2f}')
transactions_jan_2 = df[df['INV_DATE'].dt.date == pd.to_datetime('2020-01-02').date()]
num_transactions = len(transactions_jan_2)

print(f'Number of Transactions on January 2, 2020: {num_transactions}')
total_sales_rep = df.groupby('SALESREP')['TOTAL_SALE'].sum()
print(total_sales_rep)
transactions_per_product = df['PROD_CODE'].value_counts()

print(transactions_per_product)
df['SALES_TAX_RATE'] = df['SALES_TAX'] / df['TOTAL_SALE']

average_tax_rate = df['SALES_TAX_RATE'].mean()

print(f'Average Sales Tax Rate for Transactions: {average_tax_rate:.2%}')
correlation_coefficient = df['UNIT_PRICE'].corr(df['QTY'])

print(f'Correlation Coefficient between Unit Price and Quantity Sold: {correlation_coefficient:.2f}')
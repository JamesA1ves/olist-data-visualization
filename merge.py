import pandas as pd

# Carregar tabelas originais
pedidos = pd.read_csv("olist_orders_dataset.csv")
itens = pd.read_csv("olist_order_items_dataset.csv")
clientes = pd.read_csv("olist_customers_dataset.csv")
produtos = pd.read_csv("olist_products_dataset.csv")
vendedores = pd.read_csv("olist_sellers_dataset.csv")
pagamentos = pd.read_csv("olist_order_payments_dataset.csv")
traducao = pd.read_csv("product_category_name_translation.csv")

# Processo de Merge e enriquecimento
df = pd.merge(itens, pedidos, on='order_id', how='inner')
df = pd.merge(df, clientes, on='customer_id', how='inner')
df = pd.merge(df, vendedores, on='seller_id', how='inner', suffixes=('_customer', '_seller'))
df = pd.merge(df, produtos, on='product_id', how='inner')
df = pd.merge(df, traducao, on='product_category_name', how='left')

pagamentos_agrupados = pagamentos.groupby('order_id')['payment_value'].sum().reset_index()
df = pd.merge(df, pagamentos_agrupados, on='order_id', how='inner')

# Salvar com o nome exato exigido pelos códigos de visualização
df.to_csv("olist_2016_2018.csv", index=False)
print("Sucesso! O arquivo 'olist_2016_2018.csv' foi gerado.")
from forex_python.converter import CurrencyRates

mxn = float(input("Ingresa la cantidad en MXN: "))

# Obtiene la tasa de cambio de dólares a pesos mexicanos
exchange_rate = CurrencyRates().convert('MXN', 'USD', mxn)

# Imprime la tasa de cambio
print("{} MXN = {} USD".format(mxn, exchange_rate))

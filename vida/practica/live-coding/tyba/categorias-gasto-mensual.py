
from calendar import c
from unicodedata import category
from unittest import result


transactions = [
    {"type": "deposit", "amount": 1000, "date": "2024-06-01"},
    {"type": "withdrawal", "amount": 300, "category": "food", "date": "2024-06-02"},
    {"type": "withdrawal", "amount": 200, "category": "transport", "date": "2024-06-03"},
    {"type": "withdrawal", "amount": 250, "category": "food", "date": "2024-06-10"},
    {"type": "deposit", "amount": 800, "date": "2024-07-01"},
    {"type": "withdrawal", "amount": 400, "category": "entertainment", "date": "2024-07-02"},
    {"type": "withdrawal", "amount": 200, "category": "food", "date": "2024-07-05"},
]

def detectar_cateorias_superan_gasto_mensual(transactions,thresholdPercentage):
  
  monto_por_categoria_mensual={}
  resultado={}
  
  for transaction in transactions:
    
    mes = transaction["date"][0:7]

    if mes not in monto_por_categoria_mensual:
      monto_por_categoria_mensual[mes]={}
    
    #ingreso total del mes
    if transaction["type"]=="deposit":
      if "total_ingreso_mes" not in monto_por_categoria_mensual[mes]:
        monto_por_categoria_mensual[mes]["total_ingreso_mes"] = 0

      #guardamos el toatl del mes
      monto_por_categoria_mensual[mes]["total_ingreso_mes"]+=transaction["amount"]

    
    if "category" in transaction:# osea si es ingreso.

      category = transaction["category"]

      if category not in monto_por_categoria_mensual[mes]:
        monto_por_categoria_mensual[mes][category]=0
        
      #luego acumulamos
      monto_por_categoria_mensual[mes][category]+=transaction["amount"]
  
      if monto_por_categoria_mensual[mes][category] > monto_por_categoria_mensual[mes]["total_ingreso_mes"]*thresholdPercentage/100:

        if mes not in resultado:
          resultado[mes]=[]
        if category not in resultado[mes]:
          resultado[mes].append(category)
    
  print(monto_por_categoria_mensual)

  return resultado
  





  
  
  
  

respuesta=detectar_cateorias_superan_gasto_mensual(transactions,40)
print(respuesta)
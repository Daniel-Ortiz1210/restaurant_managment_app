tables = {
  1: {
    'name': ['Jiho'],
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes',
      'total': [534.50, 20.0, 5]
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

def assign_table(table_number, name, vip_status=False):
  if vip_status == 'SI':
    vip_status = True
  # ¿Qué pasa cuando una mesa ya está ocupada?
  # ¿Qué pasa cuando todas las mesas ya están ocupadas?
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}
  print('¡Mesa asignada correctamente!')

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks

def calculate_price_per_person(table_number, total, tip, split):
    total_tip = total * (tip/100)
    split_price = (total + total_tip) / split
    print('Each person has to pay', split_price)
    total_order = 0
    for n in tables[table_number]['order']['total']:
        total_order = n
        break
    print('The total count is', total_order)
  
def main():
  print(
    '''
    1. Para asignar una mesa
    2. Para tomar una orden
    3. Para calcular la cuenta de una mesa
    4. Para consultar el status de una mesa
    5. Para consultar el status de todas las mesas
    6. Para salir del programa
    '''
  )
  user = input('Qué deseas hacer?: ')
  while user == '1' or user == '2' or user == '3' or user == '4' or user == '5' or user == '6':
    if user == '1':
      table_number = int(input('Escriba el número de mesa: '))
      names = input('Escriba el nombre de los comensales con apellidos (separados por ", "): ').title().strip().split(', ')
      vip_status = input('¿Presentan acceso VIP? (S/N): ').upper()
      assign_table(table_number, names, vip_status)
      user = input('¿Qué desea hacer ahora?: ')
      continue
    elif user == '2':
      print('Esta es opción 2')
      user = input('¿Qué desea hacer ahora?: ')
      continue
    elif user == '3':
      print('Esta es opción 3')
      user = input('¿Qué desea hacer ahora?: ')
      continue
    elif user == '4':
      print('Esta es opción 4')
      user = input('¿Qué desea hacer ahora?: ')
      continue
    elif user == '5':
      print('Esta es opción 5')
      user = input('¿Qué desea hacer ahora?: ')
      continue
    elif user == '6':
      print('Cerrando sesión...')
      print('Completado. Nos vemos pronto.')
      break


if __name__ == '__main__':
  main()
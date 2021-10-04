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

print(len(tables))
def assign_table(table_number, name, vip_status=False):
  if vip_status == 'SI':
    vip_status = True
  # ¿Qué pasa cuando una mesa ya está ocupada?
  # ¿Qué pasa cuando todas las mesas ya están ocupadas?
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}
  print('... .... ....')
  print('¡Mesa {} asignada correctamente!\n'.format(table_number))

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks
  print('... .... ....')
  print('¡Orden tomada con éxito!\n')

def calculate_total_count_and_per_person(table_number, total, tip):
    price_per_person = (total + tip) / len(tables[table_number]['name'])
    print('La cuenta total de la mesa {} es ${} pesos mexicanos.\nA cada persona le toca pagar ${} pesos mexicanos.'.format(table_number, total,price_per_person))

def user_option():
  user = int(input('¿Qué deseas hacer?: '))
  while user > 7:
    user = int(input('Escribe una opción valida: '))
  return user

def main():
  print(
    '''
    1. Asignar una mesa
    2. Tomar una orden
    3. Calcular la cuenta de una mesa
    4. Consultar el status de una mesa
    5. Consultar el status de todas las mesas
    6. Desocupar una mesa
    7. Para salir del programa
    '''
  )
  user = user_option()
  while user == 1 or user == 2 or user == 3 or user == 4 or user == 5 or user == 6 or user == 7:
    if user == 1:
      table_number = int(input('Escriba el número de mesa: '))
      if table_number > len(tables):
        print('Solo tenemos {} mesas dentro del restarante.'.format(len(tables)))
        table_number = int(input('Escriba el número de mesa correctamente: '))
      names = input('Escriba el nombre de los comensales con apellidos (separados por ", "): ').title().strip().split(', ')
      vip_status = input('¿Presentan acceso VIP? (S/N): ').upper()
      assign_table(table_number, names, vip_status)
      user = int(input('¿Qué deseas hacer ahora?: '))
      continue
    elif user == 2:
      try:
        table_number = int(input('Escriba el número de mesa: '))
        order_food = input('¿Qué alimentos desea ordenar el cliente?: ')
        order_drinks = input('¿Qué bebidas desea ordenar el cliente?: ')
        assign_food_items(table_number, food=order_food, drinks=order_drinks)
      except KeyError:
        print('No hay comensales en esta mesa. Primero asigna a un comensal y despúes toma la orden.\nAcciones sugeridas: Asignar una mesa (1).')
      user = int(input('¿Qué deseas hacer ahora?: '))
      continue
    elif user == 3:
      try:
        table_number = int(input('Escribe el número de mesa: '))
        total = float(input('¿Cuál fue la cuenta total de la mesa?: '))
        tip = float(input('Escribe la propina que el cliente dió: '))
        calculate_total_count_and_per_person(table_number, total, tip)
      except KeyError:
        print('No hay comensales en esta mesa. Primero asigna a un comensal y despúes toma la orden.\nAcciones sugeridas: Asignar una mesa (1).')
      user = int(input('¿Qué deseas hacer ahora?: '))
      continue
    elif user == 4:
      print('Esta es opción 4')
      user = int(input('¿Qué deseas hacer ahora?: '))
      continue
    elif user == 5:
      print('Esta es opción 5')
      user = int(input('¿Qué deseas hacer ahora?: '))
      continue
    elif user == 6:
      print('Esta es la opción 6')
      user = int(input('¿Qué deseas hacer ahora?: '))
      continue
    elif user == 7:
      confirmation = input('¿Estás seguro qué deseas salir? (S/N): ').lower()
      if confirmation == 'no':
        user = user_option()
        continue
      print('Cerrando sesión...')
      print('Completado. Nos vemos pronto.')
      break


if __name__ == '__main__':
  main()
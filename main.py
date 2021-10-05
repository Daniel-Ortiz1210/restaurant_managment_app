tables = {
  1: {
    'name': [1],
    'vip_status': False,
    'order': {
      'drinks': 'Jugo de naranja, Agua Natural',
      'food_items': 'Pancakes',
    }
  },
  2: {
    'name': [1, 2],
    'vip_status': False,
    'order': {
      'drinks': 'Jugo de naranja, Agua Natural',
      'food_items': 'Pancakes',
    }
  },
  3: {
    'name': [1, 2, 3],
    'vip_status': False,
    'order': {
      'drinks': 'Jugo de naranja, Agua Natural',
      'food_items': 'Pancakes',
    }
  },
  4: {
    'name': [1, 2, 3, 4],
    'vip_status': False,
    'order': {
      'drinks': 'Jugo de naranja, Agua Natural',
      'food_items': 'Pancakes',
    }
  },
  5: {
    'name': [1, 2, 3, 4, 5],
    'vip_status': False,
    'order': {
      'drinks': 'Jugo de naranja, Agua Natural',
      'food_items': 'Pancakes',
    }
  },
  6: {
    'name': [1, 2, 3, 4, 5, 6],
    'vip_status': False,
    'order': {
      'drinks': 'Jugo de naranja, Agua Natural',
      'food_items': 'Pancakes',
    }
  },
  7: {
    'name': [1, 2, 3, 4, 5, 6, 7],
    'vip_status': False,
    'order': {
      'drinks': 'Jugo de naranja, Agua Natural',
      'food_items': 'Pancakes',
    }
  }
}

instructions = ['Asignar una mesa', 'Tomar una orden', 'Calcular la cuenta de una mesa', 'Consultar el status de una mesa', 'Consultar el status de todas las mesas', 'Desocupar una mesa', 'Para salir del programa']

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

def user_option(instructions):
  user = int(input('¿Qué deseas hacer?: '))
  while user > len(instructions):
    user = int(input('Escribe una opción valida: '))
  return user

def status_per_table(table_number, num_persons, foods, drinks):
  print('La mesa {} está ocupada por {} personas.\nHan pedido lo siguiente:\nAlimentos --> {}\nBebidas --> {}'.format(table_number, num_persons, foods, drinks))    

def false_table(table_number):
    print('Número de mesa inválido')
    table_number = int(input('Ingrea un número de mesa válido: '))
    return table_number

def main(instructions):
  for i in range(len(instructions)):
    print('{}. {}'.format(i+1, instructions[i]))
  user = user_option(instructions)
  while user < len(instructions):
    if user == 1:
      table_number = int(input('Escriba el número de mesa: '))
      if table_number > len(tables):
        table_number = false_table(table_number)
      # Añadir feature para evitar asignar mesas ya ocupadas
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
      try:
        table_number = int(input('Escribe el número de mesa: '))
        if table_number > len(tables):
          table_number = false_table(table_number)
        status_per_table(table_number, len(tables[table_number]['name']), tables[table_number]['order']['food_items'], tables[table_number]['order']['drinks'])
      except KeyError:
        print('No hay comensales en esta mesa. Primero asigna a un comensal y despúes toma la orden.\nAcciones sugeridas: Asignar una mesa (1).')
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
  main(instructions)
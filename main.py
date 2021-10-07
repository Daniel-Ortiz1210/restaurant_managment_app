tables = {
  1: {
    'name': [],
    'vip_status': False,
    'order': {}
  },
  2: {
    'name': [],
    'vip_status': False,
    'order': {}
  },
  3: {
    'name': [],
    'vip_status': False,
    'order': {}
  },
  4: {
    'name': [],
    'vip_status': False,
    'order': {}
  },
  5: {
    'name': [],
    'vip_status': False,
    'order': {}
  },
  6: {
    'name': [],
    'vip_status': False,
    'order': {}
  },
  7: {
    'name': [],
    'vip_status': False,
    'order': {}
  }
}

instructions = ['Asignar una mesa', 'Tomar una orden', 'Calcular la cuenta de una mesa', 'Consultar el status de una mesa', 'Consultar el status de todas las mesas', 'Desocupar una mesa', 'Para salir del programa']

def assign_table(table_number, name, vip_status=False):
  while table_number > len(tables):
    print('Solo tenemos {} mesas en el restaurante.'.format(len(tables)))
    table_number = int(input('Escribe un número de mesa válido: '))
  if len(tables[table_number]['name']) >= 1:
    print('Esta mesa está ocupada. Primero espera a que los comensales se vayan y vacía la mesa con la opción 6.\nTambién puedes consultar el status del restaurante (5).')
  else:
    if vip_status == 'SI':
      vip_status = True
    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status
    print('... .... ....')
    print('¡Mesa {} asignada correctamente!\n'.format(table_number))

def assign_food_items(table_number, **order_items):
  if tables[table_number]['name'] == []:
    print('No hay comensales en esta mesa. Primero asigna a un comensal y despúes toma la orden.\nAcciones sugeridas: Asignar una mesa (1)')
  else:
    food = order_items.get('food')
    drinks = order_items.get('drinks')
    tables[table_number]['order']['food_items'] = food
    tables[table_number]['order']['drinks'] = drinks
    print('... .... ....')
    print('¡Orden tomada con éxito!\n')

def calculate_total_count_and_per_person(table_number, total, tip):
    price_per_person = (total + tip) / len(tables[table_number]['name'])
    print('... .... ....')
    print('La cuenta total de la mesa {} es ${} pesos mexicanos.\nA cada persona le toca pagar ${} pesos mexicanos.'.format(table_number, total,price_per_person))

def user_option(instructions):
  user = int(input('¿Qué deseas hacer?: '))
  while user > len(instructions):
    user = int(input('Escribe una opción valida: '))
  return user

def status_per_table(table_number, num_persons):
  if len(tables[table_number]) >= 1: 
    print('La mesa {} está ocupada por {} personas'.format(table_number, num_persons))
  else:
    print('La mesa {} está desocupada.'.format(table_number))

def overall_status():
  for num_table in tables:
    if len(tables[num_table]['name']) >= 1:
      print('| La mesa {} está ocupada. |'.format(num_table))
    else:
      print('La mesa {} está desocupada.'.format(num_table))

def empty_table(table_number):
  tables.update({1: {'name': [], 'vip_status': False}})
  print('Mesa {} vacía. Ahora otros comensales pueden usarla.'.format(table_number))

def print_instructions(instructions):
  for i in range(len(instructions)):
    print('{}. {}'.format(i+1, instructions[i]))

def main(instructions):
  print_instructions(instructions)
  user = user_option(instructions)
  while user <= len(instructions):
    if user == 1: # ---------------------------------------------------
      print('ASIGNANDO UNA MESA...\n')
      table_number = int(input('Escriba el número de mesa: '))
      names = input('Escriba el nombre de los comensales con apellidos (separados por ", "): ').title().strip().split(', ')
      vip_status = input('¿Presentan acceso VIP? (S/N): ').upper()
      assign_table(table_number, names, vip_status)
      user = int(input('¿Qué deseas hacer ahora?: '))
    elif user == 2: # ---------------------------------------------------
      print('TOMANDO UNA ORDER...\n')
      try:
        table_number = int(input('Escriba el número de mesa: '))
        print('Primero toma los alimentos y después las bebidas.')
        order_food = input('¿Qué alimentos desea ordenar el cliente?: ')
        order_drinks = input('¿Qué bebidas desea ordenar el cliente?: ')
        assign_food_items(table_number, food=order_food, drinks=order_drinks)
      except KeyError:
        print('No hay comensales en esta mesa. Primero asigna a un comensal y despúes toma la orden.\nAcciones sugeridas: Asignar una mesa (1).')
      user = int(input('¿Qué deseas hacer ahora?: '))
    elif user == 3: # ---------------------------------------------------
      print('CALCULANDO LA CUENTA...\n')
      try:
        table_number = int(input('Escribe el número de mesa: '))
        total = float(input('¿Cuál fue la cuenta total de la mesa?: '))
        tip = float(input('Escribe la propina que el cliente dió: '))
        calculate_total_count_and_per_person(table_number, total, tip)
      except KeyError:
        print('No hay comensales en esta mesa. Primero asigna a un comensal y despúes toma la orden.\nAcciones sugeridas: Asignar una mesa (1).')
      user = int(input('¿Qué deseas hacer ahora?: '))
    elif user == 4: # -------------------------------------------------------
      print('MOSTRANDO STATUS...\n')
      table_number = int(input('Escribe el número de mesa: '))
      status_per_table(table_number, len(tables[table_number]['name']))
      user = int(input('¿Qué deseas hacer ahora?: '))
    elif user == 5: # ---------------------------------------------
      print('MOSTRANDO STATUS DE TU RESTAURANTE...\n')
      overall_status()
      user = int(input('¿Qué deseas hacer ahora?: '))
    elif user == 6: # ---------------------------------------------
      print('VACIANDO UNA MESA...')
      table_number = int(input('Escribe el número de mesa: '))
      empty_table(table_number)
      user = int(input('¿Qué deseas hacer ahora?: '))
    elif user == 7: # ---------------------------------------------
      print('Saliendo del programa...')
      print('Listo! Que vuelvas pronto.')
      break

if __name__ == '__main__':
   main(instructions)
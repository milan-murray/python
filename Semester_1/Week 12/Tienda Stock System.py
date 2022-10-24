"""
Milan Murray 16/12/19
Tienda Stock System
"""
# Other
inv_stock = {1: "Cough E(TM)", 2: "Coco DUST(TM)", 3: "Liquid Lagua(TM)", 4: "Hot Ice(TM)", 5: "Cold Magma(TM)"}
user_selection = 0
search_counter = 0
add_item_counter = 0

main_menu = "\n\t\t¦===========================================¦\n" \
            "\t\t¦\t\tTienda Sistema de Inventario\t\t¦\n" \
            "\t\t¦¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¦\n" \
            "\t\t¦\t1) Buscar un elemento\t\t\t\t\t¦\n" \
            "\t\t¦\t2) Anadir un elemento al inventario\t\t¦\n" \
            "\t\t¦\t3) Actualizar un elemento en stock\t\t¦\n" \
            "\t\t¦\t4) Eliminar un elemento en stock\t\t¦\n" \
            "\t\t¦\t5) Enumerar las existencias actuales\t¦\n" \
            "\t\t¦\t6) Estadísticas de utilizacíon\t\t\t¦\n" \
            "\t\t¦\t7) Salir\t\t\t\t\t\t\t\t¦\n" \
            "\t\t¦===========================================¦\n"

search_menu = "\n\t\t¦===========================================¦\n" \
            "\t\t¦\t\t\tBuscar un elemento\t\t\t\t¦\n" \
            "\t\t¦===========================================¦\n"

add_item_menu = "\n\t\t¦===========================================¦\n" \
            "\t\t¦\t\t\tAnadir un elemento\t\t\t\t¦\n" \
            "\t\t¦===========================================¦\n"

update_stock_menu = "\n\t\t¦===========================================¦\n" \
            "\t\t¦\t\tActualizar un elemento en stock\t\t¦\n" \
            "\t\t¦===========================================¦\n"
update_stock_counter = 0

delete_item_menu = "\n\t\t¦===========================================¦\n" \
            "\t\t¦\t\tEliminar un elemento en stock\t\t¦\n" \
            "\t\t¦===========================================¦\n"
delete_item_counter = 0

total_stock_menu1 = "\n\t\t¦===================================================¦\n" \
            "\t\t¦\t\t\t\tExistencias actuales\t\t\t\t¦\n" \
            "\t\t¦===================================================¦\n" \
            "\t\t¦ ID\t¦¦ Elementos\t\t\t\t\t\t\t\t¦\n" \
            "\t\t¦¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¦"
total_stock_menu2 = "\t\t¦===================================================¦\n"

usage_menu1 = "\n\t\t¦===========================================¦\n" \
            "\t\t¦\t\tEstadísticas de Utilizacíon\t\t\t¦\n" \
            "\t\t¦¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¦"
usage_menu2 = "\t\t¦===========================================¦"

final_message = "\n\t\t¦===========================================¦\n" \
                "\t\t¦\t\t\t\tGracias\t\t\t\t\t\t¦\n" \
                "\t\t¦¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¦\n" \
                "\t\t¦ Programado por Milan Murray\tDEC 17 2019\t¦\n" \
                "\t\t¦===========================================¦"

# Constants
EXIT_VALUE = 7

# Inputs & processes
while user_selection != EXIT_VALUE:
    print(main_menu)
    user_selection = int(input("\tPor favor, introduzca una opción del menú: "))

    while user_selection < 1 or user_selection > EXIT_VALUE:
        user_selection = int(input("\tPor favor, elegir un opcíon numéica válida del menu: "))

    if user_selection == 1:     # Search For Item
        print(search_menu)
        stock_id = int(input("\tPor favor, introduzca la clave del elemento, "
                             "o introduzca \"-1\" para volver al menú principal: "))
        if stock_id != -1:

            if stock_id in inv_stock:
                search_counter += 1
                item_in_stock = inv_stock[stock_id]
                print("\n\tEl elemento con ID", stock_id, "es:", item_in_stock)
            else:
                print("\n\tNo hay ningún elemento con esta clave.")
            input("Pulsa intro para continuar...")

    elif user_selection == 2:   # Add An Item
        print(add_item_menu)
        stock_id = int(input("\tIntroduzca la llave del elemento, o escriba \"-1\" para volver al menú principal: "))

        while stock_id < -1 or stock_id == 0 or stock_id in inv_stock:  # Input validation loop
            if stock_id < -1 or stock_id == 0:  # Input validation for second part of loop (93)
                stock_id = int(input("\tPor favor, introduzca un valor positivo para un clave "
                                     "(\"-1\" para volver al menú principal): "))
            if stock_id in inv_stock:   # Test if item already occupies the selected key
                stock_id = int(input("\tYa existe un elemnto con este clave, "
                                     "por favor, vuelva a introducir una calve asignada: "))
        if stock_id != -1:
            add_item_counter += 1
            item = input("\tPor favor, introduzca el nombre del objecto: ")
            inv_stock[stock_id] = item

    elif user_selection == 3:   # Replace an item
        print(update_stock_menu)
        stock_id = int(input("\tPor favor, introduzca la clave a reemplazar, "
                             "o introduzca \"-1\" para volver al menú principal: "))

        while stock_id not in inv_stock and stock_id != -1:
            stock_id = int(input("\tNo hay un objecto con este clave, por favor, vuelva a introducir una clave: "))

        if stock_id != -1:
            update_stock_counter += 1
            item = input("\tPor favor, introduzca el nombre del objecto: ")
            inv_stock[stock_id] = item

    elif user_selection == 4:   # Delete An Item
        print(delete_item_menu)
        stock_id = int(input("\tPor favor, introduzca la clave del objecto que debe suprimirse, "
                             "o introduzca \"-1\" para volver al menú principal: "))
        while stock_id not in inv_stock and stock_id != -1:
            stock_id = int(input("\tNo hay un objecto con este clave, por favor, vuelva a introducir una clave: "
                                 "(\"-1\" para volver al menú principal: "))
        if stock_id != -1:
            delete_item_counter += 1
            del inv_stock[stock_id]
            print("Articulo eliminado.")

    elif user_selection == 5:   # Output Total Inventory
        print(total_stock_menu1)

        if inv_stock:

            for item_id in inv_stock:

                if len(inv_stock[item_id]) <= 37:
                    print("\t\t¦ {0:<6}¦¦ {1:41}¦".format(item_id, inv_stock[item_id]))
                else:
                    print("\t\t¦ {0:<6}¦¦ {1:41}¦".format(item_id, inv_stock[item_id][:38] + "..."))

        else:
            print("\t\t¦\tNo hay artículos\t\t\t\t\t\t\t\t¦")

        print(total_stock_menu2)
        input("Pulsa intro para continuar...")

    elif user_selection == 6:
        print(usage_menu1)
        print("\t\t¦\tCantidad de articulos buscado:\t{0:<4}\t\t¦".format(search_counter))
        print("\t\t¦\tCantidad de articulos añadido:\t\t{0:<4}\t\t¦".format(add_item_counter))
        print("\t\t¦\tCantidad de articulos actualizado:\t{0:<4}\t\t¦".format(update_stock_counter))
        print("\t\t¦\tCantidad de articulos eliminado:\t{0:<4}\t\t¦".format(delete_item_counter))
        print(usage_menu2)
        input("Pulsa intro para continuar...")
        # End of inner loop
    # End of outer loop

# Outputs
print(final_message)

import domain.bitacoras.crudBitacora as CRUD
from domain.bitacoras.Bitacora import Bitacora
import interface.bitacoras.Val as Val
from utils.limpiar import limpiar


def lista():
    while True:
        limpiar()

        titulo = "Listado de bitacoras"
        espacios = int((64 - len(titulo)) / 2)
        print("-" * espacios + titulo + "-" * espacios)
        print()

        print(
            f"{'  N°':<6}{'Asunto':<15}{'Destino':<15}{'Fecha Salida':<15}{'Fecha Entrada':<15}\n"
        )

        datos = CRUD.listaGeneral()
        if datos == []:
            print("No hay bitacoras.")

        lista_id = []
        if len(datos) > 0:
            for fila in datos:
                id, asunto, destino, salida, entrada, fechaSalida, fechaEntrada = fila
                lista_id.append(id)

                asunto = asunto[0:8] + ("." * (12 - 8))
                destino = destino = destino[0:8] + ("." * (12 - 8))
                fechaEntrada = fechaEntrada if fechaEntrada is not None else "---"
                fechaSalida = fechaSalida if fechaSalida is not None else "---"

                print(
                    f"  {id:<4}{asunto:<15}{destino:<15}{fechaSalida:<15}{fechaEntrada:<15}"
                )

        print()
        print("-" * 64)

        opc = None

        if opc == None:
            print("Acciones:")
            print("1. Ver bitacora completa")
            print("2. Archivar bitacora")
            print("0. Salir")

            opc = Val.IntRange("\nOpcion: ", 0, 2)

            print()
            if opc == 0: break
        if opc == 1:
            titulo = "Buscar bitacora"
            espacios = int((64 - len(titulo)) / 2)
            print("-" * espacios + titulo + "-" * espacios)

            elec = Val.IntListRange("Numero de bitacora: ", lista_id)
            bit = CRUD.leerCompleta(elec)

            print()

            if bit:
                row = bit[0]
                empleados_lista = []

                for fila in bit:
                    nombre_empleado = fila[12]
                    if nombre_empleado:
                        empleados_lista.append(nombre_empleado)

                titulo = f"Informacion bitacora N.{elec}"
                espacios = int((64 - len(titulo)) / 2)
                print("-" * espacios + titulo + "-" * espacios)

                print(f" Asunto:      {row[3]}")
                print(f" Destino:     {row[2]}")
                print("-" * 64)
                print(f" Solicitante: {row[0]}")
                print(f" Autorizado por:    {row[1]}")
                print(
                    f" Vehículo:    {row[14]}, {row[15]} (Matrícula: {row[13]})"
                )

                print("-" * 64)
                print("[Acompañantes]:")
                if empleados_lista:
                    for emp in empleados_lista:
                        print(f"> {emp}")
                else:
                    print("   (Sin acompañantes registrados)")

                print("-" * 64)

                print(" [SALIDA]:")
                print(f" Fecha y hora de salida:  {row[4]} - {row[5]}")
                print(f" Kilometraje: {row[6]} km")
                print(f" Gasolina:    {row[7]} L")

                print("-" * 64)

                print(" [ENTRADA]")
                if row[8] is not None:
                    print(f" Fecha y hora de entrada:  {row[8]} - {row[9]}")
                    print(f" Kilometraje: {row[10]} km")
                    print(f" Gasolina:    {row[11]} L")
                else:
                    print(f" Fecha y hora de entrada:  Pendiente....")
                    print(f" Kilometraje: Pendiente....")
                    print(f" Gasolina:    Pendiente....")

            print("-" * 64)
            input("Presione ENTER para continuar...")

        if opc == 2:
            titulo = "Archivar bitacora"
            espacios = int((64 - len(titulo)) / 2)
            print("-" * espacios + titulo + "-" * espacios)
            elec = Val.IntListRange("Numero de bitacora: ", lista_id)
            archivar_decision = Val.Decision("Archivar bitacora? (S / N): ")
            if archivar_decision:
                print("Bitacora archivada.")
            else:
                print("Bitacora no archivada.")
            input("Presione enter para continuar...")


def registrarSalida():
    print("\n-- Registrar salida --")

    asunto = Val.Str("Asunto: ")
    destino = Val.Str("Destino: ")
    kilometraje = Val.Float("Kilometraje: ")
    gasolina = Val.Float("Gasolina: ")

    bitacora = Bitacora()
    bitacora.set_asunto(asunto)
    bitacora.set_destino(destino)
    bitacora.registrar_salida(kilometraje, gasolina)

    lastid = CRUD.crearSalida(bitacora)

    if (lastid == -1):
        print("No se pudo registrar.")
        return
    else:
        print("Bitacora registrada.")
    print()

    bitacora.set_numControl(lastid)

    print(bitacora)


def registrarEntrada():
    print("\n-- Registrar entrada --")

    print("Bitacoras sin entrada:")
    bitacoras_sin_entrada = CRUD.bitacoraSinEntrada()
    print()

    if bitacoras_sin_entrada == 0:
        print("No hay bitacoras.")
        return

    numControl = Val.Int("Numero de control: ")

    bitacora = Bitacora()
    bitacora.set_numControl(numControl)

    existe = CRUD.existe(bitacora)
    if len(existe) == 0:
        print(
            f"No existe la bitacora con el numero de control {numControl}.\n")
        return

    bitacora = completar_objeto(bitacora, existe[0])

    kilometraje = Val.KMEntrada("Kilometraje: ",
                                bitacora.get_salida().get_kilometraje())
    gasolina = Val.GasEntrada("Gasolina: ",
                              bitacora.get_salida().get_gasolina())

    bitacora.registrar_entrada(kilometraje, gasolina)
    bitacora.calcular_gasolinaConsumida()
    bitacora.calcular_kilometrajeTotal()
    bitacora.calcular_gasolinaRendimiento()

    rowcount = CRUD.crearEntrada(bitacora)
    if rowcount == -1:
        print("No se pudo registrar la entrada.")
        return

    print(bitacora)


def eliminar():
    print("\n-- Eliminar --")
    print("Bitacoras:")
    bitacoras = CRUD.listaGeneral()
    print()

    numControl = Val.Int("Numero de control: ")

    bitacora = Bitacora()
    bitacora.set_numControl(numControl)

    existe = CRUD.existe(bitacora)
    if len(existe) == 0:
        print(
            f"No existe la bitacora con el numero de control {numControl}.\n")
        return

    elegir = Val.Decision("Borrar la bitacora? (Si / No): ")
    if elegir:
        rowcount = CRUD.baja(bitacora)
        if rowcount == -1:
            print("No se pudo eliminar la bitacora.")
            return

        print("Bitacora eliminada.")
    else:
        print("Eliminacion cancelada.")
    print()


def modificar():
    print("\n-- Modificar destino --")
    bitacoras = CRUD.listaGeneral()
    print()

    numControl = Val.Int("Numero de control: ")

    bitacora = Bitacora()
    bitacora.set_numControl(numControl)

    existe = CRUD.existe(bitacora)
    if len(existe) == 0:
        print(
            f"No existe la bitacora con el numero de control {numControl}.\n")
        return

    nuevoDestino = Val.Str("Nuevo destino: ")

    bitacora.set_destino(nuevoDestino)

    elegir = Val.Decision("Modificar la bitacora? (Si / No): ")
    if elegir:
        rowcount = CRUD.actualizarDestino(bitacora)
        if rowcount == -1:
            print("No se pudo actualizar la bitacora.")
            return

        print("Destino actualizado.")
    else:
        print("Actualizacion cancelada.")
    print()


def completar_objeto(bitacora: Bitacora, tupla):
    bitacora.set_asunto(tupla[0])
    bitacora.set_destino(tupla[1])
    bitacora.set_responsable(tupla[2])
    bitacora.set_autorizador(tupla[3])
    bitacora.set_vehiculo(tupla[4])
    bitacora.registrar_salida(tupla[5], tupla[6])
    bitacora.get_salida().set_fecha(tupla[7])
    bitacora.get_salida().set_hora(tupla[7])

    return bitacora

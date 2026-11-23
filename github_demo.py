import subprocess


def ejecutar(comando):
    resultado = subprocess.run(
        comando,
        cwd=".",
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )

    if resultado.stdout:
        print(resultado.stdout, end="")
    if resultado.stderr:
        print(resultado.stderr, end="")
    if resultado.returncode != 0:
        print(f"\nComando terminado con error (codigo {resultado.returncode}).")

    return resultado.returncode


def confirmar(mensaje):
    respuesta = input(f"{mensaje} (s/n): ").strip().lower()
    return respuesta == "s"


def mostrar_menu():
    print("\n=== Practica Git y GitHub ===")
    print("1. Ver estado del repositorio")
    print("2. Ver cambios sin guardar")
    print("3. Ver cambios preparados")
    print("4. Ver historial")
    print("5. Ver ramas")
    print("6. Ver remotos configurados")
    print("7. Descargar cambios de GitHub (fetch)")
    print("8. Actualizar la rama local (pull)")
    print("9. Comparar con la rama principal remota")
    print("10. Subir cambios (push)")
    print("11. Preparar todos los cambios")
    print("12. Crear commit")
    print("0. Salir")


def principal():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opcion: ").strip()

        if opcion == "1":
            ejecutar(["git", "status", "--branch", "--short"])
        elif opcion == "2":
            ejecutar(["git", "diff"])
        elif opcion == "3":
            ejecutar(["git", "diff", "--cached"])
        elif opcion == "4":
            ejecutar(["git", "log", "--oneline", "--graph", "--decorate", "-12"])
        elif opcion == "5":
            ejecutar(["git", "branch", "--all", "--verbose"])
        elif opcion == "6":
            ejecutar(["git", "remote", "-v"])
        elif opcion == "7":
            ejecutar(["git", "fetch", "--all", "--prune"])
        elif opcion == "8":
            if confirmar("Esto puede actualizar tus archivos locales"):
                ejecutar(["git", "pull", "--ff-only"])
        elif opcion == "9":
            ejecutar(["git", "diff", "HEAD", "origin/main"])
        elif opcion == "10":
            if confirmar("Esto enviara tus commits a GitHub"):
                ejecutar(["git", "push"])
        elif opcion == "11":
            ejecutar(["git", "add", "-A"])
            print("Cambios preparados.")
        elif opcion == "12":
            mensaje = input("Escribe el mensaje del commit: ").strip()
            if mensaje:
                ejecutar(["git", "commit", "-m", mensaje])
            else:
                print("El mensaje no puede estar vacio.")
        elif opcion == "0":
            print("Hasta pronto.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    principal()

import func
import click
import validaciones as val

@click.group()
def gdt():
    pass

@gdt.command()
@click.argument('nombre', type=str)
@click.option('--estado', type=str, help="Estado de la tarea (Pendiente, En-curso, Terminada)")
@click.option('--desc', type=str, help="Descripcion de la tarea")
@click.pass_context
def add(ctx,nombre,estado,desc):
    if(not(nombre.strip())):
        ctx.fail("Nombre requerido!")
    else:
        if (estado is None): estado = ""
        if (desc is None): desc = ""
        estado = val.validarEstado(estado)
        if(estado is None):
            ctx.fail("Estado invalido!")

        id = func.crearTarea(nombre,estado,desc)
        print(f"\nTarea creada con exito! ID: {id}")


@gdt.command()
@click.argument('id', type=int)
@click.option('--nombre', type=str, help="Nombre de la tarea")
@click.option('--estado', type=str, help="Estado de la tarea (Pendiente, En-curso, Terminada)")
@click.option('--desc', type=str, help="Descripcion de la tarea")
@click.pass_context
def mod(ctx,id,nombre,estado,desc):
    if(not val.existeId(id)):
        ctx.fail(f"ID {id} no existe!")
    if(estado is not None):
        if(not val.validarEstado(estado)):
            ctx.fail("Estado invalido!")
    if(not func.modificarTarea(id,nombre,estado,desc)):
        print("La tarea no fue modificada...")
    else:
        print(f"Tarea ID: {id} modificada!")


@gdt.command()
@click.argument('id', type=int)
@click.pass_context
def rm(ctx,id):
    if(not val.existeId(id)):
        ctx.fail(f"ID {id} no existe!")
    else:
        print(f"¿Eliminar tarea ID {id}? S/N: ",end="")
        opcion = input().lower()
        if(opcion != 's' and opcion != 'n'):
            ctx.fail("Opcion invalida!")
        else:
            if(opcion == "s"):
                func.eliminarTarea(id)
                print(f"Tarea ID {id} eliminada!")


@gdt.command()
@click.option('--estado', type=str, help="Filtro por estado")
@click.option('--fecha', type=str, help="Filtro por fecha de inicio")
@click.pass_context
def list(ctx,estado,fecha):
    if(estado is not None):
        if(not val.validarEstado(estado)):
            ctx.fail("Estado invalido!")
    if(fecha is not None):
        if(not val.validarFecha(fecha)):
            ctx.fail("Fecha invalida!")
    func.listarTareas(estado,fecha)


if __name__ == "__main__":
    gdt()
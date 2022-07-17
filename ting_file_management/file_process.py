from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)
    dic_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file
    }
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None
    instance.enqueue(dic_file)
    return sys.stdout.write(str(dic_file))


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    removed_file = instance.dequeue()
    if removed_file is not None:
        return sys.stdout.write(
            f'Arquivo {removed_file["nome_do_arquivo"]} removido com sucesso\n'
        )


def file_metadata(instance, position):
    try:
        file_infos = instance.search(position)
        return sys.stdout.write(str(file_infos))
    except IndexError:
        return sys.stderr.write("Posição inválida\n")

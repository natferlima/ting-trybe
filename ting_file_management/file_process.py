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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""

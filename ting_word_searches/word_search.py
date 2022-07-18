def exists_word(word, instance):
    occurrences = []
    result = []
    for i in range(len(instance)):
        file = instance.search(i)
        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                occurrences.append({"linha": index + 1})
        if occurrences != []:
            result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""

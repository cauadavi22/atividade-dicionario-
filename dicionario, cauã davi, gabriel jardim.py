caua = {
    "portugues": [15, 20],
    "geografia": [11, 16],
    "matematica": [15, 19]
}

gabriel = {
    "ingles": [12, 19],
    "biologia": [11, 16],
    "fisica": [10, 19]
}

cesar = {
    "quimica": [14, 20],
    "historia": [11, 17],
    "educacao fisica": [25, 30]
}

alunos = {
    "caua": caua,
    "gabriel": gabriel,
    "cesar": cesar
}

def media_mat(nome, alunos):
    if nome in alunos:
        total = 0
        quantidade = 0
        for notas in alunos[nome].values():
            total += sum(notas)
            quantidade += len(notas)
        return total / quantidade if quantidade > 0 else 0
    else:
        return None

def melhora(alunos):
    melhor = None
    maior_media = -1
    for nome in alunos:
        media = media_mat(nome, alunos)
        if media is not None and media > maior_media:
            maior_media = media
            melhor = nome
    return melhor, maior_media

def media_aluno():
    for nome, materias in alunos.items():
        print(f"Aluno: {nome}")
        for materia, notas in materias.items():
            media = sum(notas) / len(notas)
            print(f"{materia}: média = {media:.2f}")
    media_por_alunos()

    media_geral():
    

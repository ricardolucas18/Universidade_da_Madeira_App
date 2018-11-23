# -*- coding: utf-8 -*-
"""
_author_    = "Ricardo Lucas"
_copyright_ = "Copyright 2018, ESTIG - IPBeja"
_version_   = "18:30 02/02/2018"
"""
from app_creation import app
from flask import render_template
from app_creation import db
from flask_bootstrap import Bootstrap
from db_creation import Universidades, Cursos, unidadesCurriculares, Professores
import data_processing
Bootstrap(app)

#Este for é para apanhar as informações que vão entarr em todas as páginas como por exemplo s contactos, mail...
for nome, historia, reitor, ano, morada, telefone, fax, email_uni, email_reitoria, horario, localidade in db.session.query(
        Universidades.nome,
        Universidades.historia,
        Universidades.reitor,
        Universidades.ano_origem,
        Universidades.morada,
        Universidades.telefone,
        Universidades.fax,
        Universidades.email_uni,
        Universidades.email_reitoria,
        Universidades.horario_atendimento,
        Universidades.localidade):
    nome = nome
    historia = historia
    reitor = reitor
    ano = ano
    morada = morada
    telefone = telefone
    fax = fax
    email_uni = email_uni
    email_reitoria = email_reitoria
    horario = horario
    localidade = localidade


@app.route("/")
def index():
    '''
    Def do Index
    :return: Return da template index, com as varáveis
    '''
    return render_template('index.html', nomeUniversidade=nome, moradaUniversidade=morada,
                           telefoneUniversidade=telefone, faxUniversidade=fax, email_Universidade=email_uni,
                           email_reitoriaUniversidade=email_reitoria, horarioUniversidade=horario)


@app.route("/index")
def home():
    '''
    Def do home
    :return: Return da template index, com as varáveis
    '''
    return render_template('index.html', nomeUniversidade=nome, moradaUniversidade=morada,
                           telefoneUniversidade=telefone, faxUniversidade=fax, email_Universidade=email_uni,
                           email_reitoriaUniversidade=email_reitoria, horarioUniversidade=horario)


@app.route("/about")
def about():
    '''
    Def do about
    :return: Return da template about, com as varáveis
    '''
    return render_template('about.html', nomeUniversidade=nome, localidadeUniversidade=localidade,
                           reitorUniversidade=reitor, historiaUniversidade=historia, anoUniversidade=ano,
                           moradaUniversidade=morada, telefoneUniversidade=telefone, faxUniversidade=fax,
                           email_Universidade=email_uni, email_reitoriaUniversidade=email_reitoria,
                           horarioUniversidade=horario)


@app.route("/contacts")
def contacts():
    '''
    Def do contacts
    :return: Return da template contacts, com as varáveis
    '''
    return render_template('contacts.html', nomeUniversidade=nome, moradaUniversidade=morada,
                           telefoneUniversidade=telefone, faxUniversidade=fax, email_Universidade=email_uni,
                           email_reitoriaUniversidade=email_reitoria, horarioUniversidade=horario)


@app.route("/offers")
def cursos():
    '''
    Def do cursos
    :return: Return da template offers, com as varáveis
    '''
    cursos = []
    cursos_id = []
    for var, escola_id, nome_curso, cursosId in db.session.query(Cursos.escola_id == '2', Cursos.escola_id,
                                                                 Cursos.nome_curso, Cursos.id):
        if (var == True):
            cursos.append(nome_curso)
            cursos_id.append(cursosId)
    return render_template('offers.html', moradaUniversidade=morada,
                           telefoneUniversidade=telefone, faxUniversidade=fax, email_Universidade=email_uni,
                           email_reitoriaUniversidade=email_reitoria, horarioUniversidade=horario,
                           nomeUniversidade=nome, cursos=cursos, cursos_id=cursos_id)


@app.route("/offers/<id>")
def cursosPages(id):
    '''
    Def do Cursos Pages
    :return: Return da template offersPages, com as varáveis
    '''
    cadeiras = []
    for var, nome_curso, tipo_curso, cod_escola, duracao, saidas_descricao, nome_director, email_director, objectivos_curso in db.session.query(
                    Cursos.id == id, Cursos.nome_curso, Cursos.tipo_curso, Cursos.cod_escola, Cursos.duracao_curso,
            Cursos.saidas_descricao, Cursos.nome_director, Cursos.email_director, Cursos.objectivos_curso):
        if (var == True):
            nome_curso = nome_curso
            tipo_curso = tipo_curso
            cod_escola = cod_escola
            duracao = duracao
            saidas_descricao = saidas_descricao
            nome_director = nome_director
            email_director = email_director
            objectivos_curso = objectivos_curso

    for var, nome_disciplina, area_cientifica, nivel, ficha_descritiva, disciplina_ativa, ano_curricular, semestre, horas_teoricas_semanal, horas_teorica_praticas_semanal, horas_praticas_laboratorial, horas_trabalho_campo, horas_seminario_semanal, horas_estagio_semanal, horas_orientacao_tutorial_semanal, creditos_disciplina in db.session.query(
                    unidadesCurriculares.curso_id == id, unidadesCurriculares.nome_disciplina,
            unidadesCurriculares.area_cientifica, unidadesCurriculares.nivel, unidadesCurriculares.ficha_descritiva,
            unidadesCurriculares.disciplina_ativa, unidadesCurriculares.ano_curricular, unidadesCurriculares.semestre,
            unidadesCurriculares.horas_teoricas_semanal, unidadesCurriculares.horas_teorica_praticas_semanal,
            unidadesCurriculares.horas_praticas_laboratorial, unidadesCurriculares.horas_trabalho_campo,
            unidadesCurriculares.horas_seminario_semanal, unidadesCurriculares.horas_estagio_semanal,
            unidadesCurriculares.horas_orientacao_tutorial_semanal,
            unidadesCurriculares.creditos_disciplina):
        if (var == True):
            cadeira = dict(nome_disciplina=nome_disciplina, area_cientifica=area_cientifica, nivel=nivel,
                           ficha_descritiva=ficha_descritiva, disciplina_ativa=disciplina_ativa,
                           ano_curricular=ano_curricular,
                           semestre=semestre, horas_teoricas_semanal=horas_teoricas_semanal,
                           horas_teorica_praticas_semanal=horas_teorica_praticas_semanal,
                           horas_praticas_laboratorial=horas_praticas_laboratorial,
                           horas_trabalho_campo=horas_trabalho_campo, horas_seminario_semanal=horas_seminario_semanal,
                           horas_estagio_semanal=horas_estagio_semanal,
                           horas_orientacao_tutorial_semanal=horas_orientacao_tutorial_semanal,
                           creditos_disciplina=creditos_disciplina)
            cadeiras.append(cadeira)

    return render_template('offersPages.html', moradaUniversidade=morada,
                           telefoneUniversidade=telefone, faxUniversidade=fax, email_Universidade=email_uni,
                           email_reitoriaUniversidade=email_reitoria, horarioUniversidade=horario, nomeCurso=nome_curso,
                           tipoCurso=tipo_curso, codEscola=cod_escola,
                           duracaoCurso=duracao, saidasCurso=saidas_descricao, nomeDirector=nome_director,
                           emaiDirector=email_director, objectivosCurso=objectivos_curso, cadeirasCurso=cadeiras)


@app.route("/docentes")
def docentes():
    '''
    Def de Docentes
    :return: Return da template docentes, com as varáveis
    '''
    docentes = []

    for id_docentes, nome_docente, email_docente, habilitacoes_docente, cadeiras_docente, responsabilidades_docente, actividade_docente, salario_docente, area_pesquisa, licenciatura, mestrado, doutoramento in db.session.query(
            Professores.id, Professores.nome_professor, Professores.email_professor, Professores.habilitacoes,
            Professores.cadeiras_lecionadas, Professores.responsabilidades, Professores.actividade_profissional,
            Professores.media_salario, Professores.area_pesquisa,
            Professores.licenciatura, Professores.mestrado, Professores.doutoramento):
        docente = dict(id_docentes=id_docentes, nome_docente=nome_docente, email_docente=email_docente,
                       habilitacoes_docente=habilitacoes_docente, cadeiras_docente=cadeiras_docente,
                       responsabilidades_docente=responsabilidades_docente, actividade_docente=actividade_docente,
                       salario_docente=salario_docente, area_pesquisa=area_pesquisa, licenciatura=licenciatura,
                       mestrado=mestrado, doutoramento=doutoramento)
        docentes.append(docente)

    return render_template('docentes.html', moradaUniversidade=morada,
                           telefoneUniversidade=telefone, faxUniversidade=fax, email_Universidade=email_uni,
                           email_reitoriaUniversidade=email_reitoria, horarioUniversidade=horario, docentes=docentes)

@app.route("/docentes/<id>")
def docentePage(id):
    '''
    Def do dodentesPage
    :arg id (int): Id do Docente
    :return: Return da template docentePage, com as varáveis
    '''

    for id_docentes, nome_docente, email_docente, habilitacoes_docente, cadeiras_docente, responsabilidades_docente, actividade_docente, salario_docente, area_pesquisa, licenciatura, mestrado, doutoramento in db.session.query(
            Professores.id == id, Professores.nome_professor, Professores.email_professor, Professores.habilitacoes,
            Professores.cadeiras_lecionadas, Professores.responsabilidades, Professores.actividade_profissional,
            Professores.media_salario, Professores.area_pesquisa,
            Professores.licenciatura, Professores.mestrado, Professores.doutoramento):
        if(id_docentes == True):
            nome_docente = nome_docente
            email_docente = email_docente
            habilitacoes = habilitacoes_docente
            print(habilitacoes_docente)
            cadeiras_docente = cadeiras_docente
            responsabilidades_docente = responsabilidades_docente
            actividade_docente = actividade_docente
            salario_docente = salario_docente
            area_pesquisa = area_pesquisa
            pos_licenciatura = licenciatura
            pos_mestrado = mestrado
            pos_doutoramento = doutoramento

    return render_template('docentePage.html', moradaUniversidade=morada,
                           telefoneUniversidade=telefone, faxUniversidade=fax, email_Universidade=email_uni,
                           email_reitoriaUniversidade=email_reitoria, horarioUniversidade=horario, nome_docente=nome_docente,email_docente=email_docente, habilitacoes_docente=habilitacoes, cadeiras_docente=cadeiras_docente,responsabilidades_docente = responsabilidades_docente, actividade_docente=actividade_docente, salario_docente = salario_docente, area_pesquisa=area_pesquisa, licenciatura = pos_licenciatura, mestrado = pos_mestrado, doutoramento=pos_doutoramento)

@app.route("/statistics")
def statistics():
    '''
    Def do statistics
    :return: Return da template statistics
    '''

    return render_template('statistics.html')

if __name__ == "__main__":
    app.run()

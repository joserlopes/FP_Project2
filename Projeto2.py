# Projeto realizado por:
# José António Lopes, Nº103938, Mail:jose.r.lopes@tecnico.ulisboa.pt

# ----------------------------------------------------------TAD_Posicao-------------------------------------------------


#-----------------------------Construtores---------------------------------------------------

def cria_posicao(x, y):
    '''
        int × int --> posicao

        Esta função recebe os valores correspondentes às coordenadas de uma posição e devolve a posição correspondente.
        Esta função verifica a validade dos argumentos (números inteiros positivos, 0 inclusive), gerando
        um ValueError com a mensagem 'cria_posicao:argumentos invalidos'
        caso os seus argumentos não sejam válidos.

        Representação interna do TAD: tuplo
    '''
    if type(x) != int or type(y) != int or x < 0 or y < 0:
        raise ValueError("cria_posicao: argumentos invalidos")
    return (x, y)


def cria_copia_posicao(pos):
    '''
        posicao --> posicao

        Esta função recebe uma posição (pos) e devolve uma cópia dela

    '''
    return (pos[0], pos[1])

#-----------------------------Seletores------------------------------------------------------


def obter_pos_x(pos):
    '''
        posicao --> int

        Esta função recebe uma posição (pos) e devolve a sua abcissa

    '''
    return pos[0]

def obter_pos_y(pos):
    '''
        posicao --> int

        Esta função recebe uma posição (pos) e devolve a sua ordenada

    '''
    return pos[1]

#-----------------------------Reconhecedor---------------------------------------------------
def eh_posicao(arg):
    '''
        universal --> bool

        Esta função devolve True caso o seu argumento seja um TAD posicao e
        False caso contrário.

    '''
    if type(arg) == tuple and len(arg) == 2 and type(obter_pos_x(arg)) == int \
            and type(obter_pos_y(arg)) == int and obter_pos_x(arg) >= 0 and obter_pos_y(arg) >= 0:
        return True
    return False


#-----------------------------Teste----------------------------------------------------------

def posicoes_iguais(pos1, pos2):
    '''
        posicao x posicao --> bool

        Esta função devolve True caso os seus argumentos correspondam a posições e sejam iguais

    '''
    if eh_posicao(pos1) and eh_posicao(pos2):
        if obter_pos_x(pos1) == obter_pos_x(pos2) and obter_pos_y(pos1) == obter_pos_y(pos2):
            return True
    return False

#-----------------------------Transformador--------------------------------------------------

def posicao_para_str(pos):
    '''
        posicao --> str

        Esta função devolve a cadeia de caracteres '(x, y)' que representa o
        seu argumento, sendo os valores x e y as coordenadas do argumento.

    '''
    return str(pos)

#-----------------------------Func_alto_nivel------------------------------------------------
def obter_posicoes_adjacentes(pos):
    '''
        posicao --> tuplo

        Esta função devolve um tuplo com as posições adjacentes ao argumento,
        começando pela posição acima do argumento (se posível) e seguindo no sentido horário.

    '''
    if obter_pos_x(pos) == 0 and obter_pos_y(pos) == 0:
        return (cria_posicao(obter_pos_x(pos) + 1, obter_pos_y(pos)), cria_posicao(obter_pos_x(pos), obter_pos_y(pos) + 1))
    if obter_pos_x(pos) == 0:
        return (cria_posicao(obter_pos_x(pos), obter_pos_y(pos) -1), cria_posicao(obter_pos_x(pos) + 1, obter_pos_y(pos)), cria_posicao(    obter_pos_x(pos), obter_pos_y(pos) + 1))
    if obter_pos_y(pos) == 0 or obter_pos_y(pos) == 1:
        return (cria_posicao(obter_pos_x(pos) + 1, obter_pos_y(pos)), cria_posicao(obter_pos_x(pos), obter_pos_y(pos) + 1), cria_posicao(obter_pos_x(pos) - 1, obter_pos_y(pos)))
    return (cria_posicao(obter_pos_x(pos), obter_pos_y(pos) - 1), cria_posicao(obter_pos_x(pos) + 1, obter_pos_y(pos)), cria_posicao(obter_pos_x(pos), obter_pos_y(pos) + 1),cria_posicao(obter_pos_x(pos) - 1, obter_pos_y(pos)))


def ordenar_posicoes(pos):
    '''
        tuplo --> tuplo

        Esta função devolve um tuplo contendo as mesmas posições do tuplo fornecido
        como argumento, ordenadas de acordo com a ordem de leitura do prado
        (da esquerda para a direita, de cima para baixo).

    '''
    pos_barreira = ()
    for create_pos in pos:
        pos_barreira += (cria_posicao(create_pos[0], create_pos[1]),)
    return tuple(sorted(pos_barreira, key=lambda x: (x[1], x[0])))

# ----------------------------------------------------------TAD_Animal--------------------------------------------------


#-----------------------------Construtores---------------------------------------------------


def cria_animal(spec, rep, food):
    '''
         str, int, int --> animal

         Esta função recebe uma cadeia de caracteres 'spec' não vazia correspondente
         à espécie do animal e dois valores inteiros correspondentes à frequência
         de reprodução rep (maior do que 0) e à frequência de alimentação food (maior
         ou igual que 0); e devolve o animal. Animais com frequência de alimentação
         maior que 0 são considerados predadores, caso contrário são considerados
         presas. O construtor verifica a validade dos seus argumentos, gerando um
         ValueError com a mensagem 'cria_animal: argumentos invalidos' caso
         os seus argumentos não sejam válidos.

         Representação interna do TAD: dicionário

    '''
    if not(type(spec) == str and spec != "" and type(rep) == int and rep > 0 and type(food) == int and food >= 0):
        raise ValueError("cria_animal: argumentos invalidos")
    return {"s":spec, "r": [0,rep], "f": [0,food]}

def cria_copia_animal(a):
    '''
         animal --> animal

         Esta função recebe um animal (predador ou presa) e devolve uma
         nova cópia do animal.
     '''
    r = a["r"].copy()
    f = a["f"].copy()
    return {"s":a["s"], "r": r, "f": f}

#-----------------------------Seletores------------------------------------------------------

def obter_especie(animal):
    '''
          animal --> str

          Esta função recebe um animal e devolve a cadeia de caracteres correspondente à espécie do
          animal.
    '''
    return animal["s"]

def obter_freq_reproducao(animal):
    '''
          animal --> int

          Esta função recebe um animal e devolve a frequência de reprodução do animal.
    '''
    return animal["r"][1]

def obter_freq_alimentacao(animal):
    '''
          animal --> int

          Esta função recebe um animal e devolve a frequência de alimentação do animal
          (as presas devolvem sempre 0).
    '''
    if animal["r"][1] > 0:
        return animal["f"][1]
    return 0

def obter_idade(animal):
    '''
          animal --> int

          Esta função recebe um animal e devolve a idade do animal.
    '''
    return animal["r"][0]

def obter_fome(animal):
    '''
          animal --> int

          Esta função recebe um animal e devolve a fome do animal a (as presas devolvem sempre 0).
    '''
    if animal["r"][1] > 0:
        return animal["f"][0]
    return 0

#-----------------------------Reconhecedores-----------------------------------------------------

def eh_animal(arg):
    '''
          universal --> bool

          Esta função recebe um argumento universal e devolve True caso o seu argumento seja um TAD animal e
          False caso contrário.
    '''
    if type(arg) == dict and "s" in arg and "r" in arg and "f" in arg and (type(arg["s"]) == str
    and arg["s"] != "" and type(arg["r"]) == list and arg["r"][1] > 0 and type(arg["f"]) == list and arg["f"][1] >= 0):
        return True
    return False

def eh_predador(arg):
    '''
          universal --> bool

          Esta função recebe um argumento universal e devolve True caso o seu argumento seja um TAD animal do
          tipo predador e False caso contrário.
    '''
    if not eh_animal(arg):
        return False
    if obter_freq_alimentacao(arg) > 0:
        return True
    return False

def eh_presa(arg):
    '''
          universal --> bool

          Esta função recebe um argumento universal e devolve True caso o seu argumento seja um TAD animal do
          tipo presa e False caso contrário.
    '''
    if not eh_animal(arg):
        return False
    if obter_freq_alimentacao(arg) == 0:
        return True
    return False

#-----------------------------Modificadores------------------------------------------------------

def aumenta_idade(animal):
    '''
          animal --> animal

          Esta função recebe um animal e modifica destrutivamente o animal incrementando o valor
          da sua idade em uma unidade, e devolve o próprio animal.
    '''
    animal["r"][0] += 1
    return animal

def reset_idade(animal):
    '''
          animal --> animal

          Esta função recebe um animal e modifica destrutivamente o animal definindo o valor da sua
          idade igual a 0, e devolve o próprio animal.
    '''
    animal["r"][0] = 0
    return animal


def aumenta_fome(animal):
    '''
          animal --> animal

          Esta função recebe um animal e modifica destrutivamente o animal predador incrementando
          o valor da sua fome em uma unidade, e devolve o próprio animal. Esta
          função não modifica os animais presa.
    '''
    if eh_predador(animal):
        animal["f"][0] += 1
    return animal

def reset_fome(animal):
    '''
          animal --> animal

          Esta função recebe um animal e modifica destrutivamente o animal predador definindo o valor
          da sua fome igual a 0, e devolve o próprio animal. Esta operação não modifica
          os animais presa.
    '''
    animal["f"][0] = 0
    return animal


#-----------------------------Teste-----------------------------------------------------------

def animais_iguais(a1, a2):
    '''
          animal x animal --> bool

          Esta função recebe dois animais e devolve True apenas se os dois são animais e são iguais.
    '''
    if not eh_animal(a1):
        return False
    if not eh_animal(a2):
        return False
    if (obter_especie(a1) == obter_especie(a2) and obter_freq_alimentacao(a1) == obter_freq_alimentacao(a2)\
            and obter_freq_reproducao(a1) == obter_freq_reproducao(a2) and obter_fome(a1) == obter_fome(a2)\
            and obter_idade(a1) == obter_idade(a2)):
        return True
    return False


#-----------------------------Transformadores-----------------------------------------------------------

def animal_para_char(animal):
    '''
          animal --> str

          Esta função recebe um animal e devolve a cadeia de caracteres dum único elemento correspondente
          ao primeiro caracter da espécie do animal passada por argumento,
          em maiúscula para animais predadores e em minúscula para animais presa.
    '''
    if eh_predador(animal):
        return obter_especie(animal)[0].upper()
    else:
        return obter_especie(animal)[0].lower()


def animal_para_str(animal):
    '''
          animal --> str

          Esta função recebe um animal e devolve a cadeia de caracteres que representa o animal
          de acordo com a estrutura: "'espécie' [idade/freq_reproducao] caso o animal seja presa
          e "'espécie' [idade/freq_reproducao;fome/freq_alimentacao] caso o animal seja predador.
    '''
    if eh_presa(animal):
        return obter_especie(animal) + " " + "[" + str(obter_idade(animal)) + "/" + str(obter_freq_reproducao(animal)) + "]"
    else:
        return obter_especie(animal) + " " + "[" + str(obter_idade(animal)) + "/" + str(obter_freq_reproducao(animal)) + ";" + \
        str(obter_fome(animal)) + "/" + str(obter_freq_alimentacao(animal)) + "]"


#-----------------------------Func_alto_nivel-----------------------------------------------------------

def eh_animal_fertil(animal):
    '''
          animal --> bool

          Esta função recebe um animal e devolve True caso o animal tenha atingido a
          idade de reprodução (idade = freq_reproducao) e False caso contrário.
    '''
    if obter_idade(animal) == obter_freq_reproducao(animal):
        return True
    return False

def eh_animal_faminto(animal):
    '''
          animal --> bool

          Esta função recebe um animal e devolve True caso o animal a tenha atingindo um valor de
          fome igual ou superior à sua frequência de alimentação e False caso contrário.
          As presas devolvem sempre False.
    '''
    if eh_presa(animal):
        return False
    if obter_fome(animal) >= obter_freq_alimentacao(animal):
        return True
    return False

def reproduz_animal(animal):
    '''
          animal --> bool

          Esta função recebe um animal e devolve um novo animal da mesma espécie
          com idade e fome igual a 0, e modificando destrutivamente o animal passado
          como argumento a alterando a sua idade para 0.
    '''
    reset_idade(animal)
    a = cria_copia_animal(animal)
    reset_fome(a)
    return a

# ----------------------------------------------------------TAD_Prado---------------------------------------------------


#-----------------------------Construtores---------------------------------------------------


def cria_prado(d, r, a, p):
    '''
          posicao x tuplo x tuplo x tuplo --> prado

          Esta função recebe uma posição d correspondente à posição que
          ocupa a montanha do canto inferior direito do prado, um tuplo r de 0 ou
          mais posições correspondentes aos rochedos que não são as montanhas dos
          limites exteriores do prado, um tuplo a de 1 ou mais animais, e um tuplo p da
          mesma dimensão do tuplo a com as posições correspondentes ocupadas pelos
          animais; e devolve o prado que representa internamente o mapa e os animais
          presentes. O construtor verifica a validade dos seus argumentos, gerando um
          ValueError com a mensagem 'cria prado: argumentos invalidos' caso
          os seus argumentos não sejam válidos.

          Representação interna do TAD: dicionário
    '''
    if not (eh_posicao(d) and type(r) == tuple and type(a) == tuple and len(a) >= 1 and type(p) == tuple and len(p) == len(a)):
        raise ValueError("cria_prado: argumentos invalidos")
    if not eh_posicao(d):
        raise ValueError("cria_prado: argumentos invalidos")
    for pos_obstaculos in r:
        if not eh_posicao(pos_obstaculos):
            raise ValueError("cria_prado: argumentos invalidos")
        if obter_pos_x(pos_obstaculos) == 0 or obter_pos_x(pos_obstaculos) == 0 or obter_pos_x(pos_obstaculos) >= obter_pos_x(d) or obter_pos_y(pos_obstaculos) >= obter_pos_y(d):
            raise ValueError("cria_prado: argumentos invalidos")
    for animal in a:
        if not eh_animal(animal):
            raise ValueError("cria_prado: argumentos invalidos")
    for pos_animal in p:
        if not eh_posicao(pos_animal):
            raise ValueError("cria_prado: argumentos invalidos")
        if obter_pos_x(pos_animal) == 0 or obter_pos_y(pos_animal) == 0 or obter_pos_x(pos_animal) >= obter_pos_x(d) or obter_pos_y(pos_animal) >= obter_pos_y(d):
            raise ValueError("cria_prado: argumentos invalidos")
    return {"d":d, "r":r, "a":a, "p":p}

def cria_copia_prado(prado):
    '''
          prado --> prado

          Esta função recebe um prado e devolve uma nova cópia do prado.
    '''
    d = cria_copia_posicao(prado["d"])
    r = prado["r"]
    a = prado["a"]
    p = prado["p"]
    return {"d":d, "r":r, "a":a,"p":p}

#-----------------------------Seletores------------------------------------------------------

def obter_tamanho_x(prado):
    '''
          prado --> int

          Esta função recebe um prado e devolve o valor inteiro que corresponde à dimensão Nx
          do prado.
    '''
    return prado["d"][0] + 1

def obter_tamanho_y(prado):
    '''
          prado --> int

          Esta função recebe um prado e devolve o valor inteiro que corresponde à dimensão Ny
          do prado.
    '''
    return prado["d"][1] + 1

def obter_numero_predadores(prado):
    '''
          prado --> int

          Esta função recebe um prado e devolve devolve o número de animais predadore no prado.
    '''
    count = 0
    for animal in prado["a"]:
        if eh_predador(animal):
            count += 1
    return count

def obter_numero_presas(prado):
    '''
          prado --> int

          Esta função recebe um prado e devolve devolve o número de animais presa no prado.
    '''
    count = 0
    for animal in prado["a"]:
        if eh_presa(animal):
            count += 1
    return count

def obter_posicao_animais(prado):
    '''
          prado --> tuplo posicoes

          Esta função recebe um prado e devolve um tuplo contendo as posições do prado
          ocupadas por animais, ordenadas em ordem de leitura do prado
          (da esquerda para a direita, de cima para baixo).
    '''
    count = (())
    for pos_animal in ordenar_posicoes(prado["p"]):
        count += (pos_animal,)
    return ordenar_posicoes(count)

def obter_animal(prado, pos):
    '''
          prado x posicao --> animal

          Esta função recebe um prado e devolve o animal do prado que se encontra na posição pos.
    '''
    animal_pos = prado["p"].index(pos)
    return prado["a"][animal_pos]

#-----------------------------Modificadores------------------------------------------------------

def eliminar_animal(prado, pos):
    '''
          prado x posicao --> prado

          Esta função recebe um prado e uma posição e modifica destrutivamente o prado eliminando o animal
          da posição pos deixando-a livre. Devolve o próprio prado.
    '''
    animal_pos = prado["p"].index(pos)
    prado["p"] = prado["p"][:animal_pos] + prado["p"][animal_pos + 1:]
    prado["a"] = prado["a"][:animal_pos] + prado["a"][animal_pos + 1:]
    return prado

def mover_animal(prado, pos1, pos2):
    '''
          prado x posicao x posicao --> prado

          Esta função recebe um prado e duas posições e modifica destrutivamente o prado movimentando
          o animal da posição pos1 para a nova posição pos2, deixando livre a posição onde
          se encontrava. Devolve o próprio prado.
    '''
    animal_pos = prado["p"].index(pos1)
    prado["p"] = prado["p"][:animal_pos] + ((pos2),) + prado["p"][animal_pos + 1:]
    return prado

def inserir_animal(prado, animal, pos):
    '''
          prado x animal x posicao --> prado

          Esta função recebe um prado, uma animal e uma posição e modifica destrutivamente o prado acrescentando
          na posição pos do prado o animal animal passado com argumento. Devolve o próprio prado.
    '''
    prado["a"] = prado["a"] + (animal,)
    prado["p"] = prado["p"] + ((pos),)
    return prado

#-----------------------------Reconhecedores-----------------------------------------------------

def eh_prado(arg):
    '''
          universal --> bool

          Esta função recebe um argumento universal e devolve True caso o seu argumento seja um TAD prado e False
          caso contrário.
    '''
    if not(type(arg) == dict and "d" in arg and "r" in arg and "a" in arg and "p" in arg and eh_posicao(arg["d"]) \
            and type(arg["r"]) == tuple and type(arg["a"]) == tuple and type(arg["p"]) == tuple and len(
        arg["a"]) == len(arg["p"]) \
            and len(arg["a"]) > 0 and len(arg["p"]) > 0):
        return False
    if type(arg) != dict:
        return False
    for rochedo in arg["r"]:
        if type(rochedo) != tuple and not eh_posicao(rochedo) and rochedo[0] != 0 and rochedo[1] != 0 and arg["r"].count(rochedo) != 1:
            return False
    for animal in arg["a"]:
        if type(animal) != tuple and not eh_animal(animal) and arg["a"].count(animal) != 1:
            return False
    for pos_animal in arg["p"]:
        if type(pos_animal) != tuple and not eh_posicao(pos_animal) and arg["p"].count(pos_animal) != 1:
            return False
    return True
def eh_posicao_animal(prado, pos):
    '''
          prado x posicao --> bool

          Esta função recebe um prado e uma posição e devolve True apenas no caso da posição pos do prado
          estar ocupada por um animal.
    '''
    for pos_animal in prado["p"]:
        if posicoes_iguais(pos_animal, pos):
            return True
    return False

def eh_posicao_obstaculo(prado, pos):
    '''
          prado x posicao --> bool

          Esta função recebe um prado e uma posição e devolve True apenas no caso da posição pos do prado
          corresponder a uma montanha ou rochedo.
    '''
    if obter_pos_x(pos) == 0 or obter_pos_y(pos) == 0 or obter_pos_x(pos) == obter_pos_x(prado["d"]) or obter_pos_y(pos) == obter_pos_y(prado["d"]):
        return True
    for pos_rochedo in prado["r"]:
        if pos == pos_rochedo:
            return True
    return False

def eh_posicao_livre(prado, pos):
    '''
          prado x posicao --> bool

          Esta função recebe um prado e uma posição e devolve True apenas no caso da posição pos do prado
          corresponder a um espaço livre (sem animais, nem obstáculos).
    '''
    if not eh_posicao_animal(prado, pos) and not eh_posicao_obstaculo(prado, pos) and obter_pos_x(pos) != obter_tamanho_x(prado) - 1 and obter_pos_y(pos) != obter_tamanho_y(prado) - 1:
        return True
    return False


# -----------------------------Teste----------------------------------------------------------

def prados_iguais(prado1, prado2):
    '''
          prado x prado --> bool

          Esta função recebe dois prados e devolve True apenas se prado1 e prado2 forem prados e forem
          iguais.
    '''
    if prado1 == prado2:
        return True
    return False

#-----------------------------Transformador---------------------------------------------------

def prado_para_str(prado):
    '''
          prado --> str

          Esta função recebe um prado e devolve uma cadeia de caracteres que representa o prado do tipo:
          +----------+
          |....rL...r|
          |...@@.r...|
          |..........|
          +----------+
          em que as letras maíusculas representam predadores, as minúsculas presas, os "-", montanhas, os "+"
          extremidades do prado e os "@" rochedos
    '''
    first_row = []
    rows = []
    rows_final = []

    for x in range(obter_tamanho_x(prado)):
        if x == 0 or x == obter_tamanho_x(prado) - 1:
            first_row += ["+"]
        else:
            first_row += ["-"]

    rows += [first_row]

    for y in range(1, obter_tamanho_y(prado)):
        if y == obter_tamanho_y(prado) - 1:
            rows.append(first_row)
        else:
            rows.append(list(map(lambda x: "|" if x == "+" else ".", first_row)))

    for pos_rochedos in prado["r"]:
        rows[pos_rochedos[1]][pos_rochedos[0]] = "@"


    for pos_animais in prado["p"]:
        rows[pos_animais[1]][pos_animais[0]] = animal_para_char(prado["a"][prado["p"].index(pos_animais)])
    for list_rows in rows:
        rows_final += list_rows + ["\n"]
    return "".join(rows_final[:-1])


# -----------------------------Func_alto_nivel-----------------------------------------------------------

def obter_valor_numerico(prado, pos):
    '''
          prado x posicao --> int

          Esta função recebe um prado e uma posicao e devolve o valor numérico da posição pos correspondente
          à ordem de leitura no prado prado (da esquerda para a direita, de cima para baixo).

    '''
    return obter_pos_y(pos) * obter_tamanho_x(prado) + obter_pos_x(pos)

def obter_movimento(prado,pos):
    '''
          prado x posicao --> posicao

          Esta função recebe um prado e uma posicao e devolve a posição seguinte do animal na posiçao pos dentro
          do prado prado de acordo com as regras de movimento dos animais no prado.

    '''
    i_pred = 0
    i_presa = 0
    list_pos_pred = []
    list_pos_presa = []

    if eh_predador(obter_animal(prado,pos)):
        for pos_adj_pred in (obter_posicoes_adjacentes(pos)):
            if not eh_posicao_obstaculo(prado,pos_adj_pred):
                list_pos_pred += [[pos_adj_pred, i_pred]]
                i_pred += 1
        if obter_pos_x(pos) == obter_tamanho_x(prado) - 2:
            list_pos_pred = list_pos_pred [:1] + list_pos_pred[2:]
            list_pos_pred[1][1] = 1
            list_pos_pred[2][1] = 2
        if obter_pos_y(pos) == obter_tamanho_y(prado) - 2:
            list_pos_pred = list_pos_pred[:2] + list_pos_pred[3:]
            list_pos_pred[2][1] = 2

    if eh_presa(obter_animal(prado,pos)):
        for pos_adj_presa in (obter_posicoes_adjacentes(pos)):
            if eh_posicao_livre(prado,pos_adj_presa):
                list_pos_presa += [[pos_adj_presa, i_presa]]
                i_presa += 1


    for pos_adj_livre in list_pos_pred:
        if eh_posicao_animal(prado, pos_adj_livre[0]) and eh_presa(obter_animal(prado, pos_adj_livre[0])):
            return cria_posicao(pos_adj_livre[0][0], pos_adj_livre[0][1])

    if eh_predador(obter_animal(prado,pos)) and i_pred != 0:
        next_pos_val_pred = obter_valor_numerico(prado,pos) % i_pred
        return cria_posicao(list_pos_pred[next_pos_val_pred][0][0],list_pos_pred[next_pos_val_pred][0][1])

    if eh_presa(obter_animal(prado,pos)) and i_presa != 0:
        next_pos_val_presa = obter_valor_numerico(prado,pos) % i_presa
        return cria_posicao(list_pos_presa[next_pos_val_presa][0][0], list_pos_presa[next_pos_val_presa][0][1])
    return pos

# ----------------------------------------------------------Func_adicionais---------------------------------------------

def geracao(prado):
    '''
          prado --> prado

          Esta função é a função auxiliar que modifica o prado prado fornecido como argumento de
          acordo com a evolução correspondente a uma geração completa, e devolve o próprio
          prado. Isto é, seguindo a ordem de leitura do prado, cada animal (vivo) realiza o seu
          turno de ação de acordo com as regras do prado.
    '''
    pos_animais = obter_posicao_animais(prado)
    for pos in pos_animais:
        if eh_predador(obter_animal(prado, pos)) and eh_posicao_animal(prado,pos):
            if eh_posicao_animal(prado,pos):
                aumenta_idade(obter_animal(prado, pos))
                aumenta_fome(obter_animal(prado, pos))
            if eh_posicao_animal(prado,obter_movimento(prado,pos)):
                if eh_presa(obter_animal(prado, obter_movimento(prado, pos))):
                    eliminar_animal(prado, obter_movimento(prado, pos))
                    reset_fome(obter_animal(prado, pos))
            if eh_animal_fertil(obter_animal(prado,pos)) and eh_posicao_livre(prado, obter_movimento(prado, pos)):
                inserir_animal(prado, reproduz_animal(obter_animal(prado, pos)), pos)
                reset_idade(obter_animal(prado, pos))
            if eh_animal_faminto(obter_animal(prado, pos)):
                eliminar_animal(prado,pos)
            if eh_posicao_animal(prado,pos):
                mover_animal(prado, pos, obter_movimento(prado,pos))

        if eh_posicao_animal(prado,pos) and eh_presa(obter_animal(prado, pos)):
            aumenta_idade(obter_animal(prado, pos))
            if eh_animal_fertil(obter_animal(prado,pos)) and eh_posicao_livre(prado, obter_movimento(prado, pos)):
                inserir_animal(prado, reproduz_animal(obter_animal(prado, pos)), pos)
                reset_idade(obter_animal(prado, pos))
            if eh_posicao_animal(prado, pos):
                mover_animal(prado, pos, obter_movimento(prado, pos))
    return prado


def simula_ecossistema(f, g, v):
    '''
          str x int x bool --> tuplo

          Esta função é a função principal que permite simular o ecossistema de um prado. A função recebe uma cadeia de caracteres f, um valor inteiro g e um valor booleano
          v e devolve o tuplo de dois elementos correspondentes ao número de predadores e
          presas no prado no fim da simulação. A cadeia de caracteres f passada por argumento
          corresponde ao nome do ficheiro de configuração da simulação. O valor inteiro g corresponde
          ao número de gerações a simular. O argumento booleano v ativa o modo verboso
          (True) ou o modo quiet (False). No modo quiet mostra-se pela saída standard o prado,
          o número de animais e o número de geração no início da simulação e após a última
          geração. No modo verboso, após cada geração, mostra-se também o prado, o número de
          animais e o número de geração, apenas se o número de animais predadores ou presas se
          tiver alterado.
    '''
    tup_animais = ()
    tup_pos_animais = ()
    with open(f, "r") as file:
        linhas = file.readlines()
        linhas = list(map(lambda x: eval(x[:-1]), linhas))

    for animal in linhas[2:]: #Informação sobre os animais
        tup_animais += (cria_animal(animal[0],animal[1],animal[2]),)

    for pos_animal in linhas[2:]: #Informação sobre a posição dos animais
        tup_pos_animais += (pos_animal[3],)

    prado = cria_prado(linhas[0], linhas[1], tup_animais, tup_pos_animais)

    dim_prado_livre = ((obter_tamanho_x(prado) - 2) * (obter_tamanho_y(prado) - 2)) - len(linhas[1]) #Número de casas do prado ainda por ocupar

    for i in range(g + 1):
        if (obter_numero_presas(prado) == dim_prado_livre or obter_numero_predadores(prado) == dim_prado_livre) and not v:
            print("Predadores: " + str(obter_numero_predadores(prado)) + " vs Presas: " + str(
                obter_numero_presas(prado)) + " (Gen. " + str(g) + ")")
            print(prado_para_str(prado))
            break
        if obter_numero_presas(prado) != dim_prado_livre and obter_numero_predadores(prado) != dim_prado_livre:
            if i == 0:
                print("Predadores: " + str(obter_numero_predadores(prado)) + " vs Presas: " + str(
                    obter_numero_presas(prado)) + " (Gen. " + str(i) + ")")
                print(prado_para_str(prado))
            else:
                prado = geracao(prado)
            if v:
                print("Predadores: " + str(obter_numero_predadores(prado)) + " vs Presas: " + str(
                    obter_numero_presas(prado)) + " (Gen. " + str(i) + ")")
                print(prado_para_str(prado))
            elif i == g:
                print("Predadores: " + str(obter_numero_predadores(prado)) + " vs Presas: " + str(
                    obter_numero_presas(prado)) + " (Gen. " + str(i) + ")")
                print(prado_para_str(prado))
    return (obter_numero_predadores(prado), obter_numero_presas(prado))

def cargarPersonaje (id:str) -> dict:
    archivo = open('lib_personajes.csv')

    pnj = {
        'id':'0',
        'nombre':'ERROR NO EXISTE',
    }

    llaves = archivo.readline().replace('\n','').split(';')

    while (True):
        personaje = archivo.readline().replace('\n','').split(';')
        if (personaje == ['']):
            break
        
        if (personaje[0] == str(id)):
            for i in range(len(llaves)):
                pnj.update(
                    {
                        llaves[i] : personaje[i]
                    }
                )
            pnj['vida_actual'] = pnj['vida']        

    archivo.close()

    return pnj

def guardarPersonaje (pnj:dict) -> None:
    nombre_archivo = pnj['nombre']+'_datos.dbz'
    archivo = open(nombre_archivo,'w')

    for valor in pnj.values():
        archivo.write(str(valor) + '\n')

    archivo.close() 


def imprimirPersonaje (pnj:dict) -> None:
    if (pnj['nombre'] == 'ERROR NO EXISTE'):
        print('PERSONAJE NO EXISTE!!')
        return
    
    print('Nombre: ',pnj['nombre'])
    print('VIDA: ',pnj['vida_actual'], '/',pnj['vida'])
    imprimirBarraVida(pnj)
    print('ATK ⚔ | DEF 🛡 | VEL 👟')
    print(pnj['atk'], ' | ' ,pnj['def'],' | ',pnj['vel'])

def imprimirBarraVida (pnj:dict) -> None:
    vida_total = int(pnj['vida'])
    vida_actual = int(pnj['vida_actual'])
    dif_vida = vida_total - vida_actual
    print(
        '♥ '*int(vida_actual/2),
        '✖ '*int(dif_vida/2),
        sep=''
        
    )

def restarVida (pnj:dict, dmg:int) -> None:
    pnj['vida_actual'] = str(
        int(pnj['vida_actual']) - dmg
    )

def imprimirNombre (pnj:dict) -> None:
    print(pnj['nombre'])


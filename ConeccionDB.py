import requests


def insertar(cedula, pri_nombre, seg_nombre, pri_apellido, seg_apellido):
    res = requests.post('http://localhost:5000/api/insertar_data/',
                        json={"cedula": cedula, "pri_nombre": pri_nombre,
                              "seg_nombre": seg_nombre, "pri_apellido": pri_apellido,
                              "seg_apellido": seg_apellido})
    if res.ok:
        print(res.json())
    else:
        print('Cedula no existente')


def consultarlogin(cedula, password):
    try:
        res = requests.post('http://localhost:5000/api/login/',
                            json={"cedula": cedula, "password": password})
        global var
        if res.ok:
            var = True
            print(res.json())
        else:
            var = False
            print('Cedula no existente')
    except Exception as e:
        print("Error en base de datos")


def conect():
    return var


def consultarperfil(cedula):
    print('Consultar Data Request')
    print('<--------------------------->')
    res = requests.post('http://localhost:5000/api/consultar_perfil/', json={"cedula": cedula})
    global perfil
    if res.ok:
        perfil = res.json()
    else:
        print('Cedula no existente')
        print('--------------------------------------')


def perfil():
    return perfil

# if __name__ == '__main__':
#    insertar("8-359-545", "popo", "pepe", "manuel", "analinda")

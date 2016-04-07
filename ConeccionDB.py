import requests


def insertar(cedula, pri_nombre, seg_nombre, pri_apellido, seg_apellido):
    res = requests.post('http://192.168.173.1:5000/api/insertar_data/',
                        json={"cedula": cedula, "pri_nombre": pri_nombre,
                              "seg_nombre": seg_nombre, "pri_apellido": pri_apellido,
                              "seg_apellido": seg_apellido})
    if res.ok:
        print(res.json())
    else:
        print('Cedula no existente')


def consultarlogin(cedula, password):
    res = requests.post('http://192.168.173.1:5000/api/login/',
                        json={"cedula": cedula, "password": password})
    if res.ok:
       print(res.json())
    else:
        print('Cedula no existente')

# if __name__ == '__main__':
#    insertar("8-359-545", "popo", "pepe", "manuel", "analinda")

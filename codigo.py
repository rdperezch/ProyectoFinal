
res = requests.post('http://localhost:5000/api/insertar_data/', json={"cedula":'8-850-1421',"pri_nombre":'Anyelt',"seg_nombre":'Cristel',"pri_apellido":'Sanchez',"seg_apellido":'Gracia' })
if res.ok:
   print (res.json())
else:
	print ('Cedula no existente')
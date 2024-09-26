import json

notas = {
            'maria':{
                        'mat':9,
                        'qui':8,
                        'inf':5
                    },
            'joao':{
                        'mat':9,
                        'qui':6,
                        'inf':10
                    },
            'julia':{
                        'mat':7,
                        'qui':10,
                        'inf':9
                    }
        }


json_object = json.dumps(notas, indent = 4) 
print(json_object)
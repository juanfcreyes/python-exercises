def json_encode(data):
    if isinstance(data, bool):
        if data:
            return "true"
        else:
            return "false"
    elif isinstance(data, (int, float)):
        return str(data)
    elif isinstance(data, str):
        print('str', data)
        return '"' + escape_string(data) + '"'
    elif isinstance(data, list):
        return "[" + ", ".join(json_encode(d) for d in data) + "]"
    elif isinstance(data, dict):
        result = []
        for v, k in data.items():
             result.append(json_encode(v) + " : " + json_encode(k)) 
        return "{" + ", ".join(result) + " }"
    else:
        raise TypeError("%s is not JSON serializable" % repr(data))

def escape_string(s):
    """Escapes double-quote, tab and new line characters in a string."""
    s = s.replace('"', '\\"')
    s = s.replace("'", "\\'")
    s = s.replace("\t", "\\t")
    s = s.replace("\n", "\\n")
    return s


data = {
   'firts name' : 'Juan',
   'last name' : 'Castillo',
   'country' : {
       'id' : '456fd4ds4897f',
       'name' : 'Ecuador'
    },
   'single' : True,
   'participants': [
        {
            'name': 'Participant 1',
            'email': 'email1@example.com'
        },
        {
            'name': 'Participant 2',
            'email': 'email2@example.com'
        }
    ]
   }

   
print(json_encode(data))

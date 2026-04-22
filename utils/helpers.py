import json


def json_list_load(json_file):
    try:
        return json.loads(json_file)
    except:
        start = json_file.find("[")
        end = json_file.rfind("]") + 1

        return json.loads(json_file[start:end])




def json_dict_load(json_file):
    try:
        return json.loads(json_file)
    except:
        start = json_file.find("{")
        end = json_file.rfind("}") + 1

        return json.loads(json_file[start:end])



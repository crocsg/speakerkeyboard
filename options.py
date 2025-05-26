import json
from pathlib import Path

app_options = {
    "device": "",
    "speed": 70,
    "volume": 200,
    "voice":"mb-fr4",
    "sync":0,
    "messages":{
        "f1":"Papa",
        "f2":"Maman",
        "f3":"La bonne",
        "f4":"et moi"

    }
}

def get_messages ():
    return app_options["messages"]

def get_parameter_fname ():
    paramfname = "kspeaker.json"
    return paramfname

    if detected_os == KnownOS.Linux:
        home = Path.home ()
        dir = Path.joinpath(home, ".desktopbraillerap/")
        print (home, dir)
        if not os.path.exists(dir):
            os.makedirs(dir)
        fpath = Path.joinpath(dir, paramfname)
        print (fpath)
        return fpath

    else:
        return paramfname

def load_options():
    try:
        fpath = get_parameter_fname()

        with open(fpath, "r", encoding="utf-8") as inf:
            data = json.load(inf)
            for k, v in data.items():
                if k in app_options:
                    app_options[k] = v

    except Exception as e:
        create_options ()
        print(e)
    print(app_options)

def create_options():
    """Save parameters in local json file"""
    try:
        #print("data", app_options)
        #print("json", json.dumps(app_options))
        fpath = get_parameter_fname()
        with open(fpath, "w", encoding="utf-8") as of:
            json.dump(app_options, of)

    except Exception as e:
        print(e)

def get_voice ():
    return app_options["voice"]

def get_volume ():
    return app_options["volume"]

def get_speed ():
    return app_options["speed"]

def get_sync ():
    return app_options["sync"]
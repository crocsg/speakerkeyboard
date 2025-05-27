# speakerkeyboard

this project AIM to build vocal synthesis system on Raspberry PI for an interactive public transport map

the speech synthesis use espeack-ng/mbrola
we use [shapelesskeyvoard as usb keyboard for user input](https://github.com/crocsg/shapeless_rp2040_40keys)

# Prerequesite

You must have a working audio system on your Raspberry Pi (the standard audio output is fine for speech synthesis)
You must have epseack-ng and mbrola installed 
```
$ sudo apt-get install espeak-ng
$ espeak-ng "Hello Word"
$ espeak-ng --voices
$ espeak-ng -v fr-fr "Bonjour Monde"
```

```
$ wget https://raspberry-pi.fr/download/espeak/mbrola3.0.1h_armhf.deb -O mbrola.deb
$ sudo dpkg -i mbrola.deb
$ sudo apt install mbrola-fr4 -y
$ espeak-ng -v mb-fr4 "Hello world"
```

# Install on Raspberry PI

You must be in root user to use *keyboard* python module

create a virtual env
```python -m venv venv```

activate the virtual env
```source ./venv/bin/activate```

install python dependencies
```pip install -r requirement.txt```

# Configuration
the configuration is available in *kspeaker.json*.
```
{
    "device": "",
    "speed": 70,
    "volume": 30,
    "voice": "mb-fr4",
    "sync":0,
    "messages": {
        "59": "Papa",
        "60": "Maman",
        "61": "La bonne",
        "62": "et moi"
    }
}
```
*device*, *speed*, *volume* and *voice* are speack-ng TTS parameters.
the association of keyboard keycode and message is done in *messages* part. You can use the software to display keyboard keycode.

# Run

when virtual env activated simply use :
```
python kspeaker.py
```


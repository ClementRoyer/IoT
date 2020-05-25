from random import randint

def get_rand(): 
    return randint(0, 10)

def enroll_finger():
    print("Place finger on sensor...", end="", flush=True)
    print("Image taken")
    print("Templating...", end="", flush=True)
    print("Templated")
    print("Remove finger")
    print("Creating model...", end="", flush=True)
    print("Created")
    print("Storing model ...", end="", flush=True)
    print("Stored")
    return get_rand()

def get_fingerprint():
    print("Waiting for image...")
    print("Templating...")
    return get_rand()

def delete():
    return True
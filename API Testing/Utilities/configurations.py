import configparser

def getconfig():
    config = configparser.ConfigParser()
    config.read(r"C:\Users\Milky\PycharmProjects\pythonProject\API Testing\Utilities\properties.ini")
    return config

def getpassword():
    return "Salt_github7780"
import eel
import pathlib
import database

#database.test()

path = pathlib.Path().resolve()
eel.init(f"{path}\web")
eel.start("index.html", mode="chrome", size=(500, 800))

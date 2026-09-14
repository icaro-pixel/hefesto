from rocketpy import *
from dic_hefesto import setting, aletas, coifa, rail_button, refeedRec, unrefeedRec
from dic_motor import motorD
from ambiente import envLasc, envIrec, caminho_data

foguete = Rocket(**setting)

motor = SolidMotor(**motorD)

foguete.add_nose(**coifa)
foguete.add_free_form_fins(**aletas)
foguete.set_rail_buttons(**rail_button)
foguete.add_parachute(**unrefeedRec)
foguete.add_parachute(**refeedRec)

foguete.add_motor(motor, position=2.78)

vooLasc = Flight(
    rocket= foguete,
    environment= envLasc,
    inclination=80,
    heading=90,
    rail_length=6
)

vooIrec = Flight(
    rocket= foguete,
    environment= envIrec,
    inclination=71,
    heading=90,
    rail_length=6
)

############################################################

vooIrec.info()

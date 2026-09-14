from pyprojroot import here

caminho_raiz = here()


caminho_data = caminho_raiz / "data"


setting = {
    # Foguete Base

    "radius": 0.079, # m - open rocket
    "mass": 21.644, # kg abaixo - open rocket
    "coordinate_system_orientation": "nose_to_tail",

    # e preciso checar se os eixos estao invertidos, o inertia devolve em outra ordem
    "inertia": (11.784, 11.784, 0.099), # Calculado

    "center_of_mass_without_motor": 1.35, # m - OpenRocket without motor ##

    # Arrasto

    "power_off_drag": str(caminho_data  / "power_off.csv") , # (RasAero II)
    "power_on_drag": str(caminho_data  / "power_on.csv"), #

}

aletas = {
    # Aletas (Fins)

    "n": 4,
    "position": 2.57,  # m - openrocket

    # COORDENADAS EXTRAÍDAS # AUTO
    "shape_points": [
        (0.0, 0.0),
        (0.07, 0.12),
        (0.21, 0.14),
        (0.18, 0.0)
    ]
}

coifa = {
   # Coifa (Nosecone)

    "length": 0.45,  # m - openrocket
    "position": 0,  # m
    "kind": "lvhaack"  ## checar
}

rail_button = {
    # Rail Buttons (Guias)

    "upper_button_position": 1.39,  # m
    "lower_button_position": 2.30,  # m
    "angular_position": 45.0,  # graus
    "radius": 0.02,  # m
}

refeedRec = {

    "name": "reefed",
    "cd_s": 0.85,  #
    "radius": 1.2 / 2,  # m
    "trigger": "apogee",  # m
    "lag": 1  # s

}

unrefeedRec = {

    "name": "unreefed",
    "cd_s": 1.5,  #
    "radius": 3.8000000000000003 / 2,  # openrocket
    "trigger": 450,  # openrocket
    "lag": 1  # openrocket

}
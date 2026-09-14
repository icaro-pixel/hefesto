from pyprojroot import here

caminho_raiz = here()
caminho_data = caminho_raiz / "data"

motorD = {

    "thrust_source": str(caminho_data / "motor_novo.eng"),

    "dry_mass": 10,  # 21 - 11 (mA - mP)
    "dry_inertia": (1.47, 1.47, 0.0125),  #
    "center_of_dry_mass_position": 0.499,  # m

    "grain_number": 7,  # OpenMotor

    "grain_outer_radius": 0.05,  # OpenMotor
    "grain_initial_inner_radius": 0.02343,  # media ponderada entre os raios obtidos anteriormente
    "grain_initial_height": 0.15,  # OpenMotor "Length"
    "grain_separation": 0.01,  #

    "grain_density": 1812.44,  #
    "grains_center_of_mass_position": 0.67,  #

    "nozzle_position": 0.016,  #
    "nozzle_radius": 0.039,  #

    "throat_radius": 0.0173,  # OpenMotor

    "burn_time": (0, 3.9),

    "coordinate_system_orientation": "nozzle_to_combustion_chamber",

}
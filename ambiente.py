from rocketpy import Environment

from pyprojroot import here

caminho_raiz = here()
caminho_data = caminho_raiz / "data"

envLasc = Environment(
    date = (2025, 11, 6, 15),
    latitude= -21.90795, longitude= -48.96156,
    elevation= 495
)

envLasc.set_atmospheric_model(
    type="Reanalysis",
    file=str(caminho_data / "iacanga-25-24_nov_6-7_11a15hLASC" / "data_stream-oper_stepType-instant.nc"),
    dictionary={
        "time": "valid_time",
        "latitude": "latitude",
        "longitude": "longitude",
        "level": "pressure_level",
        "temperature": "t",
        "surface_geopotential_height": None,
        "geopotential_height": None,
        "geopotential": "z",
        "u_wind": "u",
        "v_wind": "v",
    }
)

# January and June, 15 to 16, 10 to 16

envIrec = Environment(
    date = (2026, 6, 15, 12),
    latitude= 32.94019, longitude= -106.92056,
    elevation= 1401
)

envIrec.set_atmospheric_model(
    type="Reanalysis",
    file = str(caminho_data / "irec" / "data_stream-oper_stepType-instant.nc"),
    dictionary={
        "time": "valid_time",
        "latitude": "latitude",
        "longitude": "longitude",
        "level": "pressure_level",
        "temperature": "t",
        "surface_geopotential_height": None,
        "geopotential_height": None,
        "geopotential": "z",
        "u_wind": "u",
        "v_wind": "v",
    }
)



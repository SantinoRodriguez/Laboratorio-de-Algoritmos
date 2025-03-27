Ciudades = {
    "Buenos Aires": {
        "País": "Argentina",
        "Población": "15 millones",
        "Dato": "Es conocida como la 'Reina del Plata' por su ubicación en el Río de la Plata."
    },
    "París": {
        "País": "Francia",
        "Población": "2.2 millones",
        "Dato": "Es famosa por la Torre Eiffel, que se construyó para la Exposición Universal de 1889."
    },
    "Tokio": {
        "País": "Japón",
        "Población": "37 millones",
        "Dato": "Es la ciudad más poblada del mundo y un centro global de tecnología y cultura."
    }
}
for Ciudad, Info in Ciudades.items():
    print(f"Ciudad: {Ciudad}\n País: {Info['País']}\n Población: {Info['Población']}\n Dato interesante: {Info['Dato']}")
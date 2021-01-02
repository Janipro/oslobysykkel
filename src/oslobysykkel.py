# -------------------------------------------------
# Create a small application that utilizes this api
# to show the stations and the amount of available
# bikes and free spots a station currently has.
# -------------------------------------------------


import requests
import PySimpleGUI as sg

if not requests:
    print("Module requests has not been imported correctly!")
if not sg:
    print("Module PySimpleGUI has not been imported correctly!")


def get_data():
    info = {
    "Client-Identifier": "privat_bruk"
}
    response_stations = requests.get("https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json", params=info)
    response_availability = requests.get("https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json", params=info)
    stations_data = response_stations.json()["data"]["stations"]
    availability_data = response_availability.json()["data"]["stations"]
    data = {}

    for i in range(len(stations_data)):
        """Using range because len(stations_data) == len(availability_data)"""
        station = stations_data[i]["name"]
        position = (stations_data[i]["lat"], stations_data[i]["lon"])
        available_bikes = availability_data[i]["num_bikes_available"]
        free_spots = availability_data[i]["num_docks_available"]
        data[station] = (available_bikes, free_spots, position)

    return data


current_data = get_data()
stations = list(current_data.keys())
stations.sort()

stations_list_column = [
    [
        sg.Text("Filter stations"),
        sg.InputText(size=(28, 1), enable_events=True, key="-SEARCH-"),
    ],
    [
        sg.Listbox(values=stations, enable_events=True, size=(40, 40), key="-STATIONS-"),
    ],
]

stats_column = [
    [
        sg.Text("Available bikes: "),
        sg.Text("  ", size=(20, 1), key="-BIKES-"),
        sg.Text("Free spots: "),
        sg.Text("  ", size=(20, 1), key="-SPOTS-"),
    ],
]

layout = [
    [
        sg.Column(stations_list_column),
        sg.Column(stats_column),
    ],
]


def main():
    window = sg.Window("Oslo Bysykkel", layout, size=(800, 600))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            raise SystemExit

        if event == "-SEARCH-":
            search = values["-SEARCH-"]
            temp = []
            for station in stations:
                if search in station or search in station.lower():
                    temp.append(station)
            window["-STATIONS-"].update(temp)

        if event == "-STATIONS-":
            name = values["-STATIONS-"][0]
            number_of_bikes = current_data.get(name)[0]
            number_of_spots = current_data.get(name)[1]
            window["-BIKES-"].update(number_of_bikes)
            window["-SPOTS-"].update(number_of_spots)


main()


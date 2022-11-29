# This file contains all the methods used on Jet Engine Propulsion

# Link Flow Stations
def LinkPorts(Fl_O, Fl_I):
    attributes = Fl_O.show()
    match = ['T', 'Tt', 'P', 'Pt', 'W']

    for key in attributes:
        if key in match:
            Fl_O.key = Fl_I.key


from pyscript import document, display
import numpy as np
import matplotlib.pyplot as plt

days = []
absences = []

def displaying(e):
    day = document.getElementById('day').value
    absence = int(document.getElementById('absence').value)

    days.append(day)
    absences.append(absence)

    converted_absences = np.array(absences)

    plt.clf()

    plt.plot(days, converted_absences, marker='o')
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day")
    plt.ylabel("Number of Absences")
    plt.grid()

    display(plt, target="graph", append=False)

def reset_data(e):
    global days, absences
    days = []
    absences = []

    document.getElementById("graph").innerHTML = "Graph reset"
from pyscript import document
from js import document as js_document

class Classmate:
    def __init__(self, name, section, job):
        self.name = name
        self.section = section
        self.job = job

    def introduce(self):
        return f"Name: {self.name}<br>Section: {self.section}<br>Desired Job: {self.job}<br><br>"


classmates = [

]


def show_list(event=None):
    output = ""
    for c in classmates:
        output += c.introduce()

    document.getElementById("classmate-list").innerHTML = output


def add_classmate(event=None):
    name = document.getElementById("name").value.strip()
    section = document.getElementById("section").value.strip()
    job = document.getElementById("desiredJob").value.strip()

    if not name or not section or not job:
        document.getElementById("signed").innerText = "Please fill EVERYTHING!"
        return

    if any(c.name == name for c in classmates):
        document.getElementById("signed").innerText = "You're listed already bruh!"
        return

    classmates.append(Classmate(name, section, job))

    document.getElementById("signed").innerText = f"{name} succefully added you!"

    document.getElementById("name").value = ""
    document.getElementById("section").value = ""
    document.getElementById("desiredJob").value = ""


def setup(event=None):
    document.getElementById("addBtn").addEventListener("click", add_classmate)
    document.getElementById("showBtn").addEventListener("click", show_list)


js_document.addEventListener("DOMContentLoaded", setup)

from js import window

# expose functions to JS
window.addClassmate = add_classmate
window.showList = show_list
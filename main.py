from pyscript import document, display
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)
import matplotlib
matplotlib.use('svg')
import matplotlib.pyplot as plt
import io, base64

plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

DAYS_ORDER = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
data = {}

def update_status(msg, color="#28a745"):
    el = document.getElementById("status-msg")
    el.innerText = msg
    el.style.color = color

def update_dots():
    for day in DAYS_ORDER:
        dot = document.getElementById(f"dot-{day}")
        if day in data:
            dot.classList.add("filled")
        else:
            dot.classList.remove("filled")

def displaying(e):
    day = document.getElementById("day-select").value
    absence_raw = document.getElementById("absence-input").value

    if absence_raw.strip() == "":
        update_status("⚠ Please enter a number of absences.", "#e0245e")
        return

    absence = int(absence_raw)
    data[day] = absence
    update_dots()
    update_status(f"✓ {day}: {absence} absence(s) recorded.")

    ordered_days = [d for d in DAYS_ORDER if d in data]
    ordered_absences = np.array([data[d] for d in ordered_days])

    fig, ax = plt.subplots(figsize=(6, 3.6))
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#f9f9f9')

    ax.plot(ordered_days, ordered_absences, marker='o', color='#1a73e8',
            linewidth=2.5, markersize=8, markerfacecolor='#e0245e',
            markeredgecolor='white', markeredgewidth=1.5)

    for i, (d, v) in enumerate(zip(ordered_days, ordered_absences)):
        ax.annotate(str(v), (d, v), textcoords="offset points",
                    xytext=(0, 10), ha='center', fontsize=9,
                    fontweight='bold', color='#333')

    ax.set_title("Weekly Attendance (Absences)", fontsize=12, fontweight='bold', pad=12, color='#222')
    ax.set_xlabel("Day", fontsize=10, color='#555')
    ax.set_ylabel("Number of Absences", fontsize=10, color='#555')
    ax.set_ylim(bottom=0)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=130, bbox_inches='tight')
    buf.seek(0)
    img_b64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()

    container = document.getElementById("plot-output")
    container.innerHTML = f'<img src="data:image/png;base64,{img_b64}" alt="Attendance Chart">'

def reset_data(e):
    global data
    data = {}
    update_dots()
    update_status("Data cleared.", "#888")
    container = document.getElementById("plot-output")
    container.innerHTML = '''
      <div class="placeholder-msg">
        <i class="fa-regular fa-chart-bar"></i>
        Submit a day to see the graph appear here.
      </div>
    '''

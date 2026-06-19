import sys
import datetime
import psutil
import random

from gui.reactor import ArcReactor

from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QVBoxLayout, QHBoxLayout,
    QGraphicsDropShadowEffect,
    QTextEdit
)   

from PyQt6.QtGui import QPainter, QColor, QFont
from PyQt6.QtCore import pyqtSignal, QTimer, Qt

from modules.system_monitor import (
    get_cpu, get_ram, get_battery, get_pc_name
)

dashboard_instance = None


# =========================
# 🎤 WAVEFORM
# =========================
class WaveformWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.bars = [5] * 20
        self.active = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(100)

    def set_active(self, state: bool):
        self.active = state

    def animate(self):
        if self.active:
            self.bars = [random.randint(5, 45) for _ in self.bars]
        else:
            self.bars = [5] * 20
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        width = self.width()
        bar_width = width // len(self.bars)

        for i, h in enumerate(self.bars):
            painter.setBrush(QColor(0, 255, 255))
            painter.drawRect(i * bar_width, self.height() - h, bar_width - 2, h)


# =========================
# 🧠 DASHBOARD UI (IRON MAN STYLE)
# =========================
class Dashboard(QWidget):

    update_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        # 🌌 FULLSCREEN HUD
        self.setWindowTitle("JARVIS IRON MAN HUD")
        self.showFullScreen()

        self.setStyleSheet("""
            background-color: #05070d;
            color: #00f5ff;
        """)

        main_layout = QVBoxLayout()

        # =========================
        # 🟦 TITLE
        # =========================
        self.title = QLabel("J.A.R.V.I.S")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setFont(QFont("Arial", 48))

        glow = QGraphicsDropShadowEffect()
        glow.setBlurRadius(60)
        glow.setColor(QColor(0, 255, 255))
        self.title.setGraphicsEffect(glow)

        main_layout.addWidget(self.title)

        # =========================
        # ⚙ CENTER PANEL (REACTOR + STATS)
        # =========================
        self.reactor = ArcReactor()

        center = QHBoxLayout()

        # LEFT PANEL
        left = QVBoxLayout()
        self.cpu_label = QLabel("CPU: 0%")
        self.ram_label = QLabel("RAM: 0%")
        left.addWidget(self.cpu_label)
        left.addWidget(self.ram_label)

        center.addLayout(left)
        center.addWidget(self.reactor)

        # RIGHT PANEL
        right = QVBoxLayout()
        self.battery_label = QLabel("Battery: N/A")
        self.system_label = QLabel(get_pc_name())
        right.addWidget(self.battery_label)
        right.addWidget(self.system_label)

        center.addLayout(right)

        main_layout.addLayout(center)

        # =========================
        # 🎤 WAVEFORM
        # =========================
        self.waveform = WaveformWidget()
        self.waveform.setFixedHeight(70)
        main_layout.addWidget(self.waveform)

        # =========================
        # 🌐 NETWORK
        # =========================
        self.network_label = QLabel("Network: Scanning...")
        self.network_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.network_label)

        # =========================
        # 💬 OUTPUT PANEL (MAIN FIX)
        # =========================
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)

        self.output_box.setStyleSheet("""
            background-color: rgba(0,0,0,0.7);
            color: #00f5ff;
            font-size: 14px;
            border: 1px solid #00f5ff;
            padding: 10px;
        """)

        self.output_box.setFixedHeight(220)

        main_layout.addWidget(self.output_box)

        # =========================
        # 📡 STATUS
        # =========================
        self.status_label = QLabel("SYSTEM ONLINE")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mode_label = QLabel("MODE: IDLE")
        self.mode_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(self.status_label)
        main_layout.addWidget(self.mode_label)

        # =========================
        # 🕒 CLOCK
        # =========================
        self.clock_label = QLabel("")
        self.clock_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.clock_label)

        self.setLayout(main_layout)

        # SIGNAL CONNECT
        self.update_signal.connect(self._set_status)

        # TIMER
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh_stats)
        self.timer.start(1000)

    # =========================
    # 💀 CINEMATIC SHUTDOWN
    # =========================
    def cinematic_shutdown(self):

        self.setStyleSheet("background-color: black; color: red;")

        self.status_label.setText("⚠ SYSTEM SHUTTING DOWN")
        self.append_output("SYSTEM: SHUTDOWN INITIATED")

        self.waveform.set_active(False)
        self.reactor.set_mode("idle")

        def phase2():
            self.status_label.setText("DISENGAGING CORE...")
            self.append_output("CORE: DISCONNECTING")

        def phase3():
            self.status_label.setText("POWER OFF SEQUENCE...")
            self.setWindowOpacity(0.3)

        def final():
            try:
                self.reactor.timer.stop()
                self.waveform.timer.stop()
            except:
                pass
            self.close()

        QTimer.singleShot(1200, phase2)
        QTimer.singleShot(3000, phase3)
        QTimer.singleShot(5000, final)

    # =========================
    # 🎯 STATUS HANDLER (FINAL FIX)
    # =========================
    def _set_status(self, text):

        if not text:
            return

        t = str(text).lower().strip()

        # 💀 EXIT FIX
        if any(x in t for x in ["quit", "exit", "shutdown", "goodbye"]):
            self.append_output("USER: EXIT COMMAND RECEIVED")
            self.cinematic_shutdown()
            return

        if "listening" in t:
            self.waveform.set_active(True)
            self.reactor.set_mode("listening")
            self.status_label.setText("LISTENING...")
            return

        if "processing" in t:
            self.waveform.set_active(False)
            self.reactor.set_mode("processing")
            self.status_label.setText("PROCESSING...")
            return

        if "idle" in t:
            self.waveform.set_active(False)
            self.reactor.set_mode("idle")
            self.status_label.setText("IDLE")
            return

        # 💬 OUTPUT BOX MAIN DISPLAY
        self.append_output(text)
        self.status_label.setText("ACTIVE")

    # =========================
    # 💬 OUTPUT APPEND FUNCTION
    # =========================
    def append_output(self, text):
        self.output_box.append(f"• {text}")

        # auto scroll fix
        self.output_box.verticalScrollBar().setValue(
            self.output_box.verticalScrollBar().maximum()
        )

    # =========================
    # 📊 SYSTEM STATS
    # =========================
    def refresh_stats(self):

        self.cpu_label.setText(f"CPU: {get_cpu()}%")
        self.ram_label.setText(f"RAM: {get_ram()}%")

        battery, charging = get_battery()
        if battery:
            state = "Charging" if charging else "Battery"
            self.battery_label.setText(f"{battery}% ({state})")

        self.clock_label.setText(datetime.datetime.now().strftime("%H:%M:%S"))

        net = psutil.net_io_counters()
        self.network_label.setText(
            f"↑ {net.bytes_sent//1024//1024}MB ↓ {net.bytes_recv//1024//1024}MB"
        )


# =========================
# 🚀 RUN APP
# =========================
def run_gui():
    global dashboard_instance

    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    dashboard_instance = Dashboard()
    dashboard_instance.show()

    sys.exit(app.exec())


def set_status(text):
    global dashboard_instance
    if dashboard_instance:
        dashboard_instance.update_signal.emit(text)


if __name__ == "__main__":
    run_gui()
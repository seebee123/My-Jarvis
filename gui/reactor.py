from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush
from PyQt6.QtCore import QTimer, Qt
import math


class ArcReactor(QWidget):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(300, 300)

        self.angle = 0
        self.pulse_radius = 0
        self.energy_phase = 0

        # 🔥 MODE SYSTEM
        self.speed = 2
        self.glow_intensity = 150

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)

    def set_mode(self, mode):
        if mode == "idle":
            self.speed = 1
            self.glow_intensity = 80

        elif mode == "listening":
            self.speed = 2
            self.glow_intensity = 150

        elif mode == "processing":
            self.speed = 5
            self.glow_intensity = 255

    def animate(self):
        self.angle = (self.angle + self.speed) % 360
        self.pulse_radius = (self.pulse_radius + self.speed) % 120
        self.energy_phase += 0.2 * self.speed
        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        center_x = self.width() / 2
        center_y = self.height() / 2
        painter.translate(center_x, center_y)

        # 🔵 OUTER GLOW
        painter.setPen(QPen(QColor(0, 255, 255, 40), 20))
        painter.drawEllipse(-120, -120, 240, 240)

        # ⚡ PULSE
        alpha = self.glow_intensity - int(self.pulse_radius)
        painter.setPen(QPen(QColor(0, 255, 255, alpha), 4))
        painter.drawEllipse(
            -self.pulse_radius,
            -self.pulse_radius,
            self.pulse_radius * 2,
            self.pulse_radius * 2
        )

        # 🔄 RING
        painter.save()
        painter.rotate(self.angle)

        painter.setPen(QPen(QColor(0, 255, 255), 4))
        painter.drawEllipse(-90, -90, 180, 180)

        for i in range(8):
            painter.rotate(45)
            painter.drawLine(0, -90, 0, -70)

        painter.restore()

        # ⚡ ENERGY LINES
        painter.save()
        for i in range(6):
            angle = i * 60 + self.angle
            x = math.cos(math.radians(angle)) * 50
            y = math.sin(math.radians(angle)) * 50

            painter.setPen(QPen(QColor(0, 200, 255), 3))
            painter.drawLine(0, 0, int(x), int(y))

        painter.restore()

        # 💥 CORE
        glow = int((math.sin(self.energy_phase) + 1) * self.glow_intensity / 2)

        painter.setBrush(QBrush(QColor(0, glow + 100, 255)))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(-25, -25, 50, 50)
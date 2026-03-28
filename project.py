from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

file_path = "hybrid_power_6dof_robotic_arm_proposal_v2.pdf"

styles = getSampleStyleSheet()
title_style = styles["Title"]
heading_style = styles["Heading2"]
normal = styles["BodyText"]

story = []

# Title
story.append(Paragraph("Hybrid-Power 6-DOF Industrial Robotic Arm Proposal", title_style))
story.append(Spacer(1, 0.4 * cm))

# Intro
story.append(Paragraph(
    "A comprehensive mechatronics proposal combining a 6-DOF robotic arm kit, "
    "dual-control architecture, hybrid power, and a professional telemetry dashboard.",
    normal
))
story.append(Spacer(1, 0.3 * cm))

# Project overview
story.append(Paragraph("Project Overview", heading_style))
story.append(Paragraph(
    "The system integrates tactile joystick control for direct manipulation and a web-based dashboard "
    "for remote supervision, live telemetry, and motion playback. A 0.96\" OLED serves as the local "
    "status display for Wi-Fi IP address, connection state, and battery voltage, while the main "
    "dashboard provides full telemetry and control visualization. The design supports uninterrupted "
    "wall-powered operation as well as mobile battery-powered deployment.",
    normal
))

sections = [
    ("I. Mechanical & Structural Components", [
        "1 × 6-DOF Aluminum Robotic Arm Kit: includes structural links, rotating base, and gripper assembly.",
        "1 × Metal Ball Bearing Set: improves smooth, low-friction joint rotation.",
        "1 × M3 & M4 Stainless Steel Bolt/Nut Set: for assembly, reinforcement, and maintenance replacements.",
        "1 × Heavy-Duty Mounting Base (wood or acrylic): prevents tipping during high-speed motion.",
    ]),
    ("II. Actuators & Motion Control", [
        "6 × MG996R Metal Gear Servos: primary actuators for all six axes.",
        "1 × MG90S Micro Servo: optional spare for gripper upgrades or lightweight end-effector experiments.",
        "1 × PCA9685 16-Channel PWM Driver: stable multi-servo control with reduced jitter.",
    ]),
    ("III. Intelligence & Interface", [
        "1 × ESP32 DevKit V1: central controller, Wi-Fi host, and dashboard communication bridge.",
        "2 × 2-Axis Analog Joystick Modules: real-time tactile movement input.",
        "1 × 0.96\" I2C OLED Display: local status display for IP address, connection state, and battery voltage.",
        "1 × Software Suite: embedded HTML/CSS dashboard, WebSocket telemetry channel, and JavaScript visualization.",
    ]),
    ("IV. Hybrid Power & Charging", [
        "1 × 5V 10A DC Switching PSU: stable high-current supply during wall-powered operation.",
        "2 × 21700 High-Discharge Li-ion Batteries: untethered mobile operation.",
        "1 × 2S Battery Holder + 2S BMS: cell balancing and over-discharge protection.",
        "1 × USB-C 2S Charging Module: in-system charging without battery removal.",
        "1 × LM2596 Buck Converter: steps 7.4V battery path down to regulated 5V.",
        "1 × DC Barrel Jack to Terminal Block: secure external PSU connection.",
    ]),
    ("V. Connectivity & Safety", [
        "1 × 830-point Breadboard: reserved for signal-level prototyping including OLED interfacing, LED indicators, ADC testing, and other low-current logic circuits.",
        "1 × Power Distribution Block / Screw Terminal Rail: dedicated high-current power distribution path for all servo actuators to ensure stable multi-axis operation.",
        "1 × Jumper Wire Pack (M-M, M-F, F-F): approximately 60–100 wires for signal and logic connections.",
        "1 × 10A Power Toggle Kill Switch: emergency shutdown and safe servicing.",
        "LED Status Indicators: visual feedback for power and Wi-Fi connection.",
        "1 × Micro-USB Data Cable: firmware flashing and serial debugging.",
        "1 × ADS1115 ADC Module (optional): precision battery and PSU voltage telemetry.",
    ])
]

for heading, bullets in sections:
    story.append(Spacer(1, 0.3 * cm))
    story.append(Paragraph(heading, heading_style))
    for bullet in bullets:
        story.append(Paragraph(f"• {bullet}", normal))

doc = SimpleDocTemplate(file_path, pagesize=A4)
doc.build(story)

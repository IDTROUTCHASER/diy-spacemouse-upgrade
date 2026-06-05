# DIY Spacemouse Upgrade

A CircuitPython upgrade to the original DIY Spacemouse project for Fusion 360.

## Based on original project by sb-ocr
https://github.com/sb-ocr/diy-spacemouse

## Changes
- Rewrote code in CircuitPython instead of Arduino
- Fixed I2C compatibility issues with QT Py RP2040
- Added Solidworks navigation mode support
- Improved calibration and dead zone handling

## Hardware
- Adafruit QT Py RP2040
- Adafruit TLV493D 3D Magnetometer
- 2x push buttons
- Magnet
- Springs
- 3D printed enclosure (see original project)

## Software Requirements
- CircuitPython 10.x
- adafruit_tlv493d library
- adafruit_hid library

## Button Functions
- Button 1 (A2) = Send to Home View (requires Fusion 360 Add-in)
- Button 2 (SDA) = Fit to Screen

## Wiring
- STEMMA QT connector for sensor
- Button 1 = A2 and GND
- Button 2 = SDA and GND

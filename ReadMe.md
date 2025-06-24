# Plant Monitor Client 

This client was a school project inspired by a need to keep tabs on a growning garden. The first itteration is to simply get the monitor working and be able to wirelessly receive data from device without the use of WiFi.

Instead of WiFi a packet radio, listed below, is used to send a transmission of the current sensor state to the receiving system. This radio type was used for better control over power consumption for the transmitting device as the next enhancments to the hardware will include a battery and small solar panel.

Client side UI is done in NiceGui with Highcharts for the gauges.

This repository was developed along side this one: [circuit_python_water_sensor](https://github.com/jakedaylong/circuit_python_water_sensor).

These two repositories with remain more or less in sync with each other to allow easy loading to desired devices of a similar nature.

## Hardware Used
* Raspberry Pi 400
* Sparkfun Quik pHAT Extension
* Adafruit RFM69HCW 915Mhz Packet Radio



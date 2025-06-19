#pylint: disable=line-too-long
import board
import busio
import digitalio
import json
import adafruit_rfm69

RADIO_FREQ_MHZ = 915.0  # Frequency of the radio in Mhz. Must match your

CS = digitalio.DigitalInOut(board.D7)
RESET = digitalio.DigitalInOut(board.D25)
spi = busio.SPI(board.SCLK, MOSI=board.MOSI, MISO=board.MISO)
rfm69 = adafruit_rfm69.RFM69(spi, CS, RESET, RADIO_FREQ_MHZ)

def initialize_radio():

    # startup info from radio
    print(f"Temperature: {rfm69.temperature}C")
    print(f"Frequency: {rfm69.frequency_mhz}mhz")
    print(f"Bit rate: {rfm69.bitrate / 1000}kbit/s")
    print(f"Frequency deviation: {rfm69.frequency_deviation}hz")

    # initial state
    print("Waiting for packets...")


def read_data():
    packet = rfm69.receive(timeout=5.0)

    # If no packet was received during the timeout then None is returned.
    if packet is None:
        print("Received nothing! Listening again..." + str(rfm69.node))

    else:
        print(f"Received (raw bytes): {packet}")
        packet_text = str(packet, "utf-8")
        json_value = packet_text[2:-5]

        data = json.loads(json_value)

        print(f"Received (ASCII): {data['wetness']}, {data['humidity']} " + str(rfm69.rssi))

        return data
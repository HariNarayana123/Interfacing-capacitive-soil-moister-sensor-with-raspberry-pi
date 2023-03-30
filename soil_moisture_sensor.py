Import spidev
Import time
Spi=spidev.SpiDev()
Spi.open(0,0)

channel=0
vref=3.3v

def read_adc(channel):
      adc =spi.xfer2([1,(8+channel)<<4,0])
      data=((adc[1] & ob11) <<8) + adc[2])
      voltage= (adc_value * vref) / 1023.0
      return round(voltage,2)
     
while True:
     res=read_adc(channel)
     print("voltage: ", voltage)
     time.sleep(0.5)
spi.close()

import serial
import binascii
import struct
import time

#ser.EIGHTBITS
#ser.writeTimeout
try:
  ser = serial.Serial("COM4",500000,timeout=10)#Enter com port according to the com port detected
  #val=(hex(53)+hex(36)+'\r')
  #val2 = hex(86)
  a = ser.readable()
  print a
  b = ser.outWaiting()
  print b
  ser.writelines('V\r')
  print 'serial open'
  past=ser.read(8)
  print past

  ser.writelines('S6\r')
    
  print 'mode set open'
  past=ser.read(8)
  print past

  ser.writelines('O\r')
  print 'chanel open'
  past=ser.read(8)
  print past
  while 1:
    #send="\x56"
    
    #ser.writelines('2591122334411223344\r')
    
    print 'reading open'
    data=ser.read(189)
    data2 = data.split('t')
    print data2
    i=0
    for i in range(1,9):
      data2[i] = data2[i]
      xc = data2[i]
      i+=1
      print xc[0:3]
      v1= xc[4:12]
      v11 =(v1[0:2])
      v12=str(v1[2:4])
      v13=str(v1[4:6])
      v14=str(v1[6:8])

      v2= v11+" "+v12+ " "+v13+ " " + v14+ " "

      print str(xc[0:3])+": "+str(struct.unpack('<f', binascii.unhexlify(v2.replace(' ', '')))[0])
      print str(xc[12:15])+": "+str(struct.unpack('<f',binascii.unhexlify(v2.replace(' ', '')))[0])
    #xc[12:21]
    #print len(data2[2])
    val= data2[1]
    print val[0:3]
    val1 = data2[1]
    val2 = data2[2]
    val3 = data2[3]

    #data = data2[0]
    #print struct.unpack('<f', binascii.unhexlify(data.replace(' ', '')))[0]
    
    

    
    print 'serial closed'
    #ser.close()
    print "\n \n \n"
    time.sleep(2)
    
    

except:
  raise
  print 'exception'
  

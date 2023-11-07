//----------------------------------------
// Aurduino-Python Ethernet Communication
//----------------------------------------
#include <Ethernet.h>
#include <EthernetUdp.h>
#include <SPI.h>

//----------------------------------------------------------------------------------
byte mac[] = {0x90, 0xA2, 0xDA, 0x00, 0x4A, 0xE0}; //Arduino shield MAC address
IPAddress ip(192,168,1,6);//shield IP address
IPAddress ip2(192,168,1,7);
/*IPAddress subnet(255, 255, 255, 0); //Assign my subnet IP address
IPAddress gateway(192, 168, 1, 1); //Assign my gateway IP address
IPAddress dns(163,121,128,134);*/ 
//----------------------------------------------------------------------------------
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];  //array to store received data
String receivedData;                        //string to store received data
int packetSize;                             //variable to store received packet size
EthernetUDP UDP;                            //UDP object
unsigned int portt =5000;
//----------------------------------------------------------------------------------
void setup()
{
  Serial.begin(9600);
  pinMode(7,OUTPUT);
  digitalWrite(7,LOW); 
  delay(1500);
  Ethernet.begin(mac, ip);                  //initialize ethernet
  while (UDP.begin(5000)==0);  //initialize UDP to port number 5000
  
  digitalWrite(7,HIGH);
 
}
//----------------------------------------------------------------------------------
void loop()
{  
    UDP.parsePacket();     
 
    UDP.beginPacket(ip2, UDP.remotePort());//initialize packet send
    UDP.print("M");  
    UDP.endPacket();                       //send string back to Python                                //end packet send
    delay(1000);
     UDP.beginPacket(ip2, UDP.remotePort());
    UDP.print("N");
    UDP.endPacket();
    delay(1000);
    UDP.beginPacket(ip2, UDP.remotePort());
    UDP.print("F");
    UDP.endPacket();
    delay(1000);
    
  
}

#include <ESP8266WiFi.h>
#include <FirebaseESP8266.h>
               
#define FIREBASE_HOST "##" // Firebase host
#define FIREBASE_AUTH "##" //Firebase Auth code
#define WIFI_SSID ""
#define WIFI_PASSWORD "" 

const int btn = D0;
int temp =0;

//declaring the firebase object
FirebaseData firebaseData;


void setup() {

  Serial.begin(115200);   

  pinMode(D5, OUTPUT);
  pinMode(btn, INPUT);
  
  Serial.println("Serial communication started\n\n");  
           
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to ");
  Serial.print(WIFI_SSID);


  
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  
  Serial.println();
  Serial.print("Connected to ");
  Serial.println(WIFI_SSID);
  Serial.print("IP Address is : ");
  Serial.println(WiFi.localIP()); //check local ip
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);   // connect to firebase

  Firebase.reconnectWiFi(true);
  delay(1000);
}

void loop() {
  temp = digitalRead(btn);

if (Firebase.getString(firebaseData, "data")) {  //returns 1 or true if data is read

      //val = firebaseData.stringData();
      Serial.println(firebaseData.stringData());

      if (firebaseData.stringData() == "1" && temp == HIGH){
        digitalWrite(D5, HIGH);
      }

      else if (firebaseData.stringData() == "1" && temp == LOW){
        digitalWrite(D5, HIGH);
      }

      else if (firebaseData.stringData() == "0" && temp == HIGH){
        digitalWrite(D5, HIGH);
      }


      else if (firebaseData.stringData() == "0" && temp == LOW){
        digitalWrite(D5, LOW);
      }
    

  } else {
    Serial.println(firebaseData.errorReason());
  }
 }

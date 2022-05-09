# Pi Smart Camera

The Pi Smart Cam is an open-source DIY Camera designed for you to view live footage from your phone or any device. The following features

Features:
-	PIR Sensor – For Motion Detection even in the Dark 
-	Message Notification – Receive an email on the latest Motion Detected
-	Web Application - Camera App Client

## Requirements:
- This project builds on top of the [Pi Camera Stream Flask Repo](https://github.com/EbenKouao/pi-camera-stream-flask). 
- Install and setup the following dependencies.

## Preconditions
* Raspberry Pi 4, 2GB is recommended for optimal performance. However you can use a Pi 3 or older, you may see a increase in latency.
* Raspberry Pi 4 Camera Module or Pi HQ Camera Module (Newer version)
* Python 3 recommended.


## Pi Smart Cam

![Pi Stream Cam](./images/pi-smart-cam-featured.jpg) 


 | ![Pi Stream Cam](./images/open-nest-cam-promo-3-min.JPG) | ![Pi Stream Cam](./images/open-nest-cam-ports-back-min.JPG) |
 | -------------------------------------------------------- | ----------------------------------------------------------- |
 | Pi Setup                                                 | Pi - Live Stream                                            |

![Pi Stream Cam Livestream ](./images/arm-wave-near.jpeg)
Livestream Front Door

## Electronics

![Pi Stream Cam](./schematics/pi-camera-breadboard-pir-sensor_bb.png)

## Part List:

-	Pi Electronics:
    - Raspberry Pi 4 
    - Camera Module (HQ Pi Camera)

-	Arduino Electronics: Ring Bell and IR Sensor
    - PIR Sensor (HC-SR501)
    - Breadboard
    - Jumper Wires
    - Resistors: 330 Ohm 
    - Arduino Nano
    - LED
    - 220F Capacitor

## 3D Prints Assembly

.stl files for 3d Printing.
Contribute to the repo with new builds.


## Activate Email Notification

![Pi Smart Cam Email Notification](./images/email-notification-min.png)

```
pi_email = "<from-email>"
pi_app_password = "<app-password>"
pi_port = 465
pi_host = "smtp.gmail.com"
notification_recipient = "<to-email>"
```

Note: If you use want to send email notifications via Gmail, enable 2FA and use App Passwords instead of storing the password as plain text. Consider using environment variables.



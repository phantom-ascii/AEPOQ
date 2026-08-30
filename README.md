<img width="1024" height="572" alt="image" src="https://github.com/user-attachments/assets/46bca99f-a9f0-4af0-9826-91775e230f20" />

# AEPOQ
## born to be different

AEPOQ was created by a 14 year old kid. I created AEPOQ to study on keyboard layouts and matricies. "Why" you may ask... Well i want to creat a laptop in the next 2 years and what better way to learn about hardware and laptops than making a keyboard (there are proably alot of better ways.) Unfortunately i could not add my full master step die to githubs large file limit and i didnt have time to set up lfs or smth like that cause im leaving for school in 2 hours. Anyways the keyboard is a 68 key 65% keyboard designed for productivity. It has a rotaty switch and an oled to make it special. AND A CANDY HOLDER ON THE RIGHT.Heres some eye candy:

<img width="544" height="723" alt="Screenshot From 2026-08-30 17-38-26" src="https://github.com/user-attachments/assets/352f2902-3ea8-4dc3-bd83-46adaff80768" />
<img width="853" height="605" alt="Screenshot From 2026-08-30 16-52-24" src="https://github.com/user-attachments/assets/f8d90234-7ee2-40b7-942f-f98d782229e2" />
<img width="950" height="504" alt="Screenshot From 2026-08-30 16-23-58" src="https://github.com/user-attachments/assets/3034f174-c40b-42eb-be91-b4cd7aabb938" />
<img width="1047" height="411" alt="Screenshot From 2026-08-30 16-23-42" src="https://github.com/user-attachments/assets/0c6301dd-8b9d-40a5-bd59-1b5a462d003c" />
<img width="1375" height="487" alt="Screenshot From 2026-08-30 16-22-54" src="https://github.com/user-attachments/assets/3eb271dc-a400-4f11-a890-68331457200b" />
<img width="768" height="520" alt="Screenshot From 2026-08-29 22-46-02" src="https://github.com/user-attachments/assets/7ae0bb94-63a3-4900-8ff3-a875727ff511" />
<img width="614" height="343" alt="Screenshot From 2026-08-29 22-43-03" src="https://github.com/user-attachments/assets/79a6447e-a8d8-439d-a17c-ee96b58f1136" />
<img width="1587" height="396" alt="Screenshot From 2026-08-29 22-37-18" src="https://github.com/user-attachments/assets/20d24fe7-520f-4fa5-9d6c-ed2dbc5f6cba" />

 I used a normal mattix for yhe key switches and a raspberry pi pico for the mcu. the firmware is a test and im not expecting it to work. i will fix it once i actually build the keyboard as that is what i usually do. The keyboard case is at a 6.3~ slant for imprived erganomics. Everything was designed me using models as a guide from open source repositorys. This project is also published on the hackclub programn, forge. I will be using cherry mx keyswitches and generic key caps. The rotary endoer is a ec11 from alps. the oled is a generic 0.91 oled 4 pin header and the mcu is a raspberry pi pico. The keyswitch layout is a generic 65% stagered QWERTY for productivity and general erganomics. If you want to rip any models from this repo go ahead. Its open source anyways.

 Here is the BOM:
 # 65% Custom Keyboard - Master Bill of Materials

## 1. Electronics & Hardware (AliExpress)

| Component | Store | Spec / Description | Price (USD) | Order Link |
| :--- | :--- | :--- | :--- | :--- |
| **Microcontroller** | WeAct Studio Official Store | RP2040 (8MB Black Edition) | $5.16 | [RP2040 Pico Board](https://www.aliexpress.com/item/1005003708090298.html) |
| **Diodes** | Chinese Super Electronic market | 1N4148 SOD-123 SMD Diodes (1000-pack) | $4.54 | [1N4148 SOD-123 Diodes](https://www.aliexpress.com/item/32354597825.html) |
| **Rotary Encoder** | DQLZV Official Store | EC11 Encoder 20mm Half-Handle (5-pack) | $2.85 | [EC11 Rotary Encoder](https://www.aliexpress.com/w/wholesale-digital-encoder-ec11.html) |
| **OLED Display** | diymore Alice1101983 Store | 0.91" 128x32 I2C Display Module | $3.09 | [0.91" I2C OLED Module](https://www.aliexpress.com/item/32815893431.html) |
| **Switches** | The Powerpuff Girls Switch Store | Cherry Switches (70-pack) | $26.58 | [Cherry MX Switches](https://www.aliexpress.com/item/100504669940336.html) |
| **Stabilizers** | YMDK Store | Screw-In PCB Mount Stabilizer Set | $18.62 | [YMDK PCB Stabilizers](https://www.aliexpress.com/item/1005012115758953.html) |
| **Keycaps** | Melokey Store | Line Gradient Side-Shine Cherry PBT | $18.32 | [Side-Shine PBT Keycaps](https://www.aliexpress.com/w/wholesale-keycaps-65.html) |
| **Heat-Set Inserts** | Zenhosit Store | Brass Threaded Inserts M2/M2.5/M3 (220-pack) | $4.91 | [M2 Brass Inserts](https://www.aliexpress.com/item/1005010241559236.html) |
| **Choice Discount** | Choice Discounts | Applied Checkout Savings | -$7.07 | — |
| **AliExpress Shipping** | Choice / Standard | Expedited Combined Delivery | $0.00 | Free |
| **AliExpress Subtotal** | | | **$84.06** | |

---

## 2. PCB Fabrication & 3D Printing (JLCPCB / JLC3DP)

| Item | Service | Description | Price (USD) |
| :--- | :--- | :--- | :--- |
| **PCB Prototypes (`Aepoq_Y7`)** | JLCPCB | White Solder Mask, 1.6 mm, HASL (5-pack) | $22.60 |
| **Keyboard Case (`Case.step`)** | JLC3DP | 9600 Resin, White SLA 3D Print (1 pc) | $88.74 |
| **Keyboard Lid (`Lid.step`)** | JLC3DP | 9600 Resin, White SLA 3D Print (1 pc) | $13.04 |
| **JLCPCB Shipping** | Standard / Express | Package Weight: 3.01 kg | $90.06 |
| **JLCPCB Coupons** | Checkout Coupon | Applied Savings | -$25.00 |
| **JLCPCB Subtotal** | | | **$189.44** |

---

## 3. Total Project Cost

| Category | Amount (USD) |
| :--- | :--- |
| **AliExpress Subtotal** | $84.06 |
| **JLCPCB Subtotal** | $189.44 |
| **Grand Total** | **$273.50** |

<img width="1499" height="699" alt="image" src="https://github.com/user-attachments/assets/b5f6545b-2b5b-4a58-9cd1-c3b81ce83eb9" />
<img width="734" height="809" alt="image" src="https://github.com/user-attachments/assets/35ce7327-6829-4432-9618-d7f56521c511" />

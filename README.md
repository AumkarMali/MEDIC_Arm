## Inspiration 🧑‍⚕️
In 2019 alone, Canada produced over 87,000 tons of medical waste, an amount rivalling the Great Pacific Garbage Patch [1]. Additionally, the improper disposal of medical waste around the world is considered a leading cause of infectious disease, causing up to 1 million deaths annually [2]. Hospital waste is very dangerous when handled poorly, and as populations continue to rise, so too will the amount of waste produced. Our team aimed to create a robotic arm to automate the proper disposal of biohazardous waste, reducing the risk associated with the process.

## What it does 💉
MedicArm is a robotic arm system designed to sort biohazardous waste into user-defined containers. This allows the worker to properly dispose of hazardous medical garbage without the risk of injury or illness. The user configures the robot through the use of voice commands, enabling hands-free control of the machine. The user can also add their own commands, for added functionality. Additionally, the device’s precision helps eliminate the improper sorting of waste, limiting human error.

## How we built it 🔧
**Software:** The code of the robot consists of a Raspberry Pi running code connecting to various servers and API’s to process data and generate decisions. This is done through some of the more in detailed programming explanations shown above. The second part of the software system is programmed on the Arduino microcontroller, which is in control of the hardware such as servo motors, and controls the mechanical and electrical components. By connecting the Raspberry Pi and Arduino together, commands can be converted to mechanical output.

**Mechanical:** The robotic arm was completely 3D printed on the Bambu Lab X1 Carbon, to have a highly refined look. The joints of the robotic arm were controlled with MIUZEI MG966R high torque servo motors, as well as micro 9g servo motors. The robot arm can grab on objects using a 3D printed claw. To deliver objects to the arm, a conveyor belt was built using a 360 degree continuous servo motor and duct tape as the belt. 

**Electrical:** To control the servo motors for the robot arm, servo motors were connected to the GPIO pins on an Arduino, where they could be directly controlled. The Arduino was connected to the Raspberry pi with a USB cable, so that the Raspberry Pi could send commands to the Arduino to tell the robot what to do. In terms of the Raspberry Pi electronics, many basic computer components, such as a microphone, and keyboard. These tools were used to setup the Raspberry Pi.

**Google Speech Recognition AI:** The Raspberry Pi uses the Google Speech Recognition library, powered by AI, which allows for the processing of human speech. By talking to an external microphone, the system captures audio input, which is then analyzed and converted into text. This text-based output serves as the foundational mechanism for interpreting and executing user commands. The integration of speech recognition enables seamless interaction between the user and the robot, to enable real-time voice processing for operational control.

**IBM Watson Text-to-Speech (TTS):** For communication between the robot and user, the Raspberry Pi uses the IBM Watson Text-to-Speech API. This system processes text input through advanced deep learning models to generate high-quality speech output. This enables the robot not only to comprehend and act on spoken commands but also to respond with natural, intelligible voice feedback.

 **MongoDB:** MongoDB allows us to keep a dynamic repository of commands, allowing us to store a diverse set of processing protocols. This allows users to customize the robot's functionality in real-time, and also ensures that predefined commands are readily available for accurate operation.

**OpenAI:** The system uses OpenAI's language models to allow for natural, context-aware conversations with the user. This allows the robot to understand complex instructions, ask clarifying questions when needed, and provide helpful feedback in a conversational tone.

## Challenges we ran into 💥
- We prepared CAD models with measurements with motors and screws we had at home, with plans to order more motors for the day of the Hackathon. On the day of the Hackathon, we discovered that the motors we ordered were not the exact same, so we had to adjust the sizes
- Originally, we tried to run the servo control code on the Raspberry Pi, but unfortunately all the Raspberry Pi libraries don’t work with the newest version of the Raspberry Pi. So we decided to instead send serial data to an Arduino instead to control the servos.

## Accomplishments that we're proud of 😝
We’re proud of the build quality and the build met most of our personal goals. In addition, we are proud of the hardware and software integration.

## What we learned 🤖
- Serial communication between Raspberry Pi and Arduino
- How to cad a robot arm with 5 degrees of freedom

## What's next for MedicArm 🦾
The MedicArm has a number of potential improvements in for the future:
- We aim to swap out the Raspberry Pi for an ESP32 microcontroller, which has better supported libraries for our purposes. 
- The robot design could be adapted to be more modular, allowing it to handle a wider range of biohazardous waste. This could also allow the robot to manage other types of dangerous substances.

## References
[1]	Narendra Singh, Oladele A. Ogunseitan & Yuanyuan Tang (2022) Medical waste: 
Current challenges and future opportunities for sustainable management, Critical Reviews in Environmental Science and Technology, 52:11, 2000-2022, DOI: 10.1080/10643389.2021.1885325

[2]	D. Duong, “Improper disposal of medical waste costs health systems and the environment,” Canadian Medical Association Journal, vol. 195, no. 14, pp. E518–E519, Apr. 2023, doi: https://doi.org/10.1503/cmaj.1096046.


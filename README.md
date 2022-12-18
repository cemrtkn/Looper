# Looper
Script for a pyhsically functioning musical layering tool (looper). Embedded in a Raspberry Pi 4 system

VA455 Final Project – Musical Looper:

The product, as it is in this folder, is fully implemented on software level. Main functionalities are as follows:

•	It is a primitive example of a looper
•	Primitive because, above all, it doesn’t have a count-in or builtin metronome, this is due to complications faced using python’s time.sleep tool and the inefficiency of it in a multithreading project
•	Core of a looper is implemented, using pygame’s mixer.sound as a sound board
•	Using multithreading for each looped sample
•	It doesn’t seem to overwhelm with the amount of samples concurrently being played
•	There is latency issues with playback time differing from the stop time of the record, I suspect that this is due to multithreading
•	Due to the latency, the layers built on top of each other may be asynchronous, however, randomness is fun!

Additional Hardware:
1-	A USB  microphone(initially i was planning on using the mic of an Apple earbud, however it was not possible due to USB sound card’s i/o ports being separated
2-	3PDT switch
3-	USB sound card

Case:
Using the case from this link(https://www.thingiverse.com/thing:3723481) as the base model, i have made small changes on the size of the case for he switch to fit. However, I wasn’t able to 3D print it so I wasn’t able to work with the fully developed end product in which case the Raspberry Pi would be housed in the case


Code:
Looper class is implemented in the LoopingThread file, the main code is suitably named ‘name.py’


Cem Ertürkan

![image](https://user-images.githubusercontent.com/73444238/208298450-fc00fac8-8def-4afe-b427-f189bbf06d06.png)

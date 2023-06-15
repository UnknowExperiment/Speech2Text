# Program to convert speech to text
# Author @inforkgodara

import speech_recognition as sr



# List all microphones
mic_check = False

if mic_check == True:
	mic_list = sr.Microphone.list_microphone_names()
	for i in range(len(mic_list)):
		print("index:", i, mic_list[i])
	selected_index = int(input("Enter your mic's index. "))
	mic = sr.Microphone(device_index=selected_index)
else:
	mic = sr.Microphone()


r = sr.Recognizer()
r.pause_threshold = 1 

def s2t():
	r.pause_threshold = 0.6

	# Noise Sampling
	print('Sampling noise for 0.8s')
	with mic as source:
		r.adjust_for_ambient_noise(source)

	# Begin TTS
	print("Please begin your speech")
	with mic as source:
		audio = r.listen(source)

	print('end')
	speech_input = r.recognize_google(audio)
	# print(speech_input)
	return speech_input

# print(s2t())
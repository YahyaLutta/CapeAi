import requests
import vlc

url = "https://cloudlabs-text-to-speech.p.rapidapi.com/synthesize"

payload = {
	"voice_code": "en-US-1",
	"text": "hello, what is your name?",
	"speed": "1.00",
	"pitch": "1.00",
	"output_type": "audio_url"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "f2aa3c499emsh8883aed0425a000p162175jsn693731f60c6f",
	"X-RapidAPI-Host": "cloudlabs-text-to-speech.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

p = vlc.MediaPlayer(str(url))
p.play()
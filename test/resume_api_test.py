import requests

url = "https://resume-parser-and-analyzer.p.rapidapi.com/api/v1/cv/"

payload = {}
files=[
  ('file',('resume sample.pdf',open('resume sample.pdf','rb'),'application/pdf'))
]
headers = {
  'X-RapidAPI-Key': '780c68ffb0msha7d91a86bde50eap1def2ejsn4a2f1940f2f9',
  'X-RapidAPI-Host': 'resume-parser-and-analyzer.p.rapidapi.com'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)

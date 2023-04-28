import requests

url = 'https://cloud.emlo.cloud/analysis/analyzeFile?outputType=json'
data = {
    "apiKey":'e18c7429-5e9d-4536-a2f1-e3f73bda8130' ,
    "apiKeyPassword":'XH@H)Q*D9ZYYTHK6J4@^3Q)(Z1PG5)6I$FUG2SJXEMJVW(N#86*5HD)(I(#I(7(T' ,
    "consentObtainedFromDataSubject": True
}

# Open the file in binary mode
with open('sbf.wav', 'rb') as file:
    files = {'file': file}

    response = requests.post(url, data=data, files=files)

print(response.text)

import requests

file_id = 123
api_url = 'http://127.0.0.1:8000/get-file/'

response = requests.get(api_url)
if response.status_code == 200:
    # Save the downloaded file to disk
    with open('downloaded_file.py', 'wb') as f:
        f.write(response.content)
    print('File downloaded successfully.')
else:
    print('File download failed.')
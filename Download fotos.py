import requests


def baixar_arquivo(url, local):
    res = requests.get(url)
    with open(f'teste1{end}', 'wb') as new_file:
        new_file.write(res.content)


link = str(input('link here: '))
end = (link[-4:])
baixar_arquivo(f'{link}', f'teste1{end}')

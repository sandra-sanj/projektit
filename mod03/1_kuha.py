min_length = 37  # cm

kuha_length = int(input('Anna kuhan pituus: '))

if kuha_length < min_length:
    kuha_length_to_min_length = min_length - kuha_length
    print(f'{kuha_length} cm pituinen kuha on alimittainen. Erotus minimipituuteen on {kuha_length_to_min_length} cm. '
          f'Laske kuha takaisin järveen.')
else:
    print(f'{kuha_length} cm pituinen kuha ei ole alimittainen.')

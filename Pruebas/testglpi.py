import glpi_api

URL = 'http://localhost/glpi-10.0.7/glpi/front/central.php'
APPTOKEN = 'J6Lon5uDbNIrcDPWfBnoTggdFs32ZjdEhC9P'
USERTOKEN = 'JuanDavidL'

try:
    with glpi_api.connect(URL, APPTOKEN, USERTOKEN) as glpi:
        print(glpi.get_config())
except glpi_api.GLPIError as err:
    print(str(err))
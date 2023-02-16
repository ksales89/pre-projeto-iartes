# Espaço destinado para atividade com testes automatizados
1. salvar log de "posição/lugar/id" usando testes AUTOMATIZADOS

Se você está usando Appium com Python, existem algumas maneiras de salvar logs de teste automatizado. Aqui estão algumas opções:
Use o módulo de logging do Python. O Python tem um módulo padrão de registro (logging) que pode ser usado para registrar logs de teste. Você pode usar a função logging.getLogger() para criar um objeto de registro e usar os métodos .debug(), .info(), .warning(), .error(), .critical() para registrar logs com diferentes níveis de gravidade. Você também pode usar o método .basicConfig() para configurar o formato de registro.
Aqui está um exemplo:

```
import logging 
logging.basicConfig(
    filename='meu_log.log', 
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.info('Teste iniciado')
```

Este código cria um arquivo de log chamado meu_log.log e registra uma mensagem de informação no log.
Use o Appium Server para salvar logs. O Appium Server pode salvar logs para você, incluindo logs de aplicativos, logs do servidor e logs de desempenho. Para habilitar o registro, basta adicionar as seguintes opções ao inicializar o driver:


```
from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'app': '/path/to/app.apk'
} 


from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'app': '/path/to/app.apk'
}



# habilitando o logging do Appium Server
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['appium:logLevel'] = 'debug'
desired_caps['appium:chromeOptions'] = {'w3c': False}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
```



Neste exemplo, a opção logLevel é definida como debug para registrar logs com nível de gravidade debug.

Use a biblioteca Loguru. A biblioteca Loguru fornece uma sintaxe mais amigável para registrar logs em Python. Para usá-lo, basta instalar a biblioteca usando o pip e importá-lo em seu código:

```
!pip install loguru

from loguru import logger

logger.add("meu_log.log")

logger.info('Teste iniciado')
```

Este código cria um arquivo de log chamado meu_log.log e registra uma mensagem de informação no log.

Independentemente da opção que você escolher, certifique-se de registrar informações relevantes e úteis para seus testes, e armazenar os logs em um local acessível a todos os membros da equipe de teste.
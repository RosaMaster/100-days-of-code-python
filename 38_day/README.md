### Rastreador de Treinos (Workout Tracker)

#### STEPS

- [**Step 01**](./doc/step1.md)

- [**Step 02**](./doc/step2.md)

- [**Step 03**](./doc/step3.md)

- [**Step 04**](./doc/step4.md)

- [**Step 05**](./doc/step5.md)

- [**Step 06**](./doc/step6.md)

#### Links uteís

| **Documentação**                                                                      |
| ------------------------------------------------------------------------------------- |
| [Requests Docs - Developer Interface](https://requests.readthedocs.io/en/latest/api/) |
| [OpenAI-API](https://openai.com/index/openai-api/)                                    |
| [Nutrition & Exercise API](https://www.nutritionix.com/business/api)                  |
| [Content Experience Suite API Documentation](https://docx.syndigo.com/developers)     |
| [Sheety API](https://sheety.co/)                                                      |

##### Objetivo

Criar um aplicativo de monitoramento de exercícios usando processamento de linguagem natural e planilhas do Google.

Você **não** conseguirá executar o código desta solução como está. Por quê? Você precisará adicionar **suas próprias** chaves de API como variáveis ​​de ambiente primeiro.

## Variáveis ​​de Ambiente do PyCharm

No PyCharm, você define suas variáveis ​​de ambiente em "Editar Configurações". Você deverá ver uma seção chamada "Ambiente" -> "Variáveis ​​de Ambiente". Lá, você pode clicar em um pequeno símbolo que abre uma janela onde você pode colar todas as suas variáveis ​​de ambiente ao mesmo tempo. O formato segue o exemplo do arquivo env_for_pycharm (use suas próprias chaves de API).

## Variáveis ​​de Ambiente do Replit

Para o Replit, você precisa clicar no símbolo de cadeado (Segredos) no menu. Lá, você pode adicionar suas variáveis ​​de ambiente. Você pode adicioná-las uma a uma ou colá-las de um arquivo .json. O .json fornecido é apenas um exemplo. Você precisará substituí-la por suas próprias chaves de API.

## FAQ KeyError

O nome das suas variáveis ​​de ambiente no seu código Python precisa corresponder ao nome real das suas variáveis ​​de ambiente. Se você usar:

```
API_KEY = os.environ["NT_API_KEY"]
```

Certifique-se de que a sua variável de ambiente se chama `NT_API_KEY`. Se você usar um nome diferente (como `ENV_NIX_API_KEY`), certifique-se de que o seu código Python corresponda.

## FAQ Sheety: Permissão Insuficiente

O Sheety precisa de permissão para acessar sua Planilha Google. Ao entrar no Sheety, você provavelmente esqueceu de conceder permissão. Saia do Sheety e entre novamente. Além disso, acesse sua Conta do Google -> Segurança -> Aplicativos de Terceiros com Acesso à Conta. Verifique se o Sheety está listado lá.

## FAQ Sheety: Solicitação Incorreta. O JSON Payload deve estar dentro de uma propriedade raiz chamada "X".

O nome da sua planilha do Google deve estar no plural. Caso contrário, o Sheety ainda esperará que ele esteja no plural em CamelCase no endpoint da API. Ou seja, se o nome da sua planilha for "Meus Treinos", você deverá usar "myWorkouts" no endpoint.

O nome do projeto no endpoint também deve estar em CamelCase.

O nome que você usar para a chave primária na chamada da API deve ser a versão em CamelCase do singular do nome da planilha. Ou seja, se o nome da sua planilha for "Meus Treinos", você deverá usar "myWorkout" no dicionário da API. Também pode ser necessário atualizar a página da API no Sheety.

[**[ INICIO ]**](#rastreador-de-treinos-workout-tracker)

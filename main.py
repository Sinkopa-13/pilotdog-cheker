import asyncio
import csv
import json
import requests
import config
from loguru import logger

class Checker:
    def __init__(self, wallet):
        self.wallet = wallet

    async def check(self):

        if config.proxy_use:
            result = requests.get(url="https://www.pilotdog.tech/api/get_eligible?address="+self.wallet, proxies=config.proxies)
        else:
            result = requests.get(url="https://www.pilotdog.tech/api/get_eligible?address="+self.wallet)
        if result.status_code == 200:
            data = json.loads(result.text)
            drop = data['data']['claimable_amount']
            return self.wallet, drop
        return 'error'


async def write_to_csv(wallet, drop):
    with open('result.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(['wallet', 'drop'])

        writer.writerow([wallet, drop])


async def main():
    print(f'============================================= Плюшкин Блог =============================================')
    print(f'subscribe to : https://t.me/plushkin_blog \n============================================================================================================\n')


    with open("wallets.txt", "r") as f:
        wallets = [row.strip() for row in f]

    batches = [wallets[i:i + config.amount_wallets_in_batch] for i in range(0, len(wallets), config.amount_wallets_in_batch)]

    for batch in batches:
        tasks = []
        for wallet in batch:
            checker1 = Checker(wallet)
            tasks.append(checker1.check())

        res = await asyncio.gather(*tasks)
        for res_ in res:
            wallet, drop= res_        
            await write_to_csv(wallet, drop)

        tasks = []


if __name__ == '__main__':
    # Запускаем цикл событий
    results = asyncio.run(main())
    logger.success(f'типа все!')


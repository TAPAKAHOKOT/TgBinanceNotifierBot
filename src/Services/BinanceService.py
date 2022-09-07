import requests as r
from aiogram.utils.exceptions import ChatNotFound

from Settings import settings


class BinanceService:
    @staticmethod
    async def check_if_price_increased():
        max_price = await BinanceService.get_max_price()

        if max_price > settings.binance_data['max_price']:
            await BinanceService.notify_price_go_up(max_price)
        elif max_price < settings.binance_data['max_price']:
            await BinanceService.notify_price_go_up(max_price, False)

        settings.binance_data['max_price'] = max_price

    @staticmethod
    async def notify_price_go_up(max_price, is_up: bool = True):
        for admin in settings.admins:
            try:
                await settings.bot.send_message(
                    chat_id=admin,
                    text=f'Макс. цена выросла📈: {max_price}' if is_up else f'Макс. цена упала📉: {max_price}'
                )
            except ChatNotFound:
                pass

    @staticmethod
    async def get_max_price():
        data = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 1,
            "payTypes": [
                "Mobiletopup"
            ],
            "countries": [],
            "publisherType": None,
            "asset": "USDT",
            "fiat": "RUB",
            "tradeType": "SELL"
        }
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "123",
            "content-type": "application/json",
            "Host": "p2p.binance.com",
            "Origin": "https://p2p.binance.com",
            "Pragma": "no-cache",
            "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
        }
        url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'

        result = r.post(url, headers=headers, json=data, timeout=3)
        json_res = result.json()

        if len(json_res['data']) <= 0:
            return -1

        return float(json_res['data'][0]['adv']['price'])

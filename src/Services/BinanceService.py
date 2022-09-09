import requests as r
from aiogram.utils.exceptions import ChatNotFound

from Settings import settings


class BinanceService:
    @staticmethod
    async def check_if_price_increased():
        max_price, user_no, nickname, duplicate_nickname, is_duplicate_price = await BinanceService.get_max_price_data()

        if settings.binance_data['max_price'] == -1:
            settings.binance_data['max_price'] = max_price
            return

        notify_is_duplicate_price = (settings.binance_data['duplicate_price'] != max_price) and is_duplicate_price

        if is_duplicate_price:
            settings.binance_data['duplicate_price'] = max_price
        else:
            settings.binance_data['duplicate_price'] = -1

        if (max_price != settings.binance_data['max_price']) or notify_is_duplicate_price:
            await BinanceService.notify_price_go_up(
                settings.binance_data['max_price'],
                max_price,
                nickname,
                duplicate_nickname,
                notify_is_duplicate_price
            )

        settings.binance_data['max_price'] = max_price

    @staticmethod
    async def notify_price_go_up(
            old_max_price,
            max_price,
            nickname: str,
            duplicate_nickname: str,
            is_duplicate_price: bool
    ):
        new_price_percents = round(max_price / old_max_price * 10) / 10 * (-1 if max_price < old_max_price else 1)

        message = f'Цена изменилась: {new_price_percents}%'
        message += f'\n\nПользователь {nickname} установил цену {max_price}'

        if is_duplicate_price:
            message = f'У пользователей {nickname} и {duplicate_nickname} одинаковая цена'

        for admin in settings.admins:
            try:
                await settings.bot.send_message(
                    chat_id=admin,
                    text=message
                )
            except ChatNotFound:
                pass

    @staticmethod
    async def get_max_price_data():
        data = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 2,
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

        is_duplicate_price = False
        duplicate_nickname = ''
        if len(json_res['data']) > 1:
            is_duplicate_price = \
                float(json_res['data'][0]['adv']['price']) == float(json_res['data'][1]['adv']['price'])
            duplicate_nickname = json_res['data'][1]['advertiser']['nickName'],

        return (
            float(json_res['data'][0]['adv']['price']),
            json_res['data'][0]['advertiser']['userNo'],
            json_res['data'][0]['advertiser']['nickName'],
            duplicate_nickname,
            is_duplicate_price
        )

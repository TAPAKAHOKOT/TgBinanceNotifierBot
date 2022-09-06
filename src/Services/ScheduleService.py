from asyncio import sleep as asleep

from aioschedule import (
    every as schedule_every,
    run_pending as schedule_run_pending
)

from .BinanceService import BinanceService


class ScheduleService:
    @staticmethod
    async def run_schedule():
        schedule_every(5).seconds.do(BinanceService.check_if_price_increased)

        while True:
            await schedule_run_pending()
            await asleep(5)

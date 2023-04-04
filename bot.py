import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import load_config, Config


async def main() -> None:
    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем bot, Dispatcher
    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

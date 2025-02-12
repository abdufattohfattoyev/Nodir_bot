from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("📊 Statistika"), KeyboardButton("➕ Kino Qo‘shish")],
        [KeyboardButton("📣 Reklama"),KeyboardButton("📋 Mavjud kinolar")],
        [KeyboardButton("🗑 Kino O‘chirish"), KeyboardButton("🔙 Admin menyu")],  # Reklama tugmasini qo'shish
    ],
    resize_keyboard=True
)

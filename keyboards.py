from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💸 Буст за ММР", callback_data="cat:mmr")],
        [InlineKeyboardButton(text="🏆 Сезонный буст", callback_data="cat:season")],
        [InlineKeyboardButton(text="⭐️ Буст звёзд", callback_data="cat:stars")],
        [InlineKeyboardButton(text="💥 Пати-буст", callback_data="cat:party")],
        [InlineKeyboardButton(text="🎓 Тренировка с PRO", callback_data="cat:training")],
        [InlineKeyboardButton(text="🌀 Клан с галочкой", callback_data="cat:clan")],
        [InlineKeyboardButton(text="💙 Участие в Rising", callback_data="cat:rising")],
        [InlineKeyboardButton(text="📞 Связь с менеджером", callback_data="support")],
    ])
    return kb


def back_to_menu_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Назад в меню", callback_data="back_menu")]
    ])


def payment_kb(order_id: int, price: int, parts: bool = True):
    buttons = [
        [InlineKeyboardButton(text="⭐ Оплатить Telegram Stars", callback_data=f"pay:stars:{order_id}")],
        [InlineKeyboardButton(text="💳 Оплатить картой (СБП)", callback_data=f"pay:sbp:{order_id}")],
    ]
    if parts and price >= 5000:
        buttons.append([InlineKeyboardButton(
            text=f"💸 Оплатить частями (3 платежа по {price // 3}₽)",
            callback_data=f"pay:parts:{order_id}"
        )])
    buttons.append([InlineKeyboardButton(text="◀️ Назад", callback_data=f"back_cat:{order_id}")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def manager_actions_kb(user_id: int):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Подтвердить заказ", callback_data=f"mng:confirm:{user_id}")],
        [InlineKeyboardButton(text="❌ Отклонить", callback_data=f"mng:reject:{user_id}")],
    ])

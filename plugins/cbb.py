from pyrogram import Client 
from bot import Bot
from config import OWNER_ID, ABOUT_TXT, HELP_TXT, START_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.database import add_user, del_user, full_userbase, present_user

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                     InlineKeyboardButton('ᴄʟᴏꜱᴇ', callback_data='close')]
                ]
            )
        )
    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help'),
                 InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data='about')],
                [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')]
            ])
        )
    elif data == "premium":
        await query.message.edit_text(
            text=f"Premium Benefits & Perks\nDirect Channel Links, No Ad Links\nSpecial Access In Events\n\nPricing Rates\n<blockquote>7 Days - INR 39\n15 Days - INR 69\n1 Month - INR 89\n3 Months - INR 249\n6 Months - INR 489\n12 Month - <a href=https://t.me/Adult_Flux_ProBot>Contact Owner</a></blockquote>\n\nReady To Upgrade?💓\n» Message @Adult_Flux_ProBot to get UPI or QR Code for payment.\n» Send a screenshot of your payment to @DoraShin_Hlo (𝑓𝑜𝑟 𝑎𝑢𝑡𝑜 𝑣𝑒𝑟𝑖𝑓𝑖𝑐𝑎𝑡𝑖𝑜𝑛).\n\n⚡ Seats are LIMITED for Premium Members – Grab Yours Now!",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/Adult_Flux_ProBot"),
                        InlineKeyboardButton("ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ", url="https://t.me/adult_Flux")
                    ],
                    [
                        InlineKeyboardButton("ᴏɴʟʏғᴀɴs", url="https://t.me/+-SnePh_K_QU4ZWVl"),
                        InlineKeyboardButton("ᴊᴀᴠ ʟɪᴠᴇ ᴀᴄᴛɪᴏɴ", url="https://t.me/+o709ZnSKF7xlNWU1")
                    ],
                    [
                        InlineKeyboardButton("ʜᴀɴɪᴍᴇ&ʜ*ɴᴛᴀɪ", url="https://t.me/+8aWEpN1c265jZWE1"),
                        InlineKeyboardButton("🔒ᴄʟᴏꜱᴇ", callback_data='close')
                    ]
                ]
            )
        )

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
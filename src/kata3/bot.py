import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    return update.message.reply_text("Hola, Geeks!")    
    

def help(update, context):
    return update.message.reply_text("Ayudame!")    
    

def mayus(update, context):
    
    return context.args[0].upper()

def alreves(update, context):
    """Repite el mensaje del usuario."""
    #
    return update.message.reply_text(context.args[0].reverse())

def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Inicio del Bot"""
    #Colocamos el Token creado por FatherBot
    updater = Updater(token=open("bot_token"), use_context=True)

    # Es el Registro de Comandos a través del dispartcher
    dp = ["start","help","mayus","alreves"]

    
    
    update.dispatcher.add_handler(CommandHandler(dp[0],start))    
    update.dispatcher.add_handler(CommandHandler(dp[1],help))    
    update.dispatcher.add_handler(CommandHandler(dp[2],mayus))
    update.dispatcher.add_handler(MessageHandler(Filters.text, dp[3]),alreves)
    # Este comando es un Trigger que se lanza cuando no hay comandos [alreves]
    #
    
    # Y este espera al error
    dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()

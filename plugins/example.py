from say import fmt

from plugin_system import Plugin

plugin = Plugin("Пример плагина")

# Желательно первой командой указывать основную (она будет в списке команд)
@plugin.on_command('тестовыйплагин', 'примерплагина')
def anynameoffunctioncanbehere(vk, msg, args):
    print("OK!")
    vk.respond(msg, {'message': fmt('Пример плагина (аргументы - {args})')})

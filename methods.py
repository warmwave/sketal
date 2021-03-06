# Словарь, ключ - раздел API методов, значение - список разрешённых методов
ALLOWED_METHODS = {
    'groups': ('getById',
               'getCallbackConfig',
               'getCallbackServer',
               'getCallbackSettings',
               'getMembers',
               'setCallbackServer',
               'setCallbackServerSettings',
               'setCallbackSettings'),

    'docs': ('getMessagesUploadServer',
             'getWallUploadServer'),

    'photos': ('getMessagesUploadServer',
               'saveMessagesPhoto')
}
# Словарь, ключ - раздел API методов, значение - список запрещённых методов
DISALLOWED_MESSAGES = ('addChatUser',
                       'allowMessagesFromGroup',
                       'createChat',
                       'denyMessagesFromGroup',
                       'deleteChatPhoto',
                       'editChat',
                       'getChat',
                       'getChatUsers',
                       'getLastActivity',
                       'markAsImportant',
                       'removeChatUser',
                       'searchDialogs',
                       'setActivity',
                       'setChatPhoto')


def is_available_from_group(key: str) -> bool:
    if key == 'execute':
        return True

    try:
        topic, method = key.split('.')
    except ValueError:
        return False

    # Если раздел - messages, проверяем, нельзя ли выполнить этот метод
    if topic == 'messages':
        return method not in DISALLOWED_MESSAGES

    # Получаем список разрешённых методов для данного раздела
    methods_allowed = ALLOWED_METHODS.get(topic, None)

    if not methods_allowed:
        return False

    if method in methods_allowed:
        return True


# Методы, которые можно выполнять без авторизации API
ALLOWED_PUBLIC = {
    'apps': ('get', 'getCatalog'),

    'auth': ('checkPhone', 'confirm', 'restore', 'signup'),

    'board': ('getComments', 'getTopics'),

    'database': ('getChairs', 'getCities', 'getCitiesById',
                 'getCountries', 'getCountriesById', 'getFaculties',
                 'getRegions', 'getSchoolClasses', 'getSchools',
                 'getStreetsById', 'getUniversities'),

    'friends': ('get',),

    'groups': ('getById', 'getMembers', 'isMember'),

    'likes': ('getList',),

    'newsfeed': ('search',),

    'pages': ('clearCache',),

    'photos': ('get', 'getAlbums', 'getById', 'search'),

    'users': ('get', 'getFollowers', 'getSubscriptions'),

    'utils': ('checkLink', 'getServerTime', 'resolveScreenName'),

    'video': ('getCatalog', 'getCatalogSection'),

    'wall': ('get', 'getById', 'getComments', 'getReposts', 'search'),

    'widgets': ('getComments', 'getPages')
}


def is_available_from_public(key: str) -> bool:
    try:
        topic, method = key.split('.')
    except ValueError:
        return False

    methods = ALLOWED_PUBLIC.get(topic, ())
    if method in methods:
        return True

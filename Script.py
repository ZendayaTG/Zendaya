class script(object):
    START_TXT = """<b>š·š“š»š¾ {} š„°šāā</b>
    
<b>Hey Sweetheart, My Name Is <a href=https://t.me/{}>{}</a>. I'm a Powerful Series Auto-Filter Bot.</b>

<b>Just send in the series name. Thats All, and i will Provide Tons of series There..š</b>"""
    HELP_TXT = """š·š“š {}
    
<b>ā PLEASE DONT SPAM ME...š¤</b>
    
š·š“šš“ šøš šš·š“ š·š“š»šæ šµš¾š š¼š š²š¾š¼š¼š°š½š³š."""
    ABOUT_TXT = """<b>āÆ CREATOR: Hislordship</b>
<b>āÆ MOVIE CHANNEL: <a href=https://t.me/+R59lJd9RGV1iNzZk>Hislordship Movies</a></b>
<b>āÆ SERIES CHANNEL: <a href=https://t.me/+14mNx7OU_BxjMTE0>LordshipTV</a></b>
<b>āÆ CREDIT: To Everyone that created this repo</b>"""
    SOURCE_TXT = """<b>NOTE:</b>
<b>THIS BOT WAS MADE USING SO MANY REPOS!! credit I give unto them in the mighty name of Jesus, Amen!\n\nš²š®š“š±š¢š¤ š¢š®š£š¤ ~ š­š®š³ š šµš šØš«š š”š«š¤ š±šØš¦š§š³ š­š®š¶</b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. I should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
ā¢ /filter - <code>add a filter in chat</code>
ā¢ /filters - <code>list all the filters of a chat</code>
ā¢ /del - <code>delete a specific filter in chat</code>
ā¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- I Support both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. I support buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Lordshipmovies)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
ā¢ /connect  - <code>connect a particular chat to your PM</code>
ā¢ /disconnect  - <code>disconnect from a chat</code>
ā¢ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
ā¢ /id - <code>get id of a specified user.</code>
ā¢ /info  - <code>get information about a user.</code>
ā¢ /imdb  - <code>get the film information from IMDb source.</code>
ā¢ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
ā¢ /logs - <code>to get the rescent errors</code>
ā¢ /stats - <code>to get status of files in db.</code>
ā¢ /delete - <code>to delete a specific file from db.</code>
ā¢ /users - <code>to get list of my users and ids.</code>
ā¢ /chats - <code>to get list of the my chats and ids </code>
ā¢ /leave  - <code>to leave from a chat.</code>
ā¢ /disable  -  <code>do disable a chat.</code>
ā¢ /ban  - <code>to ban a user.</code>
ā¢ /unban  - <code>to unban a user.</code>
ā¢ /channel - <code>to get list of total connected channels</code>
ā¢ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """ā šš¾šš°š» šµšøš»š“š: <code>{}</code>
ā šš¾šš°š» ššš“šš: <code>{}</code>
ā šš¾šš°š» š²š·š°šš: <code>{}</code>
ā ššš“š³ ššš¾šš°š¶š“: <code>{}</code> š¼šš±
ā šµšš“š“ ššš¾šš°š¶š“: <code>{}</code> š¼šš±"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

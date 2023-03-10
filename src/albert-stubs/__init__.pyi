def debug(obj: object) -> None:
    '''Log a message to stdout. Note that `debug` is effectively a NOP in release builds. Puts the passed object into
    `str()` for convenience. The messages are logged using the QLoggingCategory of the python extension and therefore
    are subject to filter rules.'''
    pass

def info(obj: object) -> None:
    '''Log a message to stdout. Note that `debug` is effectively a NOP in release builds. Puts the passed object into
    `str()` for convenience. The messages are logged using the QLoggingCategory of the python extension and therefore
    are subject to filter rules.'''
    pass

def warning(obj: object) -> None:
    '''Log a message to stdout. Note that `debug` is effectively a NOP in release builds. Puts the passed object into
    `str()` for convenience. The messages are logged using the QLoggingCategory of the python extension and therefore
    are subject to filter rules.'''
    pass

def critical(obj: object) -> None:
    '''Log a message to stdout. Note that `debug` is effectively a NOP in release builds. Puts the passed object into
    `str()` for convenience. The messages are logged using the QLoggingCategory of the python extension and therefore
    are subject to filter rules.'''
    pass

def cacheLocation() -> str:
    '''Returns the writable cache, config and data location of the app. E.g. on Linux *$HOME/.cache/albert/*,
    *$HOME/.config/albert/* and *$HOME/.local/share/albert/*.'''

def configLocation() -> str:
    '''Returns the writable cache, config and data location of the app. E.g. on Linux *$HOME/.cache/albert/*,
    *$HOME/.config/albert/* and *$HOME/.local/share/albert/*.'''

def dataLocation() -> str:
    '''Returns the writable cache, config and data location of the app. E.g. on Linux *$HOME/.cache/albert/*,
    *$HOME/.config/albert/* and *$HOME/.local/share/albert/*.'''

def setClipboardText(text: str = '') -> None:
    pass

def openUrl(url: str = '') -> None:
    pass

def runDetachedProcess(cmdln: list(str) = [], workdir: str = '') -> None:
    pass

def runTerminal(script: str = '', workdir: str = '', close_on_exit: bool = False) -> None:
    pass

def sendTrayNotification(title: str = '', msg: str = '', ms: int = 10000) -> None:
    pass

class Action:
    '''Represents the internal `albert::Action` class.'''

    def __init__(self, id: str, text: str, callable: object) -> None:
        pass

class Item:
    '''Corresponds to the internal class `albert::StandardItem`. See the C++ documentation for more info.'''

    def __init__(
        self,
        id: str = '',
        text: str = '',
        subtext: str = '',
        completion: str = '',
        icon: list(str) = [],
        actions: list(Action) = [],
    ) -> None:
        pass

class Extension:
    '''Corresponds to the internal class `albert::Extension` which is a virtual base class for all extensions. You
    _have to_ override the following functions in all subclasses.'''

    def id(self) -> str:
        '''***MANDATORY*** Return the extension id'''
    def name(self) -> str:
        '''***MANDATORY*** Return the human readable extension name'''
    def description(self) -> str:
        '''***MANDATORY*** Return an imperative, brief description'''
    def initialize(self) -> None:
        pass
    def finalize(self) -> None:
        pass

class QueryHandler(Extension):
    '''Corresponds to the internal extension class `albert::QueryHandler`. Subclass it to provide a query handling
    extension.'''

    def handleQuery(self, query: Query) -> None:
        '''***MANDATORY***. When the user types a query, this function is called with a query object representing the
        current query execution. See the Query section below.'''
    def synopsis(self) -> str:
        '''**Optional** Return a synopsis to display on empty queries'''
    def defaultTrigger(self) -> str:
        '''**Optional** Return a default trigger overwrite. Defaults to extension id.'''
    def allowTriggerRemap(self) -> bool:
        '''**Optional** Return a bool indicating if the user is allowed to remap the trigger. Defaults to True.'''

class Query:
    '''The query class represents a user query and is passed to the handleQuery function when the user starts a
    query.'''

    trigger: str
    '''Returns the trigger used to trigger this query'''

    string: str
    '''Returns the query string _without_ the trigger'''

    isValid: bool
    '''This flag indicates if the query is valid. A query is valid until the query manager cancels it. You should 
    regularly check this flag and abort the query handling if the flag is `False` to release threads in the 
    threadpool for the next query.'''

    def add(self, item: Item | list[Item]) -> None:
        '''
        - Adds a single item to the query
        - Adds a list of items to the query
        '''

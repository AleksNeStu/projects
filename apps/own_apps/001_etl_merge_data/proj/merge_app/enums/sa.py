import enum


# To avoid {TypeError}Object of type xxx is not JSON serializable use mixin str
# https://stackoverflow.com/questions/24481852/serialising-an-enum-member-to-json
# Used lower case for enums by design:)
@enum.unique
class SyncStatus(str, enum.Enum):
    started: str = 'started'
    skipped: str = 'skipped'
    got_data: str = 'got_data'
    finished: str = 'finished'  # meaning got data was parsed
    errors: str = 'errors'


@enum.unique
class SyncEndReason(str, enum.Enum):
    no_new_input_data: str = 'no_new_remote_data'
    get_data_errors: str = 'get_data_errors'
    data_parsing_errors: str = 'data_parsing_errors'
    data_parsing_end: str = 'data_parsing_end'


@enum.unique
class SyncType(str, enum.Enum):
    app_init: str = 'app_init'
    scheduled: str = 'scheduled'
    manual: str = 'manual'
    forced: str = 'forced'
    manual_forced: str = 'manual_forced'


@enum.unique
class NotSyncedItemReason(str, enum.Enum):
    duplicated_data: str = 'duplicated_data'
    duplicated_none: str = 'duplicated_none'
    not_recognized_data: str = 'not_recognized_data'


@enum.unique
class CurrencyType(str, enum.Enum):
    eur: str = 'eur'
    usd: str = 'usd'
    # ...


@enum.unique
class OperationType(str, enum.Enum):
    add: str = 'add'
    remove: str = 'remove'

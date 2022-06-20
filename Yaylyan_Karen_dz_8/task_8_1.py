import re


def email_parse(email_address):
    RE_MAIL_PARSE = re.compile(r'(?P<username>\w+)@(?P<domain>\w+\.\w+)$',
                               re.IGNORECASE)
    result = RE_MAIL_PARSE.match(email_address)
    if result:
        return result.groupdict()
    else:
        raise ValueError(f'wrong email: {email_address}')

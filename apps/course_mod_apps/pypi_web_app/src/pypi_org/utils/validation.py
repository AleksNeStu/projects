import email_validator as email_validator
import validate_email


def is_email_valid(email, check_if_email_existing=False):
    try:
        normalized_email = email_validator.validate_email(email).email
        if check_if_email_existing:
            return validate_email.validate_email(normalized_email)
        return True

    except email_validator.EmailNotValidError:
        return False
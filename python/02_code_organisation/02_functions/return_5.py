# return statements are also used to convey
# the status of operations


def send_email(email_id, message):
    if len(message) > 5:
        print("Message too large.")
        return -1
    else:
        print("Sending email")
        return 0


result = send_email("example@crampete.com", "Hi")

if result == 0:
    print("Email sent successfully.")
else:
    print("Failed to send email.")


result = send_email("example@crampate.com", "Hi. How are you?")

if result == 0:
    print("Email sent successfully.")
else:
    print("Failed to send email.")

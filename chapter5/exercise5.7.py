# (Duplicate Elimination) In organizations, a list of email addresses is often com-
# piled for marketing purposes. However, duplicate email addresses need to be removed
# from this list. Write a function that receives a list and returns a list containing only unique
# values. Test your function with a list of email addresses.

# def remove_duplicates(email_list):
#     unique_emails = []
#     for email in email_list:
#         if email not in unique_emails:
#             unique_emails.append(email)
#     return unique_emails
#
# email_list = [
#     "example1@example.com",
#     "example2@example.com",
#     "example1@example.com",
#     "example3@example.com",
#     "example2@example.com",
# ]
#
# unique_emails = remove_duplicates(email_list)
# print(unique_emails)



# def generate_username(email_list):
#     unique_emails = []
#     for email in email_list:
#         if email not in unique_emails:
#             unique_emails.append(email)
#             return unique_emails
#
#
# email_list = ["rotiminicol"]
# unique_email = generate_username(email_list)
# print(unique_email)

def generate_username(email_list):
    if "@" in email_list:
        email = email_list.split("@")[0]
        return email
    else:
        return None

email = generate_username("rotiminicol117@gmail.com")
print(email)



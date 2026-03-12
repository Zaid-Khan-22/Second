def inDomain(mail):
    return mail.split("@")[1] in allowed_domains

emails = ["alice@gmail.com", "bob@yahoo.com", "carol@gmail.com"]
allowed_domains = {"gmail.com"}

print(list(filter(inDomain, emails)))

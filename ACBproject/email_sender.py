import smtplib, ssl 

def send_email():
    sender_email = "acbcfg2023@gmail.com"
    receiver_email = "juskeerat@gmail.com"
    password = "jive koth yflp zdqi"
    
    smtp_server = "smtp.gmail.com"
    port = 587  
    context = ssl.create_default_context()

    subject = "ACB Update"
    body = "Here is information about our upcoming event!"
    message = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context) 
        server.login(sender_email, password)  
        server.sendmail(sender_email, receiver_email, message)

        print("Email sent. ")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        server.quit()  

send_email()

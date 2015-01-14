import sys
import smtpd
import asyncore
import email

class CustomSMTPServer(smtpd.SMTPServer):
    
    def process_message(self, peer, mailfrom, rcpttos, data):
        print 'Receiving message from:', peer
        print 'Message addressed from:', mailfrom
        print 'Message addressed to  :', rcpttos
        print 'Message length        :', len(data)
        print '--- '


        msg = email.message_from_string(data)
        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                # Skip multipart envelope
                continue
            elif part.get_content_maintype() == 'text':
                print 'Content type: ' + part.get_content_type()
                print '---'
                print part.get_payload(decode=1)
            else:
                print 'Skipping display of ' + part.get_content_type() + ' attachment.'
            print '---'


def main(*args):
    if len(args) == 0:
        args = sys.argv[1:]
    if len(args) > 1:
        bind = args[1]
    else:
        bind = '127.0.0.1'

    port = int(args[0])

    server = CustomSMTPServer((bind, port), None)
    asyncore.loop()

if __name__ == '__main__':
    main()

import sys
import smtpd
import asyncore

class CustomSMTPServer(smtpd.SMTPServer):
    
    def process_message(self, peer, mailfrom, rcpttos, data):
        print 'Receiving message from:', peer
        print 'Message addressed from:', mailfrom
        print 'Message addressed to  :', rcpttos
        print 'Message length        :', len(data)
        print '--- '
        print data[:512]


def main():
    if len(sys.argv) > 2:
        bind = sys.argv[2]
    else:
        bind = '127.0.0.1'

    port = int(sys.argv[1])

    server = CustomSMTPServer((bind, port), None)
    asyncore.loop()

if __name__ == '__main__':
    main()

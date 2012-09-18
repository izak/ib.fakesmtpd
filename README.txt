ib.fakesmtpd
============

This sets up a simple smtp server that dumps all transactions to stdout. I
wrote this because I am tired of having to configure exim/postfix on
development machines just so I can see what the email would look like. Though
similar packages exist, none of them was easily installable by buildout.

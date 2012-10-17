ib.fakesmtpd
============

This sets up a simple smtp server that dumps all transactions to stdout. I
wrote this because I am tired of having to configure exim/postfix on
development machines just so I can see what the email would look like. Though
similar packages exist, none of them was easily installable by buildout.

Using with buildout
===================

If you use mr.developer, add it to your sources:

[sources]
ib.fakesmtpd = git git://github.com/izak/ib.fakesmtpd.git

Then add this to buildout (and add smtpd to buildout::parts):

[smtpd]
recipe = zc.recipe.egg:scripts
eggs = ib.fakesmtpd
arguments = 1025

Finally configure plone to use an smtp server on localhost port 1025,
and run bin/smtpd when you need an smtp server.

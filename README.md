# Millennium Panel

__Big fat disclaimer__: This is a work in progress and not a functional product yet, whatsoever. 

## History
Some time in 2014, I was an exchange student in Montréal, Canada and stumbled right into the decomissioning periode of Millennium payphones by Bell Canada and BCE.

The local hackerspace, [Foulab](https://foulab.org/), had one of the Millennium phones - however it was gutted due to it not being in working order. As I soon found out: a state in which pretty much all privately owned/collected Millenniums were.

I started researching the phones and even managed to find a few likeminded people who were friendly enough to hook me up with some additional information and helping me get development underway.

[On November, 13th 2016 we were able to provision a stock Millennium phone](https://twitter.com/boscop/status/797863014569562112).

However, the code pictured there was still sending static blobs of data (extracted from DEMO-Code firmware and sniffed from working payphone lines). But knowing how packages are to be constructed, I set out to create an easy to use UI which would be available as a hosted service at https://millennium.management/ or for self-hosting.

Probably out of misguided pride, I wanted to offer a somewhat finished, working product to the world before publishing the project. But more than 5 years later the project is still nowhere near completition. This, combined with the excellent work of [@hharte](https://github.com/hharte/) on his [mm_manager](https://github.com/hharte/mm_manager), published in January 2020 brought me the conclusion that I should probably just publish everything "as is" and request the support of the community to finish this project.

## Resources
I curated an extensive collection of information regarding the Millennium payphones at https://wiki.millennium.management/. Feel free to have a look and contribute.

There is a list of all known (to me) tables exisiting in the Millennium universe at https://wiki.millennium.management/dlog:start. Most relevant tables have also a description of how the packages are constructed, including differences for MTR1.x and MTR2.x.

## Vital Tables
Every phone needs at least these tables set up:
- [DLOG_MT_NCC_TERM_PARMS](https://wiki.millennium.management/dlog:DLOG_MT_NCC_TERM_PARMS)
- [DLOG_MT_INSTALL_PARMS](https://wiki.millennium.management/dlog:DLOG_MT_INSTALL_PARMS)
- [DLOG_MT_FCONFIG_OPTS](https://wiki.millennium.management/dlog:DLOG_MT_FCONFIG_OPTS)
- [DLOG_MT_COIN_VAL_TABLE](https://wiki.millennium.management/dlog:DLOG_MT_COIN_VAL_TABLE)
- [DLOG_MT_CARD_TABLE](https://wiki.millennium.management/dlog:DLOG_MT_CARD_TABLE)
- [DLOG_MT_RATE_TABLE](https://wiki.millennium.management/dlog:DLOG_MT_RATE_TABLE)
- [DLOG_MT_NPA_NXX_TABLE_1](https://wiki.millennium.management/dlog:DLOG_MT_NPA_NXX_TABLE_1)

Those tables have already been setup in this project.

## Contributing
There is still a lot to do in order to get this thing finished and into a working state. For starters, please have a look at the [GitHub issues](https://github.com/pc-coholic/millennium-panel/).

## Where is the ~beef~ glue(code)?
The original idea of this project was to split things into two separate projects: The panel which offers the UI and "package/payload generator" and the modem-daemon, which provides communication. With my predisposition for python, the daemon would have probably just used the existing models of the panel to access all the relevant data and push them out.

~Every~ Most models contain a `getFrame()` function, which returns the payload for the requested table. It would however be up to the modem-daemon to break the payload into the properly sized chunks and frame it for sending out the data.

The proof-of-concept which was destined to be changed into the glue-code is located ~here~ TODO: Dig out from old HDD.

## Architecture
Since this application is meant to be used as a hosted service, there are multiple "tenants" - or user groups. Every user can be a member or one or more tenants. Every tenant can have any number of phones and configurations - however the phones/configurations are tied to their tenant and cannot be used across tenants. Once a user is member of more than one tenant, they can switch between their tenants by using the drop-down-menu in the header-bar.

## Installation
* virtualenv -p /usr/bin/python3 env
* source env/bin/activate
* cd src
* pip install -r requirements.txt
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver
* Add at least one group and assign it to the user

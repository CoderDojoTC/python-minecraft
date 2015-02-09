==================
 Connect to Wi-Fi
==================

The username and password needed you need to connect to the campus
Wi-Fi is printed on the name badge passed out to each student and
mentor. These credentials are only good for the day of the session, so
if you have credentials saved on your computer from a prior session,
you will need to delete them and use the ones on your name
badge. These credentials are good for a single device (e.g., one
laptop). If you need an extra set of credentials for additional
devices, check with one of the mentors.

The official documentation for connecting to the UMN campus Wi-Fi is
available in the `WiFi Setup Guides`_. You should look at the section
for your specific operating system under the heading *UoM Secure*.

.. _WiFi Setup Guides: http://it.umn.edu/wifi-setup-guides

That said, you might be able to muddle through setting up a connection
using only the key bits of information below:

* Connect to the ``UofM Secure`` SSID. Other networks might seem to
  work (e.g., ``UofM Guest``), but they are bandwidth-restricted. You
  will have Internet connectivity, but will be terribly slow.

* Choose ``WPA2-Enterprise`` security.

* Choose ``AES`` encryption.

* If you're only visiting the campus for a short time to participate
  in a CoderDojo event, it is probably unnecessary to configure the
  *Protected EAP* properties or to mess around with any advanced
  settings like 802.1X or its certificates. Skipping those steps means
  you can't be positive that your PC is talking to the
  University-provided Wi-Fi infrastructure, but the risk is pretty
  low.

  .. warning:: However, if you live, study, or work on campus, take
               the extra time to go through all the setup steps in the
               official documentation so you stay secure.


Once Wi-Fi is working and you are able to visit websites (try the
`CoderDojo site`_), move on to :doc:`connecting to your lab instance
<lab-instance>`.

.. _CoderDojo site: http://www.coderdojotc.org/

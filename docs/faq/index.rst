======================
 Python Minecraft FAQ
======================

Why can't I...
==============

... change anything in my world?

   If you can't create or destroy blocks in your world through the
   Minecraft game itself, you probably need to make sure that your
   player has Operator_ status on the game server.

.. _Operator: http://minecraft.gamepedia.com/Operator


How do I...
===========

... create a new world?

   To create a new world, you need to use the :command:`/createworld
   WORLDNAME` to create a world named *WORLDNAME*. Then use the
   command :command:`/spawn WORLDNAME` to switch to that world. To
   create and joing a world named ``Mine``, you would use the
   following two commands::

     /createworld Mine
     /spawn Mine

   The world you are in when the game starts it called ``default``. To
   return to it, you would use the command :command:`/spawn default`.


Why is...
=========

... my network connection so slow?

   You might have connected via Wi-Fi to ``UofM Guest`` instead of
   ``UofM Secure``. The ``Guest`` network has much less bandwidth, and
   is too slow for most useful work.

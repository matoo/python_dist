#!/usr/bin/env python3

import re

class MailAddress:
  
  def __init__(self, mailaddress):
    self._mailaddress = mailaddress

  def __str__(self):
    return self._mailaddress

  @property
  def local(self):
    l = self._mailaddress.split('@')
    return l[0]

  @local.setter
  def local(self, local):
    l = self._mailaddress.split('@')
    new_address = '{}@{}'.format(local, l[1])
    self._mailaddress = new_address

  @property
  def domain(self):
    l = self._mailaddress.split('@')
    return l[1]

  @domain.setter
  def domain(self, domain):
    l = self._mailaddress.split('@')
    new_address = '{}@{}'.format(l[0], domain)
    self._mailaddress = new_address

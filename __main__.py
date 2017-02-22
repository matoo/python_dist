#!/usr/bin/env python3

import os
import sys
import networkx as nx
from lib.mail import MailAddress

if __name__ == '__main__':

  #out = uname()
  #print(out)

  mail_list = list()
  for i in range(0, 10):
    tmp = 'test{}@hoge.com'.format(i)
    mail = MailAddress(tmp)
    mail_list.append(mail)

  edge_list = list()
  edge_list.append((mail_list[0], mail_list[1]))
  edge_list.append((mail_list[1], mail_list[2]))
  edge_list.append((mail_list[2], mail_list[4]))
  edge_list.append((mail_list[4], mail_list[5]))
  edge_list.append((mail_list[5], mail_list[3]))
  edge_list.append((mail_list[3], mail_list[0]))

  G = nx.DiGraph()
  for e in edge_list:
    G.add_edge(e[0], e[1])

  for l in nx.simple_cycles(G):
    for e in l:
      print(e)

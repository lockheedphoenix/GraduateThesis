#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: lockheed
Information and Electronics Engineering
Huazhong University of science and technology
E-mail:lockheedphoenix@gmail.com
Created on: 4/29/14 3:19 PM

Copyright (C)  lockheedphoenix
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or  any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
from __future__ import division
import graph_tool.all as gt
import numpy.random as np
import scipy as sp

File = 'RG.xml.gz'
G = gt.load_graph(File)
k= 0
G = gt.load_graph(File)
for k in range(-20,1):
    p = sp.power(10, k/5)
    for e in G.edges():
        if np.random() < p:
            v = e.source()
            G.remove_edge(e)
            j = np.randint(0, G.num_vertices())
            while j == G.vertex_index[v] or gt.shortest_distance(G,v,G.vertex(j)) == 1:  # no parallel edges
                j = np.randint(0, G.num_vertices())

            G.add_edge(v, G.vertex(j))
    G.save(str(p)+'SW.xml.gz')






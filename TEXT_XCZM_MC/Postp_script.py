# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v7.6.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
sys.path.insert( 0, r'/home/mbgnktc2/Desktop/TEST_XCZM_MC')

###
### PARAVIS component
###

import pvsimple
pvsimple.ShowParaviewView()
#### import the simple module from the paraview
from pvsimple import *
#### disable automatic camera reset on 'Show'
pvsimple._DisableFirstRenderCameraReset()

# create a new 'MED Reader'
double_crackmed = MEDReader(FileName='/home/mbgnktc2/Desktop/TEST_XCZM_MC/visualresultstest_slice')

# Properties modified on double_crackmed
double_crackmed.AllArrays #= ['TS0/Mesh_3/ComSup0/Mesh_3@@][@@P0']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size


# show data in view
double_crackmedDisplay = Show(double_crackmed, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# change representation type
double_crackmedDisplay.SetRepresentationType('Surface With Edges')

# current camera placement for renderView1
renderView1.CameraPosition = [-221.42582325030642, 100.0, 0.0]
renderView1.CameraFocalPoint = [0.9999999999999939, 100.0, 0.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 101.98529305738157

# save screenshot
SaveScreenshot('/home/mbgnktc2/Desktop/screenshot.png', magnification=1, quality=100, view=renderView1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-221.42582325030642, 100.0, 0.0]
renderView1.CameraFocalPoint = [0.9999999999999939, 100.0, 0.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 101.98529305738157


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)

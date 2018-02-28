3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)]
Python Type "help", "copyright", "credits" or "license" for more information.
kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
generator = map(kingdoms.__getitem__, [0,3])
next(generator)
'Bacteria'
next(generator)
'Plantae'
next(generator)
Traceback (most recent call last):
  Python Shell, prompt 5, line 1
builtins.StopIteration:

# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
from kivymd import hooks_path as kivymd_hooks_path
import sys
import os
block_cipher = None
path = os.path.abspath(".")

# pyinstaller --onefile C:\Coding\pomodoro\pomodoro.spec --hidden-import=numpy
a = Analysis(['C:\\Coding\\pomodoro\\pomodoro.py'],
             pathex=[path],
             binaries=[],
             datas=[],
             hookspath=[kivymd_hooks_path],
             hiddenimports=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

Key = ['mkl','libopenblas']

def remove_from_list(input, keys):
    outlist = []
    for item in input:
        name, _, _ = item
        flag = 0
        for key_word in keys:
            if name.find(key_word) > -1:
                flag = 1
        if flag != 1:
            outlist.append(item)
    return outlist

a.binaries = remove_from_list(a.binaries, Key)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='pomodoro',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='C:\\Coding\\pomodoro\\111.ico')

coll = COLLECT(exe, Tree('C:\\Coding\\pomodoro'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='pomodoro')

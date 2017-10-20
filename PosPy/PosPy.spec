# -*- mode: python -*-

block_cipher = None


a = Analysis(['PosPy.py'],
             pathex=['/home/pmc/Projects/PointofSalePy/PosPy'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='PosPy',
          debug=False,
          strip=False,
          upx=True,
          console=True )

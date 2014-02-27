# -*- mode: python -*-
from kivy.tools.packaging.pyinstaller_hooks import install_hooks
install_hooks(globals())
a = Analysis(['/Users/samricklin/KBSVote/KBSVoteApp/main.py'],
             pathex=['/Users/samricklin/Downloads/PyInstaller-2.1/KBSVote'],
             hiddenimports=[],
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='KBSVote',
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe, Tree('/Users/samricklin/KBSVote/KBSVoteApp/'),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='KBSVote')

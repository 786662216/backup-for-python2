# -*- coding: utf-8 -*-
from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = ['Finance.py','-F','-c']
    run(opts)
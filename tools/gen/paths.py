# -*- coding: utf-8 -*-
"""ریشهٔ مخزن، نسبت به محل خودِ این فایل — تا ژنراتورها روی هر ماشینی کار کنند."""
import os

GEN = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(GEN))
SRC = os.path.join(ROOT, 'src')


def out(name):
    """مسیر یک فایل .dc.html در src/"""
    return os.path.join(SRC, name)

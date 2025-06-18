from flask import Flask, request, Response
import sys
import os

# إضافة المجلد الرئيسي إلى مسار البحث
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# استيراد التطبيق من الملف الرئيسي
from l_edit import flask_app

# تصدير التطبيق لاستخدامه مع Vercel
app = flask_app
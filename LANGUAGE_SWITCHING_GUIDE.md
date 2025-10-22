# دليل تبديل اللغة / Language Switching Guide

## 🌍 نظرة عامة / Overview

تم تحسين نظام إدارة الأصول ليدعم اللغتين العربية والإنجليزية بشكل كامل مع دعم RTL/LTR تلقائي وتصميم متجاوب.

The IT Asset Management System has been enhanced to fully support Arabic and English with automatic RTL/LTR support and responsive design.

---

## ✨ الميزات الجديدة / New Features

### 🔄 تبديل اللغة التلقائي / Automatic Language Switching
- **اتجاه تلقائي**: يتم تطبيق `dir="rtl"` للعربية و `dir="ltr"` للإنجليزية تلقائياً
- **Automatic Direction**: `dir="rtl"` for Arabic and `dir="ltr"` for English applied automatically
- **استمرارية اللغة**: يتم حفظ اللغة المختارة في الجلسة
- **Language Persistence**: Selected language is saved in session

### 🎨 ملفات CSS منفصلة / Separate CSS Files
- **style_ltr.css**: تنسيق كامل للغة الإنجليزية (LTR)
- **style_rtl.css**: تنسيق كامل للغة العربية (RTL)
- **rtl.css**: إصلاحات إضافية لـ RTL

### 📱 تصميم متجاوب محسّن / Enhanced Responsive Design
- **شريط جانبي قابل للطي**: ينطوي تلقائياً على الشاشات الصغيرة
- **Collapsible Sidebar**: Automatically collapses on small screens
- **انتقالات سلسة**: حركات ناعمة عند تبديل اللغة
- **Smooth Transitions**: Fluid animations when switching languages

---

## 🚀 كيفية الاستخدام / How to Use

### تبديل اللغة / Switch Language

1. **من صفحة تسجيل الدخول / From Login Page**:
   - اضغط على "English" أو "العربية" في أسفل النموذج
   - Click on "English" or "العربية" at the bottom of the form

2. **من لوحة التحكم / From Dashboard**:
   - اضغط على زر اللغة في الشريط العلوي (EN / عربي)
   - Click on the language button in the top bar (EN / عربي)

### الوصول من الكود / Access from Code

```python
# في routes.py / In routes.py
@bp.route('/set_language/<language>')
def set_language(language):
    session['language'] = language  # ar or en
    return redirect(request.referrer or url_for('dashboard.index'))
```

---

## 📝 الحسابات التجريبية / Test Accounts

يمكنك تسجيل الدخول باستخدام هذه الحسابات لتجربة النظام:

You can login using these accounts to test the system:

| الدور / Role | اسم المستخدم / Username | كلمة المرور / Password | الصلاحيات / Permissions |
|-------------|-------------------------|----------------------|-------------------------|
| مدير / Admin | `admin` | `admin123` | كاملة / Full Access |
| موظف / Staff | `staff` | `staff123` | عرض وتعديل / View & Edit |
| مشاهد / Viewer | `viewer` | `viewer123` | عرض فقط / View Only |

---

## 🎯 التحسينات الرئيسية / Key Improvements

### 1. استقرار اللغة / Language Stability
- ✅ اللغة ثابتة عبر جميع الصفحات
- ✅ Language remains consistent across all pages
- ✅ لا توجد مشاكل في RTL/LTR
- ✅ No RTL/LTR switching issues

### 2. التصميم المتجاوب / Responsive Design
- ✅ يعمل بشكل مثالي على سطح المكتب والجهاز اللوحي والجوال
- ✅ Works perfectly on desktop, tablet, and mobile
- ✅ الشريط الجانبي ينطوي تلقائياً على الشاشات الصغيرة
- ✅ Sidebar auto-collapses on small screens

### 3. تجربة مستخدم محسّنة / Enhanced UX
- ✅ انتقالات سلسة بين اللغات
- ✅ Smooth transitions between languages
- ✅ خطوط مناسبة (Cairo للعربية، Inter للإنجليزية)
- ✅ Appropriate fonts (Cairo for Arabic, Inter for English)

---

## 🔧 الهيكل الفني / Technical Structure

```
app/
├── static/
│   └── css/
│       ├── style_ltr.css    # LTR styling
│       ├── style_rtl.css    # RTL styling
│       └── rtl.css          # RTL utilities
├── templates/
│   └── base/
│       ├── layout.html      # Main layout with language detection
│       └── dashboard_layout.html  # Dashboard with responsive sidebar
└── translations/
    ├── ar/LC_MESSAGES/
    │   ├── messages.po      # Arabic translations source
    │   └── messages.mo      # Arabic translations compiled
    └── en/LC_MESSAGES/
        ├── messages.po      # English translations source
        └── messages.mo      # English translations compiled
```

---

## 🎨 نظام الألوان / Color Palette

- **Royal Blue** (الأزرق الملكي): `#1e3a8a` - Primary
- **Silver Gray** (الرمادي الفضي): `#64748b` - Secondary  
- **Emerald Green** (الأخضر الزمردي): `#10b981` - Accent
- **Orange** (البرتقالي): `#f97316` - Alerts

---

## 📱 اختبار التجاوب / Responsive Testing

### Desktop (سطح المكتب)
- ✅ الشريط الجانبي ظاهر دائماً
- ✅ Sidebar always visible
- ✅ عرض كامل للبطاقات والجداول
- ✅ Full display of cards and tables

### Tablet (الجهاز اللوحي)
- ✅ الشريط الجانبي قابل للطي
- ✅ Collapsible sidebar
- ✅ تخطيط متكيف
- ✅ Adaptive layout

### Mobile (الجوال)
- ✅ الشريط الجانبي مخفي افتراضياً
- ✅ Sidebar hidden by default
- ✅ قائمة همبرغر
- ✅ Hamburger menu
- ✅ بطاقات متراصة عمودياً
- ✅ Vertically stacked cards

---

## 🐛 استكشاف الأخطاء / Troubleshooting

### المشكلة: اللغة لا تتبدل / Issue: Language not switching
**الحل / Solution**:
1. امسح ذاكرة التخزين المؤقت للمتصفح / Clear browser cache
2. حدّث الصفحة بقوة (Ctrl+Shift+R) / Hard refresh (Ctrl+Shift+R)

### المشكلة: RTL غير صحيح / Issue: Incorrect RTL
**الحل / Solution**:
1. تأكد من تحميل `style_rtl.css` / Ensure `style_rtl.css` is loaded
2. افحص `dir` attribute في `<html>` / Check `dir` attribute in `<html>`

### المشكلة: الشريط الجانبي لا يعمل على الجوال / Issue: Sidebar not working on mobile
**الحل / Solution**:
1. تأكد من تحميل JavaScript / Ensure JavaScript is loaded
2. افحص console للأخطاء / Check console for errors

---

## 📞 الدعم / Support

إذا واجهت أي مشاكل، يرجى التحقق من:
If you encounter any issues, please check:

1. ملف السجل / Log file: `/tmp/logs/`
2. Console المتصفح / Browser console
3. Database connection
4. Flask-Babel configuration

---

## 🎓 موارد إضافية / Additional Resources

- [Flask-Babel Documentation](https://python-babel.github.io/flask-babel/)
- [TailwindCSS RTL Support](https://tailwindcss.com/docs/text-direction)
- [MDN - dir attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/dir)

---

**تم التحديث / Last Updated**: October 22, 2025  
**الإصدار / Version**: 2.0

"""
==========================================================
            مشروع: نظام إدارة المهام (To-Do List)
            اللغة: Python 3
            الوصف: برنامج بسيط لإدارة المهام اليومية
            المطور: طالب علوم الحاسب
==========================================================
"""

import json
import os
from datetime import datetime

# اسم الملف الذي سيتم حفظ المهام فيه
DATA_FILE = "tasks.json"


# ---------- دوال التعامل مع الملف ----------

def load_tasks():
    """تحميل المهام من الملف، أو إرجاع قائمة فارغة إذا لم يكن موجودًا."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_tasks(tasks):
    """حفظ قائمة المهام في الملف."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)


# ---------- دوال العمليات الأساسية ----------

def add_task(tasks):
    """إضافة مهمة جديدة."""
    title = input("📝 أدخل عنوان المهمة: ").strip()
    if not title:
        print("⚠️  لا يمكن إضافة مهمة فارغة!")
        return

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ تمت إضافة المهمة: {title}")


def show_tasks(tasks):
    """عرض جميع المهام."""
    if not tasks:
        print("\n📭 لا توجد مهام حتى الآن.\n")
        return

    print("\n" + "=" * 50)
    print("           📋 قائمة المهام")
    print("=" * 50)
    for task in tasks:
        status = "✔️ مكتملة" if task["done"] else "⏳ قيد التنفيذ"
        print(f"{task['id']}. [{status}] {task['title']}")
        print(f"   📅 {task['created_at']}")
    print("=" * 50 + "\n")


def complete_task(tasks):
    """تحديد مهمة كمكتملة."""
    show_tasks(tasks)
    if not tasks:
        return
    try:
        task_id = int(input("🔢 أدخل رقم المهمة المكتملة: "))
        for task in tasks:
            if task["id"] == task_id:
                task["done"] = True
                save_tasks(tasks)
                print(f"🎉 أحسنت! تم إنجاز: {task['title']}")
                return
        print("❌ لم يتم العثور على المهمة.")
    except ValueError:
        print("⚠️  من فضلك أدخل رقمًا صحيحًا.")


def delete_task(tasks):
    """حذف مهمة."""
    show_tasks(tasks)
    if not tasks:
        return
    try:
        task_id = int(input("🗑️  أدخل رقم المهمة للحذف: "))
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                removed = tasks.pop(i)
                # إعادة ترقيم المهام
                for index, t in enumerate(tasks, start=1):
                    t["id"] = index
                save_tasks(tasks)
                print(f"🗑️  تم حذف المهمة: {removed['title']}")
                return
        print("❌ لم يتم العثور على المهمة.")
    except ValueError:
        print("⚠️  من فضلك أدخل رقمًا صحيحًا.")


def show_stats(tasks):
    """عرض إحصائيات المهام."""
    total = len(tasks)
    done = sum(1 for t in tasks if t["done"])
    pending = total - done
    print("\n" + "=" * 50)
    print("           📊 الإحصائيات")
    print("=" * 50)
    print(f"📦 إجمالي المهام : {total}")
    print(f"✔️  المهام المكتملة : {done}")
    print(f"⏳ المهام المتبقية : {pending}")
    if total > 0:
        percent = (done / total) * 100
        print(f"📈 نسبة الإنجاز : {percent:.1f}%")
    print("=" * 50 + "\n")


# ---------- القائمة الرئيسية ----------

def show_menu():
    """عرض القائمة الرئيسية."""
    print("\n╔══════════════════════════════════════╗")
    print("║      📌 نظام إدارة المهام         ║")
    print("╠══════════════════════════════════════╣")
    print("║ 1. عرض المهام                       ║")
    print("║ 2. إضافة مهمة جديدة                 ║")
    print("║ 3. تعليم مهمة كمكتملة               ║")
    print("║ 4. حذف مهمة                         ║")
    print("║ 5. عرض الإحصائيات                   ║")
    print("║ 6. خروج                             ║")
    print("╚══════════════════════════════════════╝")


def main():
    """نقطة بداية تشغيل البرنامج."""
    print("\n🌟 مرحبًا بك في برنامج إدارة المهام 🌟")
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("👉 اختر رقمًا (1-6): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            show_stats(tasks)
        elif choice == "6":
            print("\n👋 إلى اللقاء! بالتوفيق في إنجاز مهامك.\n")
            break
        else:
            print("⚠️  اختيار غير صحيح، حاول مرة أخرى.")


# تشغيل البرنامج
if __name__ == "__main__":
    main()

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Diary")
root.geometry("600x700")

#|----------------------------Фреймы/Контейнеры----------------------------|
FrameLabelDiary = ttk.Frame(borderwidth=3, relief=SOLID, padding=(200,10))
LabelDiary = ttk.Label(FrameLabelDiary,text="Diary")

LabelDiary.pack(anchor="n")
FrameLabelDiary.pack(anchor="n",  padx=5, pady=5)

BodyFrames = ttk.Frame(borderwidth=1, relief=SOLID, width=400, height=700)

LeftContainerFrame = ttk.Frame(BodyFrames, borderwidth=0, relief=SOLID, padding=(10,5))
RightContainerFrame = ttk.Frame(BodyFrames,borderwidth=0, relief=SOLID, padding=(10,5))

FrameMonday = ttk.Frame(LeftContainerFrame, borderwidth=3, relief=SOLID, height=100)
FrameTuesday = ttk.Frame(LeftContainerFrame,borderwidth=3, relief=SOLID, height=100)
FrameWednesday = ttk.Frame(LeftContainerFrame,borderwidth=3, relief=SOLID, height=100)
FrameThursday = ttk.Frame(RightContainerFrame,borderwidth=3, relief=SOLID,height=100)
FrameFriday = ttk.Frame(RightContainerFrame,borderwidth=3, relief=SOLID, height=100)
FrameSaturday = ttk.Frame(RightContainerFrame,borderwidth=3, relief=SOLID, height=100)

FrameTools = ttk.Frame(borderwidth=2, relief=SOLID, width=200, height=150)
#|----------------------------Фреймы/Контейнеры----------------------------|

#|----------------------------Упаковка----------------------------|
BodyFrames.pack(anchor="n")

LeftContainerFrame.pack(anchor="nw", side=LEFT)
RightContainerFrame.pack(anchor="ne", side=RIGHT)

ttk.Label(LeftContainerFrame, text="Monday").pack(anchor="n", padx=5)
FrameMonday.pack(anchor="n", padx=5, pady=5)

ttk.Label(LeftContainerFrame, text="Tuesday").pack(anchor="center", padx=5)
FrameTuesday.pack(anchor="w", padx=5, pady=5)

ttk.Label(LeftContainerFrame, text="Wednesday").pack(anchor="n", padx=5)
FrameWednesday.pack(anchor="s", padx=5, pady=5)

ttk.Label(RightContainerFrame, text="Thursday").pack(anchor="s", padx=5)
FrameThursday.pack(anchor="ne", padx=5, pady=5)

ttk.Label(RightContainerFrame, text="Friday").pack(anchor="center", padx=5)
FrameFriday.pack(anchor="w", padx=5, pady=5)

ttk.Label(RightContainerFrame, text="Saturday").pack(anchor="s", padx=5)
FrameSaturday.pack(anchor="s", padx=5, pady=5)

FrameTools.pack(anchor="s", padx=5, pady=5)
#|----------------------------Колонны и уроки----------------------------|
LessonsList = [
    "","Russian", "English", "Mathematics", "Drawing", "Physical Education",
    "Physics", "History", "Philosophy", "Geography",
    "Computer Science", "Programming", "Psychology"
]

columns = ("number", "lesson", "mark")

lesson = ""
mark = None
ChoosedLessons = []
lessons = [["1", lesson, mark],["2", lesson, mark],["3", lesson, mark],
           ["4", lesson, mark],["5", lesson, mark],["6", lesson, mark]]

#Таблицы дней недели
# Понедельник
TreeMonday = ttk.Treeview(FrameMonday, columns=columns, show="headings")
TreeMonday.heading("number", text="№", anchor="center")
TreeMonday.heading("lesson", text="lesson", anchor="center")
TreeMonday.heading("mark", text="Mark", anchor="center")
TreeMonday.column("#1", anchor="center", width=30)
TreeMonday.column("#2", anchor="center", width=130)
TreeMonday.column("#3", anchor="center", width=30)

# Вторник
TreeTuesday = ttk.Treeview(FrameTuesday, columns=columns, show="headings")
TreeTuesday.heading("number", text="№", anchor="center")
TreeTuesday.heading("lesson", text="Урок", anchor="center")
TreeTuesday.heading("mark", text="Оценка", anchor="center")
TreeTuesday.column("#1", anchor="center", width=30)
TreeTuesday.column("#2", anchor="center", width=130)
TreeTuesday.column("#3", anchor="center", width=30)

# Среда
TreeWednesday = ttk.Treeview(FrameWednesday, columns=columns, show="headings")
TreeWednesday.heading("number", text="№", anchor="center")
TreeWednesday.heading("lesson", text="Урок", anchor="center")
TreeWednesday.heading("mark", text="Оценка", anchor="center")
TreeWednesday.column("#1", anchor="center", width=30)
TreeWednesday.column("#2", anchor="center", width=130)
TreeWednesday.column("#3", anchor="center", width=30)

# Четверг
TreeThursday = ttk.Treeview(FrameThursday, columns=columns, show="headings")
TreeThursday.heading("number", text="№", anchor="center")
TreeThursday.heading("lesson", text="Урок", anchor="center")
TreeThursday.heading("mark", text="Оценка", anchor="center")
TreeThursday.column("#1", anchor="center", width=30)
TreeThursday.column("#2", anchor="center", width=130)
TreeThursday.column("#3", anchor="center", width=30)

# Пятница
TreeFriday = ttk.Treeview(FrameFriday, columns=columns, show="headings")
TreeFriday.heading("number", text="№", anchor="center")
TreeFriday.heading("lesson", text="Урок", anchor="center")
TreeFriday.heading("mark", text="Оценка", anchor="center")
TreeFriday.column("#1", anchor="center", width=30)
TreeFriday.column("#2", anchor="center", width=130)
TreeFriday.column("#3", anchor="center", width=30)

# Суббота
TreeSaturday = ttk.Treeview(FrameSaturday, columns=columns, show="headings")
TreeSaturday.heading("number", text="№", anchor="center")
TreeSaturday.heading("lesson", text="Урок", anchor="center")
TreeSaturday.heading("mark", text="Оценка", anchor="center")
TreeSaturday.column("#1", anchor="center", width=30)
TreeSaturday.column("#2", anchor="center", width=130)
TreeSaturday.column("#3", anchor="center", width=30)

#|----------------------------Упаковка----------------------------|

# Понедельник
for LessonData in lessons:
    TreeMonday.insert("", "end", values=LessonData)
TreeMonday.pack(expand=1, anchor="center")

# Вторник
for LessonData1 in lessons:
    TreeTuesday.insert("", "end", values=LessonData1)
TreeTuesday.pack(expand=1, anchor="center")

# Среда
for LessonData2 in lessons:
    TreeWednesday.insert("", "end", values=LessonData2)
TreeWednesday.pack(expand=1, anchor="center")

# Четверг
for LessonData3 in lessons:
    TreeThursday.insert("", "end", values=LessonData3)
TreeThursday.pack(expand=1, anchor="center")

# Пятница
for LessonData4 in lessons:
    TreeFriday.insert("", "end", values=LessonData4)
TreeFriday.pack(expand=1, anchor="center")

# Суббота
for LessonData5 in lessons:
    TreeSaturday.insert("", "end", values=LessonData5)
TreeSaturday.pack(expand=1, anchor="center")


class AdminPanel:
    global lessons
    global LessonsList
    global TreeMonday, TreeTuesday, TreeWednesday, TreeThursday, TreeFriday, TreeSaturday
    def __init__(self):
        self.LabelAdminDiary = None
        self.adminroot = Toplevel()
        self.adminroot.title("AdminDiary")
        self.adminroot.geometry("700x1000")
        self.adminroot.minsize(700,800)
        #self.adminroot.maxsize(700,800)
        self.AdminObjects()

    def AdminObjects(self):
        FrameLabelAdminDiary = ttk.Frame(master=self.adminroot, borderwidth=3, relief=SOLID, padding=(200, 10))
        self.LabelAdminDiary = ttk.Label(FrameLabelAdminDiary, text="Admin panel")

        self.LabelAdminDiary.pack(anchor="n")
        FrameLabelAdminDiary.pack(anchor="n", padx=5, pady=5)

        # |----------------------------Фреймы----------------------------|
        BodyFramesAdmin = ttk.Frame(master=self.adminroot, borderwidth=1, relief=SOLID, width=400, height=700)

        LeftContainerFrameAdmin = ttk.Frame(BodyFramesAdmin, borderwidth=0, relief=SOLID, padding=(10,5))
        RightContainerFrameAdmin = ttk.Frame(BodyFramesAdmin, borderwidth=0, relief=SOLID, padding=(10,5))

        FrameMondayAdmin = ttk.Frame(LeftContainerFrameAdmin, borderwidth=3, relief=SOLID, padding=(5,5))
        FrameTuesdayAdmin = ttk.Frame(LeftContainerFrameAdmin, borderwidth=3, relief=SOLID, padding=(5,5))
        FrameWednesdayAdmin = ttk.Frame(LeftContainerFrameAdmin, borderwidth=3, relief=SOLID, padding=(5,5))
        FrameThursdayAdmin = ttk.Frame(RightContainerFrameAdmin, borderwidth=3, relief=SOLID, padding=(5,5))
        FrameFridayAdmin = ttk.Frame(RightContainerFrameAdmin, borderwidth=3, relief=SOLID, padding=(5,5))
        FrameSaturdayAdmin = ttk.Frame(RightContainerFrameAdmin, borderwidth=3, relief=SOLID, padding=(5,5))

        FrameToolsAdmin = ttk.Frame(master=self.adminroot, borderwidth=2, relief=SOLID, width=200, height=70)
        # |----------------------------Фреймы----------------------------|

        # |----------------------------Упаковка----------------------------|
        BodyFramesAdmin.pack(anchor="n")

        LeftContainerFrameAdmin.pack(anchor="nw", side=LEFT)
        RightContainerFrameAdmin.pack(anchor="ne", side=RIGHT)

        ttk.Label(LeftContainerFrameAdmin, text="Monday").pack(anchor="n", padx=5)
        FrameMondayAdmin.pack(anchor="n", padx=5, pady=5)

        ttk.Label(LeftContainerFrameAdmin, text="Tuesday").pack(anchor="center", padx=5)
        FrameTuesdayAdmin.pack(anchor="w", padx=5, pady=5)

        ttk.Label(LeftContainerFrameAdmin, text="Wednesday").pack(anchor="n", padx=5)
        FrameWednesdayAdmin.pack(anchor="s", padx=5, pady=5)

        ttk.Label(RightContainerFrameAdmin, text="Thursday").pack(anchor="s", padx=5)
        FrameThursdayAdmin.pack(anchor="ne", padx=5, pady=5)

        ttk.Label(RightContainerFrameAdmin, text="Friday").pack(anchor="center", padx=5)
        FrameFridayAdmin.pack(anchor="w", padx=5, pady=5)

        ttk.Label(RightContainerFrameAdmin, text="Saturday").pack(anchor="s", padx=5)
        FrameSaturdayAdmin.pack(anchor="s", padx=5, pady=5)

        FrameToolsAdmin.pack(anchor="s", padx=5, pady=5)

        AdminPanelButtonSave = ttk.Button(FrameToolsAdmin, text='Save', width=74, command=self.GetData)
        AdminPanelButtonSave.pack(anchor="nw")
        # |----------------------------Упаковка----------------------------|
        # |----------------------------Расстановка полей ввода----------------------------|
        lessonsz = [["1", lesson, mark], ["2", lesson, mark], ["3", lesson, mark],
                   ["4", lesson, mark], ["5", lesson, mark], ["6", lesson, mark]]
        # Понедельник
        labelN = ttk.Label(FrameMondayAdmin, text=" |№|                Lesson                | Mark |")
        label1 = ttk.Label(FrameMondayAdmin,text="   1")
        label2 = ttk.Label(FrameMondayAdmin, text="   2")
        label3 = ttk.Label(FrameMondayAdmin, text="   3")
        label4 = ttk.Label(FrameMondayAdmin, text="   4")
        label5 = ttk.Label(FrameMondayAdmin, text="   5")
        label6 = ttk.Label(FrameMondayAdmin, text="   6")

        self.lessonsMondayVar1 = StringVar(value=LessonsList[0])
        self.lessonsMondayVar2 = StringVar(value=LessonsList[0])
        self.lessonsMondayVar3 = StringVar(value=LessonsList[0])
        self.lessonsMondayVar4 = StringVar(value=LessonsList[0])
        self.lessonsMondayVar5 = StringVar(value=LessonsList[0])
        self.lessonsMondayVar6 = StringVar(value=LessonsList[0])

        comboboxWidth = 10
        comboboxMonday1 = ttk.Combobox(FrameMondayAdmin, textvariable=self.lessonsMondayVar1, values=LessonsList, state="readonly", width=comboboxWidth)
        comboboxMonday2 = ttk.Combobox(FrameMondayAdmin, textvariable=self.lessonsMondayVar2, values=LessonsList, state="readonly", width=comboboxWidth)
        comboboxMonday3 = ttk.Combobox(FrameMondayAdmin, textvariable=self.lessonsMondayVar3, values=LessonsList, state="readonly", width=comboboxWidth)
        comboboxMonday4 = ttk.Combobox(FrameMondayAdmin, textvariable=self.lessonsMondayVar4, values=LessonsList, state="readonly", width=comboboxWidth)
        comboboxMonday5 = ttk.Combobox(FrameMondayAdmin, textvariable=self.lessonsMondayVar5, values=LessonsList, state="readonly", width=comboboxWidth)
        comboboxMonday6 = ttk.Combobox(FrameMondayAdmin, textvariable=self.lessonsMondayVar6, values=LessonsList, state="readonly", width=comboboxWidth)

        entryWidth = 3
        self.entryMonday1 = ttk.Entry(FrameMondayAdmin, width=entryWidth)
        self.entryMonday2 = ttk.Entry(FrameMondayAdmin, width=entryWidth)
        self.entryMonday3 = ttk.Entry(FrameMondayAdmin, width=entryWidth)
        self.entryMonday4 = ttk.Entry(FrameMondayAdmin, width=entryWidth)
        self.entryMonday5 = ttk.Entry(FrameMondayAdmin, width=entryWidth)
        self.entryMonday6 = ttk.Entry(FrameMondayAdmin, width=entryWidth)


        # |----------------------------Расстановка полей ввода----------------------------|
        # |----------------------------Упаковка----------------------------|
        labelN.grid(row=0, column=0, columnspan=3, sticky="ew", padx=5, pady=(0, 10))

        label1.grid(row=1, column=0, sticky="w", padx=5, pady=2)
        comboboxMonday1.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        self.entryMonday1.grid(row=1, column=2, sticky="e", padx=5, pady=2)

        label2.grid(row=2, column=0, sticky="w", padx=5, pady=2)
        comboboxMonday2.grid(row=2, column=1, sticky="ew", padx=5, pady=2)
        self.entryMonday2.grid(row=2, column=2, sticky="e", padx=5, pady=2)

        label3.grid(row=3, column=0, sticky="w", padx=5, pady=2)
        comboboxMonday3.grid(row=3, column=1, sticky="ew", padx=5, pady=2)
        self.entryMonday3.grid(row=3, column=2, sticky="e", padx=5, pady=2)

        label4.grid(row=4, column=0, sticky="w", padx=5, pady=2)
        comboboxMonday4.grid(row=4, column=1, sticky="ew", padx=5, pady=2)
        self.entryMonday4.grid(row=4, column=2, sticky="e", padx=5, pady=2)

        label5.grid(row=5, column=0, sticky="w", padx=5, pady=2)
        comboboxMonday5.grid(row=5, column=1, sticky="ew", padx=5, pady=2)
        self.entryMonday5.grid(row=5, column=2, sticky="e", padx=5, pady=2)

        label6.grid(row=6, column=0, sticky="w", padx=5, pady=2)
        comboboxMonday6.grid(row=6, column=1, sticky="ew", padx=5, pady=2)
        self.entryMonday6.grid(row=6, column=2, sticky="e", padx=5, pady=2)

        FrameMondayAdmin.grid_columnconfigure(1, weight=1)

        # Вторник
        labelNTuesday = ttk.Label(FrameTuesdayAdmin, text=" |№|             Lesson             | Mark |")
        label1Tuesday = ttk.Label(FrameTuesdayAdmin, text="   1")
        label2Tuesday = ttk.Label(FrameTuesdayAdmin, text="   2")
        label3Tuesday = ttk.Label(FrameTuesdayAdmin, text="   3")
        label4Tuesday = ttk.Label(FrameTuesdayAdmin, text="   4")
        label5Tuesday = ttk.Label(FrameTuesdayAdmin, text="   5")
        label6Tuesday = ttk.Label(FrameTuesdayAdmin, text="   6")

        self.lessonsTuesdayVar1 = StringVar(value=LessonsList[0])
        self.lessonsTuesdayVar2 = StringVar(value=LessonsList[0])
        self.lessonsTuesdayVar3 = StringVar(value=LessonsList[0])
        self.lessonsTuesdayVar4 = StringVar(value=LessonsList[0])
        self.lessonsTuesdayVar5 = StringVar(value=LessonsList[0])
        self.lessonsTuesdayVar6 = StringVar(value=LessonsList[0])

        comboboxTuesday1 = ttk.Combobox(FrameTuesdayAdmin, textvariable=self.lessonsTuesdayVar1, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxTuesday2 = ttk.Combobox(FrameTuesdayAdmin, textvariable=self.lessonsTuesdayVar2, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxTuesday3 = ttk.Combobox(FrameTuesdayAdmin, textvariable=self.lessonsTuesdayVar3, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxTuesday4 = ttk.Combobox(FrameTuesdayAdmin, textvariable=self.lessonsTuesdayVar4, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxTuesday5 = ttk.Combobox(FrameTuesdayAdmin, textvariable=self.lessonsTuesdayVar5, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxTuesday6 = ttk.Combobox(FrameTuesdayAdmin, textvariable=self.lessonsTuesdayVar6, values=LessonsList,state="readonly", width=comboboxWidth)

        self.entryTuesday1 = ttk.Entry(FrameTuesdayAdmin, width=entryWidth)
        self.entryTuesday2 = ttk.Entry(FrameTuesdayAdmin, width=entryWidth)
        self.entryTuesday3 = ttk.Entry(FrameTuesdayAdmin, width=entryWidth)
        self.entryTuesday4 = ttk.Entry(FrameTuesdayAdmin, width=entryWidth)
        self.entryTuesday5 = ttk.Entry(FrameTuesdayAdmin, width=entryWidth)
        self.entryTuesday6 = ttk.Entry(FrameTuesdayAdmin, width=entryWidth)

        labelNTuesday.grid(row=0, column=0, columnspan=3, sticky="ew", padx=5, pady=(0, 10))
        label1Tuesday.grid(row=1, column=0, sticky="w", padx=5, pady=2)
        comboboxTuesday1.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        self.entryTuesday1.grid(row=1, column=2, sticky="e", padx=5, pady=2)
        label2Tuesday.grid(row=2, column=0, sticky="w", padx=5, pady=2)
        comboboxTuesday2.grid(row=2, column=1, sticky="ew", padx=5, pady=2)
        self.entryTuesday2.grid(row=2, column=2, sticky="e", padx=5, pady=2)
        label3Tuesday.grid(row=3, column=0, sticky="w", padx=5, pady=2)
        comboboxTuesday3.grid(row=3, column=1, sticky="ew", padx=5, pady=2)
        self.entryTuesday3.grid(row=3, column=2, sticky="e", padx=5, pady=2)
        label4Tuesday.grid(row=4, column=0, sticky="w", padx=5, pady=2)
        comboboxTuesday4.grid(row=4, column=1, sticky="ew", padx=5, pady=2)
        self.entryTuesday4.grid(row=4, column=2, sticky="e", padx=5, pady=2)
        label5Tuesday.grid(row=5, column=0, sticky="w", padx=5, pady=2)
        comboboxTuesday5.grid(row=5, column=1, sticky="ew", padx=5, pady=2)
        self.entryTuesday5.grid(row=5, column=2, sticky="e", padx=5, pady=2)
        label6Tuesday.grid(row=6, column=0, sticky="w", padx=5, pady=2)
        comboboxTuesday6.grid(row=6, column=1, sticky="ew", padx=5, pady=2)
        self.entryTuesday6.grid(row=6, column=2, sticky="e", padx=5, pady=2)
        FrameTuesdayAdmin.grid_columnconfigure(1, weight=1)

        # Среда
        labelNWednesday = ttk.Label(FrameWednesdayAdmin, text=" |№|             Lesson             | Mark |")
        label1Wednesday = ttk.Label(FrameWednesdayAdmin, text="   1")
        label2Wednesday = ttk.Label(FrameWednesdayAdmin, text="   2")
        label3Wednesday = ttk.Label(FrameWednesdayAdmin, text="   3")
        label4Wednesday = ttk.Label(FrameWednesdayAdmin, text="   4")
        label5Wednesday = ttk.Label(FrameWednesdayAdmin, text="   5")
        label6Wednesday = ttk.Label(FrameWednesdayAdmin, text="   6")

        self.lessonsWednesdayVar1 = StringVar(value=LessonsList[0])
        self.lessonsWednesdayVar2 = StringVar(value=LessonsList[0])
        self.lessonsWednesdayVar3 = StringVar(value=LessonsList[0])
        self.lessonsWednesdayVar4 = StringVar(value=LessonsList[0])
        self.lessonsWednesdayVar5 = StringVar(value=LessonsList[0])
        self.lessonsWednesdayVar6 = StringVar(value=LessonsList[0])

        comboboxWednesday1 = ttk.Combobox(FrameWednesdayAdmin, textvariable=self.lessonsWednesdayVar1,values=LessonsList, state="readonly", width=comboboxWidth)
        comboboxWednesday2 = ttk.Combobox(FrameWednesdayAdmin, textvariable=self.lessonsWednesdayVar2,values=LessonsList, state="readonly", width=comboboxWidth)
        comboboxWednesday3 = ttk.Combobox(FrameWednesdayAdmin, textvariable=self.lessonsWednesdayVar3,values=LessonsList, state="readonly", width=comboboxWidth)
        comboboxWednesday4 = ttk.Combobox(FrameWednesdayAdmin, textvariable=self.lessonsWednesdayVar4,values=LessonsList, state="readonly", width=comboboxWidth)
        comboboxWednesday5 = ttk.Combobox(FrameWednesdayAdmin, textvariable=self.lessonsWednesdayVar5,values=LessonsList, state="readonly", width=comboboxWidth)
        comboboxWednesday6 = ttk.Combobox(FrameWednesdayAdmin, textvariable=self.lessonsWednesdayVar6,values=LessonsList, state="readonly", width=comboboxWidth)

        self.entryWednesday1 = ttk.Entry(FrameWednesdayAdmin, width=entryWidth)
        self.entryWednesday2 = ttk.Entry(FrameWednesdayAdmin, width=entryWidth)
        self.entryWednesday3 = ttk.Entry(FrameWednesdayAdmin, width=entryWidth)
        self.entryWednesday4 = ttk.Entry(FrameWednesdayAdmin, width=entryWidth)
        self.entryWednesday5 = ttk.Entry(FrameWednesdayAdmin, width=entryWidth)
        self.entryWednesday6 = ttk.Entry(FrameWednesdayAdmin, width=entryWidth)

        labelNWednesday.grid(row=0, column=0, columnspan=3, sticky="ew", padx=5, pady=(0, 10))
        label1Wednesday.grid(row=1, column=0, sticky="w", padx=5, pady=2)
        comboboxWednesday1.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        self.entryWednesday1.grid(row=1, column=2, sticky="e", padx=5, pady=2)
        label2Wednesday.grid(row=2, column=0, sticky="w", padx=5, pady=2)
        comboboxWednesday2.grid(row=2, column=1, sticky="ew", padx=5, pady=2)
        self.entryWednesday2.grid(row=2, column=2, sticky="e", padx=5, pady=2)
        label3Wednesday.grid(row=3, column=0, sticky="w", padx=5, pady=2)
        comboboxWednesday3.grid(row=3, column=1, sticky="ew", padx=5, pady=2)
        self.entryWednesday3.grid(row=3, column=2, sticky="e", padx=5, pady=2)
        label4Wednesday.grid(row=4, column=0, sticky="w", padx=5, pady=2)
        comboboxWednesday4.grid(row=4, column=1, sticky="ew", padx=5, pady=2)
        self.entryWednesday4.grid(row=4, column=2, sticky="e", padx=5, pady=2)
        label5Wednesday.grid(row=5, column=0, sticky="w", padx=5, pady=2)
        comboboxWednesday5.grid(row=5, column=1, sticky="ew", padx=5, pady=2)
        self.entryWednesday5.grid(row=5, column=2, sticky="e", padx=5, pady=2)
        label6Wednesday.grid(row=6, column=0, sticky="w", padx=5, pady=2)
        comboboxWednesday6.grid(row=6, column=1, sticky="ew", padx=5, pady=2)
        self.entryWednesday6.grid(row=6, column=2, sticky="e", padx=5, pady=2)
        FrameWednesdayAdmin.grid_columnconfigure(1, weight=1)

        # Четверг
        labelNThursday = ttk.Label(FrameThursdayAdmin, text=" |№|             Lesson             | Mark |")
        label1Thursday = ttk.Label(FrameThursdayAdmin, text="   1")
        label2Thursday = ttk.Label(FrameThursdayAdmin, text="   2")
        label3Thursday = ttk.Label(FrameThursdayAdmin, text="   3")
        label4Thursday = ttk.Label(FrameThursdayAdmin, text="   4")
        label5Thursday = ttk.Label(FrameThursdayAdmin, text="   5")
        label6Thursday = ttk.Label(FrameThursdayAdmin, text="   6")

        self.lessonsThursdayVar1 = StringVar(value=LessonsList[0])
        self.lessonsThursdayVar2 = StringVar(value=LessonsList[0])
        self.lessonsThursdayVar3 = StringVar(value=LessonsList[0])
        self.lessonsThursdayVar4 = StringVar(value=LessonsList[0])
        self.lessonsThursdayVar5 = StringVar(value=LessonsList[0])
        self.lessonsThursdayVar6 = StringVar(value=LessonsList[0])

        comboboxThursday1 = ttk.Combobox(FrameThursdayAdmin, textvariable=self.lessonsThursdayVar1, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxThursday2 = ttk.Combobox(FrameThursdayAdmin, textvariable=self.lessonsThursdayVar2, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxThursday3 = ttk.Combobox(FrameThursdayAdmin, textvariable=self.lessonsThursdayVar3, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxThursday4 = ttk.Combobox(FrameThursdayAdmin, textvariable=self.lessonsThursdayVar4, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxThursday5 = ttk.Combobox(FrameThursdayAdmin, textvariable=self.lessonsThursdayVar5, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxThursday6 = ttk.Combobox(FrameThursdayAdmin, textvariable=self.lessonsThursdayVar6, values=LessonsList,state="readonly", width=comboboxWidth)

        self.entryThursday1 = ttk.Entry(FrameThursdayAdmin, width=entryWidth)
        self.entryThursday2 = ttk.Entry(FrameThursdayAdmin, width=entryWidth)
        self.entryThursday3 = ttk.Entry(FrameThursdayAdmin, width=entryWidth)
        self.entryThursday4 = ttk.Entry(FrameThursdayAdmin, width=entryWidth)
        self.entryThursday5 = ttk.Entry(FrameThursdayAdmin, width=entryWidth)
        self.entryThursday6 = ttk.Entry(FrameThursdayAdmin, width=entryWidth)

        labelNThursday.grid(row=0, column=0, columnspan=3, sticky="ew", padx=5, pady=(0, 10))
        label1Thursday.grid(row=1, column=0, sticky="w", padx=5, pady=2)
        comboboxThursday1.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        self.entryThursday1.grid(row=1, column=2, sticky="e", padx=5, pady=2)

        label2Thursday.grid(row=2, column=0, sticky="w", padx=5, pady=2)
        comboboxThursday2.grid(row=2, column=1, sticky="ew", padx=5, pady=2)
        self.entryThursday2.grid(row=2, column=2, sticky="e", padx=5, pady=2)

        label3Thursday.grid(row=3, column=0, sticky="w", padx=5, pady=2)
        comboboxThursday3.grid(row=3, column=1, sticky="ew", padx=5, pady=2)
        self.entryThursday3.grid(row=3, column=2, sticky="e", padx=5, pady=2
                                 )
        label4Thursday.grid(row=4, column=0, sticky="w", padx=5, pady=2)
        comboboxThursday4.grid(row=4, column=1, sticky="ew", padx=5, pady=2)
        self.entryThursday4.grid(row=4, column=2, sticky="e", padx=5, pady=2)

        label5Thursday.grid(row=5, column=0, sticky="w", padx=5, pady=2)
        comboboxThursday5.grid(row=5, column=1, sticky="ew", padx=5, pady=2)
        self.entryThursday5.grid(row=5, column=2, sticky="e", padx=5, pady=2)

        label6Thursday.grid(row=6, column=0, sticky="w", padx=5, pady=2)
        comboboxThursday6.grid(row=6, column=1, sticky="ew", padx=5, pady=2)
        self.entryThursday6.grid(row=6, column=2, sticky="e", padx=5, pady=2)
        FrameThursdayAdmin.grid_columnconfigure(1, weight=1)

        # Пятница
        labelNFriday = ttk.Label(FrameFridayAdmin, text=" |№|             Lesson             | Mark |")
        label1Friday = ttk.Label(FrameFridayAdmin, text="   1")
        label2Friday = ttk.Label(FrameFridayAdmin, text="   2")
        label3Friday = ttk.Label(FrameFridayAdmin, text="   3")
        label4Friday = ttk.Label(FrameFridayAdmin, text="   4")
        label5Friday = ttk.Label(FrameFridayAdmin, text="   5")
        label6Friday = ttk.Label(FrameFridayAdmin, text="   6")

        self.lessonsFridayVar1 = StringVar(value=LessonsList[0])
        self.lessonsFridayVar2 = StringVar(value=LessonsList[0])
        self.lessonsFridayVar3 = StringVar(value=LessonsList[0])
        self.lessonsFridayVar4 = StringVar(value=LessonsList[0])
        self.lessonsFridayVar5 = StringVar(value=LessonsList[0])
        self.lessonsFridayVar6 = StringVar(value=LessonsList[0])

        comboboxFriday1 = ttk.Combobox(FrameFridayAdmin, textvariable=self.lessonsFridayVar1, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxFriday2 = ttk.Combobox(FrameFridayAdmin, textvariable=self.lessonsFridayVar2, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxFriday3 = ttk.Combobox(FrameFridayAdmin, textvariable=self.lessonsFridayVar3, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxFriday4 = ttk.Combobox(FrameFridayAdmin, textvariable=self.lessonsFridayVar4, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxFriday5 = ttk.Combobox(FrameFridayAdmin, textvariable=self.lessonsFridayVar5, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxFriday6 = ttk.Combobox(FrameFridayAdmin, textvariable=self.lessonsFridayVar6, values=LessonsList,state="readonly", width=comboboxWidth)

        self.entryFriday1 = ttk.Entry(FrameFridayAdmin, width=entryWidth)
        self.entryFriday2 = ttk.Entry(FrameFridayAdmin, width=entryWidth)
        self.entryFriday3 = ttk.Entry(FrameFridayAdmin, width=entryWidth)
        self.entryFriday4 = ttk.Entry(FrameFridayAdmin, width=entryWidth)
        self.entryFriday5 = ttk.Entry(FrameFridayAdmin, width=entryWidth)
        self.entryFriday6 = ttk.Entry(FrameFridayAdmin, width=entryWidth)

        labelNFriday.grid(row=0, column=0, columnspan=3, sticky="ew", padx=5, pady=(0, 10))
        label1Friday.grid(row=1, column=0, sticky="w", padx=5, pady=2)
        comboboxFriday1.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        self.entryFriday1.grid(row=1, column=2, sticky="e", padx=5, pady=2)

        label2Friday.grid(row=2, column=0, sticky="w", padx=5, pady=2)
        comboboxFriday2.grid(row=2, column=1, sticky="ew", padx=5, pady=2)
        self.entryFriday2.grid(row=2, column=2, sticky="e", padx=5, pady=2)

        label3Friday.grid(row=3, column=0, sticky="w", padx=5, pady=2)
        comboboxFriday3.grid(row=3, column=1, sticky="ew", padx=5, pady=2)
        self.entryFriday3.grid(row=3, column=2, sticky="e", padx=5, pady=2)

        label4Friday.grid(row=4, column=0, sticky="w", padx=5, pady=2)
        comboboxFriday4.grid(row=4, column=1, sticky="ew", padx=5, pady=2)
        self.entryFriday4.grid(row=4, column=2, sticky="e", padx=5, pady=2)

        label5Friday.grid(row=5, column=0, sticky="w", padx=5, pady=2)
        comboboxFriday5.grid(row=5, column=1, sticky="ew", padx=5, pady=2)
        self.entryFriday5.grid(row=5, column=2, sticky="e", padx=5, pady=2)

        label6Friday.grid(row=6, column=0, sticky="w", padx=5, pady=2)
        comboboxFriday6.grid(row=6, column=1, sticky="ew", padx=5, pady=2)
        self.entryFriday6.grid(row=6, column=2, sticky="e", padx=5, pady=2)
        FrameFridayAdmin.grid_columnconfigure(1, weight=1)

        # Суббота
        labelNSaturday = ttk.Label(FrameSaturdayAdmin, text=" |№|             Lesson             | Mark |")
        label1Saturday = ttk.Label(FrameSaturdayAdmin, text="   1")
        label2Saturday = ttk.Label(FrameSaturdayAdmin, text="   2")
        label3Saturday = ttk.Label(FrameSaturdayAdmin, text="   3")
        label4Saturday = ttk.Label(FrameSaturdayAdmin, text="   4")
        label5Saturday = ttk.Label(FrameSaturdayAdmin, text="   5")
        label6Saturday = ttk.Label(FrameSaturdayAdmin, text="   6")

        self.lessonsSaturdayVar1 = StringVar(value=LessonsList[0])
        self.lessonsSaturdayVar2 = StringVar(value=LessonsList[0])
        self.lessonsSaturdayVar3 = StringVar(value=LessonsList[0])
        self.lessonsSaturdayVar4 = StringVar(value=LessonsList[0])
        self.lessonsSaturdayVar5 = StringVar(value=LessonsList[0])
        self.lessonsSaturdayVar6 = StringVar(value=LessonsList[0])

        comboboxSaturday1 = ttk.Combobox(FrameSaturdayAdmin, textvariable=self.lessonsSaturdayVar1, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxSaturday2 = ttk.Combobox(FrameSaturdayAdmin, textvariable=self.lessonsSaturdayVar2, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxSaturday3 = ttk.Combobox(FrameSaturdayAdmin, textvariable=self.lessonsSaturdayVar3, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxSaturday4 = ttk.Combobox(FrameSaturdayAdmin, textvariable=self.lessonsSaturdayVar4, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxSaturday5 = ttk.Combobox(FrameSaturdayAdmin, textvariable=self.lessonsSaturdayVar5, values=LessonsList,state="readonly", width=comboboxWidth)
        comboboxSaturday6 = ttk.Combobox(FrameSaturdayAdmin, textvariable=self.lessonsSaturdayVar6, values=LessonsList, state="readonly", width=comboboxWidth)

        self.entrySaturday1 = ttk.Entry(FrameSaturdayAdmin, width=entryWidth)
        self.entrySaturday2 = ttk.Entry(FrameSaturdayAdmin, width=entryWidth)
        self.entrySaturday3 = ttk.Entry(FrameSaturdayAdmin, width=entryWidth)
        self.entrySaturday4 = ttk.Entry(FrameSaturdayAdmin, width=entryWidth)
        self.entrySaturday5 = ttk.Entry(FrameSaturdayAdmin, width=entryWidth)
        self.entrySaturday6 = ttk.Entry(FrameSaturdayAdmin, width=entryWidth)

        labelNSaturday.grid(row=0, column=0, columnspan=3, sticky="ew", padx=5, pady=(0, 10))
        label1Saturday.grid(row=1, column=0, sticky="w", padx=5, pady=2)
        comboboxSaturday1.grid(row=1, column=1, sticky="ew", padx=5, pady=2)

        self.entrySaturday1.grid(row=1, column=2, sticky="e", padx=5, pady=2)
        label2Saturday.grid(row=2, column=0, sticky="w", padx=5, pady=2)
        comboboxSaturday2.grid(row=2, column=1, sticky="ew", padx=5, pady=2)

        self.entrySaturday2.grid(row=2, column=2, sticky="e", padx=5, pady=2)
        label3Saturday.grid(row=3, column=0, sticky="w", padx=5, pady=2)
        comboboxSaturday3.grid(row=3, column=1, sticky="ew", padx=5, pady=2)

        self.entrySaturday3.grid(row=3, column=2, sticky="e", padx=5, pady=2)
        label4Saturday.grid(row=4, column=0, sticky="w", padx=5, pady=2)
        comboboxSaturday4.grid(row=4, column=1, sticky="ew", padx=5, pady=2)

        self.entrySaturday4.grid(row=4, column=2, sticky="e", padx=5, pady=2)
        label5Saturday.grid(row=5, column=0, sticky="w", padx=5, pady=2)
        comboboxSaturday5.grid(row=5, column=1, sticky="ew", padx=5, pady=2)
        self.entrySaturday5.grid(row=5, column=2, sticky="e", padx=5, pady=2)

        label6Saturday.grid(row=6, column=0, sticky="w", padx=5, pady=2)
        comboboxSaturday6.grid(row=6, column=1, sticky="ew", padx=5, pady=2)
        self.entrySaturday6.grid(row=6, column=2, sticky="e", padx=5, pady=2)

        FrameSaturdayAdmin.grid_columnconfigure(1, weight=1)

        # |----------------------------Упаковка----------------------------|

    def GetData(self):

        # Понедельник
        lessonsMonday = [
            ["1", self.lessonsMondayVar1.get() or "", self.entryMonday1.get().strip() or ""],
            ["2", self.lessonsMondayVar2.get() or "", self.entryMonday2.get().strip() or ""],
            ["3", self.lessonsMondayVar3.get() or "", self.entryMonday3.get().strip() or ""],
            ["4", self.lessonsMondayVar4.get() or "", self.entryMonday4.get().strip() or ""],
            ["5", self.lessonsMondayVar5.get() or "", self.entryMonday5.get().strip() or ""],
            ["6", self.lessonsMondayVar6.get() or "", self.entryMonday6.get().strip() or ""],
        ]

        # Вторник
        lessonsTuesday = [
            ["1", self.lessonsTuesdayVar1.get() or "", self.entryTuesday1.get().strip() or ""],
            ["2", self.lessonsTuesdayVar2.get() or "", self.entryTuesday2.get().strip() or ""],
            ["3", self.lessonsTuesdayVar3.get() or "", self.entryTuesday3.get().strip() or ""],
            ["4", self.lessonsTuesdayVar4.get() or "", self.entryTuesday4.get().strip() or ""],
            ["5", self.lessonsTuesdayVar5.get() or "", self.entryTuesday5.get().strip() or ""],
            ["6", self.lessonsTuesdayVar6.get() or "", self.entryTuesday6.get().strip() or ""],
        ]

        # Среда
        lessonsWednesday = [
            ["1", self.lessonsWednesdayVar1.get() or "", self.entryWednesday1.get().strip() or ""],
            ["2", self.lessonsWednesdayVar2.get() or "", self.entryWednesday2.get().strip() or ""],
            ["3", self.lessonsWednesdayVar3.get() or "", self.entryWednesday3.get().strip() or ""],
            ["4", self.lessonsWednesdayVar4.get() or "", self.entryWednesday4.get().strip() or ""],
            ["5", self.lessonsWednesdayVar5.get() or "", self.entryWednesday5.get().strip() or ""],
            ["6", self.lessonsWednesdayVar6.get() or "", self.entryWednesday6.get().strip() or ""],
        ]

        # Четверг
        lessonsThursday = [
            ["1", self.lessonsThursdayVar1.get() or "", self.entryThursday1.get().strip() or ""],
            ["2", self.lessonsThursdayVar2.get() or "", self.entryThursday2.get().strip() or ""],
            ["3", self.lessonsThursdayVar3.get() or "", self.entryThursday3.get().strip() or ""],
            ["4", self.lessonsThursdayVar4.get() or "", self.entryThursday4.get().strip() or ""],
            ["5", self.lessonsThursdayVar5.get() or "", self.entryThursday5.get().strip() or ""],
            ["6", self.lessonsThursdayVar6.get() or "", self.entryThursday6.get().strip() or ""],
        ]

        # Пятница
        lessonsFriday = [
            ["1", self.lessonsFridayVar1.get() or "", self.entryFriday1.get().strip() or ""],
            ["2", self.lessonsFridayVar2.get() or "", self.entryFriday2.get().strip() or ""],
            ["3", self.lessonsFridayVar3.get() or "", self.entryFriday3.get().strip() or ""],
            ["4", self.lessonsFridayVar4.get() or "", self.entryFriday4.get().strip() or ""],
            ["5", self.lessonsFridayVar5.get() or "", self.entryFriday5.get().strip() or ""],
            ["6", self.lessonsFridayVar6.get() or "", self.entryFriday6.get().strip() or ""],
        ]

        # Суббота
        lessonsSaturday = [
            ["1", self.lessonsSaturdayVar1.get() or "", self.entrySaturday1.get().strip() or ""],
            ["2", self.lessonsSaturdayVar2.get() or "", self.entrySaturday2.get().strip() or ""],
            ["3", self.lessonsSaturdayVar3.get() or "", self.entrySaturday3.get().strip() or ""],
            ["4", self.lessonsSaturdayVar4.get() or "", self.entrySaturday4.get().strip() or ""],
            ["5", self.lessonsSaturdayVar5.get() or "", self.entrySaturday5.get().strip() or ""],
            ["6", self.lessonsSaturdayVar6.get() or "", self.entrySaturday6.get().strip() or ""],
        ]

        # Сохраняем всё в словарь
        self.all_schedule = {
            "Monday": lessonsMonday,
            "Tuesday": lessonsTuesday,
            "Wednesday": lessonsWednesday,
            "Thursday": lessonsThursday,
            "Friday": lessonsFriday,
            "Saturday": lessonsSaturday,
        }

        for item in TreeMonday.get_children():
            TreeMonday.delete(item)

        for item in TreeTuesday.get_children():
            TreeTuesday.delete(item)

        for item in TreeWednesday.get_children():
            TreeWednesday.delete(item)

        for item in TreeThursday.get_children():
            TreeThursday.delete(item)

        for item in TreeFriday.get_children():
            TreeFriday.delete(item)

        for item in TreeSaturday.get_children():
            TreeSaturday.delete(item)


        for row in lessonsMonday:
            TreeMonday.insert("", "end", values=row)
        TreeMonday.pack(expand=1, anchor="center")

        for row in lessonsTuesday:
            TreeTuesday.insert("", "end", values=row)
        TreeTuesday.pack(expand=1, anchor="center")

        for row in lessonsWednesday:
            TreeWednesday.insert("", "end", values=row)
        TreeWednesday.pack(expand=1, anchor="center")

        for row in lessonsThursday:
            TreeThursday.insert("", "end", values=row)
        TreeThursday.pack(expand=1, anchor="center")

        for row in lessonsFriday:
            TreeFriday.insert("", "end", values=row)
        TreeFriday.pack(expand=1, anchor="center")

        for row in lessonsSaturday:
            TreeSaturday.insert("", "end", values=row)
        TreeSaturday.pack(expand=1, anchor="center")

def OpenAdminPanel():
    AdminPanel()

#Панель где будут выставлятся уроки и оценки
AdminPanelButton = ttk.Button(FrameTools,text='Admin panel',width=80, command=OpenAdminPanel)
AdminPanelButton.pack(anchor="nw")

root.minsize(700,800)
#root.maxsize(700,800)
root.mainloop()

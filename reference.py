import tkinter 
import tkinter.messagebox
import tkinter.ttk

root = tkinter.Tk()
root.title('参考文献格式生成器') #标题

root['height'] = 270 #窗口高度
root['width'] = 840  #窗口宽度

class EntryWithPlaceholder(tkinter.Entry):#Placeholder功能模块
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey',):
        super().__init__(master)#Placeholder默认值"PLACEHOLDER"，默认颜色灰色

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in) #绑定鼠标点入操作
        self.bind("<FocusOut>", self.foc_out)#绑定鼠标点出操作

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get(): #如果Entry没有得到值
            self.put_placeholder()#那么将默认值放上去

def Pagesaregood(Page_1st,Page_2nd):#检查页码是否正确
    global result,Formatofcreate
    if (Page_1st=='起始页' or Page_1st=='') and (Page_2nd=='终止页' or Page_2nd==''):
    #防止此时光标刚好停在文本框，而此时又没有数据写入，故有空字符串，下同理，不赘述
        tkinter.messagebox.showinfo(title='Error!',message='请至少输入一页！')
        Formatofcreate=1
    elif (Page_1st=='起始页' or Page_1st=='') and (Page_2nd!='终止页' and Page_2nd!=''):
        result+=Page_2nd+'.'
    elif (Page_1st!='起始页' and Page_1st!='') and (Page_2nd=='终止页' or Page_2nd==''):
        result+=Page_1st+'.'
    elif (Page_1st!='起始页' and Page_1st!='') and (Page_2nd!='终止页' and Page_2nd!=''):
        if str.isdigit(Page_1st)==True and str.isdigit(Page_2nd)==True :
        #如果页码都是数字，那么比较前后两个数字，合理才能输入
            if int(Page_1st)>int(Page_2nd):
                tkinter.messagebox.showinfo(title='Error!',message='请输入正确的起止页！')
                Formatofcreate=1
            elif int(Page_1st)==int(Page_2nd):
                result+=Page_1st+'.'
            elif int(Page_1st)<int(Page_2nd):
                result+=Page_1st+'-'+Page_2nd+'.'
        else:
        #如果页码存在字母或者其他特殊字符，那么不比较（前言、扉页等处）
            if Page_1st==Page_2nd:
                result+=Page_1st+'.'
            else:
                result+=Page_1st+'-'+Page_2nd+'.'
                
def doallentry():#全做一遍，防止Entry重叠引起输入错误
    Journal();
    Monograph();
    Dissertation();
    Symposium();
    Report();
    Patent();
    Standard();
    Newspaper();
    EBOL();
    Others();
    
def forgetallentry():#清屏，防止Entry占屏幕引起程序错误
    #Journal 20个
    labelJournalLocation.place_forget()
    buttonJournalEmpty.place_forget()
    labelJournalAuthor.place_forget()
    entryJournalAuthor.place_forget()
    labelJournalTitle.place_forget()
    entryJournalTitle.place_forget()
    labelJournalName.place_forget()
    entryJournalName.place_forget()
    labelJournalYear.place_forget()
    entryJournalYear.place_forget()
    labelJournalVolume.place_forget()
    entryJournalVolume.place_forget()
    labelJournalPages.place_forget()
    labelJournal_Pages.place_forget()
    entryJournalPages_1st.place_forget()
    entryJournalPages_2nd.place_forget()
    labelJournalPeriod.place_forget()
    entryJournalPeriod.place_forget()
    buttonJournalCreate.place_forget()
    buttonJournalHelp.place_forget()
    
    #Monograph 18个
    labelMonographLocation.place_forget()
    buttonMonographEmpty.place_forget()
    labelMonographAuthor.place_forget()
    entryMonographAuthor.place_forget()
    labelMonographTitle.place_forget()
    entryMonographTitle.place_forget()
    labelMonographPress.place_forget()
    entryMonographPress.place_forget()
    labelMonographArea.place_forget()
    labelMonographYear.place_forget()
    entryMonographYear.place_forget()
    entryMonographArea.place_forget()
    labelMonographPages.place_forget()
    labelMonograph_Pages.place_forget()
    entryMonographPages_1st.place_forget()
    entryMonographPages_2nd.place_forget()
    buttonMonographCreate.place_forget()
    buttonMonographHelp.place_forget()

    #Dissertation 14个
    labelDissertationLocation.place_forget()
    buttonDissertationEmpty.place_forget()
    labelDissertationAuthor.place_forget()
    entryDissertationAuthor.place_forget()
    labelDissertationTitle.place_forget()
    entryDissertationTitle.place_forget()
    labelDissertationPress.place_forget()
    entryDissertationPress.place_forget()
    labelDissertationArea.place_forget()
    labelDissertationYear.place_forget()
    entryDissertationYear.place_forget()
    entryDissertationArea.place_forget()
    buttonDissertationCreate.place_forget()
    buttonDissertationHelp.place_forget()

    #Symposium 20个
    labelSymposiumLocation.place_forget()
    buttonSymposiumEmpty.place_forget()
    labelSymposiumAuthor.place_forget()
    entrySymposiumAuthor.place_forget()
    labelSymposiumTitle.place_forget()
    entrySymposiumTitle.place_forget()
    labelSymposiumName.place_forget()
    entrySymposiumName.place_forget()
    labelSymposiumPress.place_forget()
    entrySymposiumPress.place_forget()
    labelSymposiumArea.place_forget()
    entrySymposiumArea.place_forget()
    labelSymposiumPages.place_forget()
    labelSymposium_Pages.place_forget()
    entrySymposiumPages_1st.place_forget()
    entrySymposiumPages_2nd.place_forget()
    labelSymposiumYear.place_forget()
    entrySymposiumYear.place_forget()
    buttonSymposiumCreate.place_forget()
    buttonSymposiumHelp.place_forget()

    #Report 14个
    labelReportLocation.place_forget()
    buttonReportEmpty.place_forget()
    labelReportAuthor.place_forget()
    entryReportAuthor.place_forget()
    labelReportTitle.place_forget()
    entryReportTitle.place_forget()
    labelReportArea.place_forget()
    entryReportArea.place_forget()
    labelReportOrg.place_forget()
    entryReportOrg.place_forget()
    labelReportYear.place_forget()
    entryReportYear.place_forget()
    buttonReportCreate.place_forget()
    buttonReportHelp.place_forget()

    #Patent 14个
    labelPatentLocation.place_forget()
    buttonPatentEmpty.place_forget()
    labelPatentAuthor.place_forget()
    entryPatentAuthor.place_forget()
    labelPatentTitle.place_forget()
    entryPatentTitle.place_forget()
    labelPatentCoun.place_forget()
    entryPatentCoun.place_forget()
    labelPatentNum.place_forget()
    entryPatentNum.place_forget()
    labelPatentDate.place_forget()
    entryPatentDate.place_forget()
    buttonPatentCreate.place_forget()
    buttonPatentHelp.place_forget()

    #Standard 13个
    labelStandardLocation.place_forget()
    buttonStandardEmpty.place_forget()
    labelStandardNum.place_forget()
    entryStandardNum.place_forget()
    labelStandardTitle.place_forget()
    entryStandardTitle.place_forget()
    labelStandardArea.place_forget()
    entryStandardArea.place_forget()
    labelStandardAuthor.place_forget()
    entryStandardAuthor.place_forget()
    labelStandardYear.place_forget()
    entryStandardYear.place_forget()
    buttonStandardCreate.place_forget()

    #Newspaper 13个
    labelNewspaperLocation.place_forget()
    buttonNewspaperEmpty.place_forget()
    labelNewspaperAuthor.place_forget()
    entryNewspaperAuthor.place_forget()
    labelNewspaperTitle.place_forget()
    entryNewspaperTitle.place_forget()
    labelNewspaperName.place_forget()
    entryNewspaperName.place_forget()
    labelNewspaperDate.place_forget()
    entryNewspaperDate.place_forget()
    labelNewspaperLayout.place_forget()
    entryNewspaperLayout.place_forget()
    buttonNewspaperCreate.place_forget()

    #EBOL 14个
    labelEBOLLocation.place_forget()
    buttonEBOLEmpty.place_forget()
    labelEBOLAuthor.place_forget()
    entryEBOLAuthor.place_forget()
    labelEBOLTitle.place_forget()
    entryEBOLTitle.place_forget()
    labelEBOLAdd.place_forget()
    entryEBOLAdd.place_forget()
    labelEBOLDate.place_forget()
    entryEBOLDate.place_forget()
    labelEBOLType.place_forget()
    entryEBOLType.place_forget()
    buttonEBOLCreate.place_forget()
    buttonEBOLHelp.place_forget()

    #Others 14个
    labelOthersLocation.place_forget()
    buttonOthersEmpty.place_forget()
    labelOthersAuthor.place_forget()
    entryOthersAuthor.place_forget()
    labelOthersTitle.place_forget()
    entryOthersTitle.place_forget()
    labelOthersArea.place_forget()
    entryOthersArea.place_forget()
    labelOthersOrg.place_forget()
    entryOthersOrg.place_forget()
    labelOthersYear.place_forget()
    entryOthersYear.place_forget()
    buttonOthersCreate.place_forget()
    buttonOthersHelp.place_forget()

def AuthorNameinput():#输入作者姓名，三个及三个以上只写前三个
    global AuthorName,result

    if len(AuthorName)==1:
        result=AuthorName[0]+'.'
    elif len(AuthorName)==2:
        result=AuthorName[0]+','+AuthorName[1]+'.'
    elif len(AuthorName)==3:
        result=AuthorName[0]+','+AuthorName[1]+','+AuthorName[2]+'.'
    else:
        result=AuthorName[0]+','+AuthorName[1]+','+AuthorName[2]+'等.'
        
def JournalEmpty():#清空期刊论文[J]表单并恢复注释
    entryJournalAuthor.delete(0,'end')
    entryJournalTitle.delete(0,'end')
    entryJournalName.delete(0,'end')
    entryJournalYear.delete(0,'end')
    entryJournalVolume.delete(0,'end')
    entryJournalPages_1st.delete(0,'end')
    entryJournalPages_2nd.delete(0,'end')
    entryJournalPeriod.delete(0,'end')
    
    entryJournalAuthor.put_placeholder()#为了恢复注释，以下所有××Empty函数略去该解释
    entryJournalTitle.put_placeholder()
    entryJournalName.put_placeholder()
    entryJournalYear.put_placeholder()
    entryJournalVolume.put_placeholder()
    entryJournalPages_1st.put_placeholder()
    entryJournalPages_2nd.put_placeholder()
    entryJournalPeriod.put_placeholder()
        
def JournalCreate():#生成期刊论文[J]参考文献格式
    global result,AuthorName,Formatofcreate
    AuthorName=entryJournalAuthor.get().split(',')#将作者按英文逗号分隔，写入列表
    Formatofcreate=0 #布尔变量判断格式是否正确，为1禁止输入
    
    if entryJournalAuthor.get()=='多个姓名以英文逗号隔开' or entryJournalAuthor.get()=='':
        #防止此时光标刚好停在文本框，而此时又没有数据写入，故有空字符串，下同理，不赘述
        tkinter.messagebox.showinfo(title='Error!',message='请输入作者名称！')
        Formatofcreate=1
    if entryJournalTitle.get()=='请输入文章标题' or entryJournalTitle.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入文章标题！')
        Formatofcreate=1
    if entryJournalName.get()=='请输入期刊名称' or entryJournalName.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入期刊名称！')
        Formatofcreate=1
    if entryJournalYear.get()=='年份,如2007' or entryJournalYear.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入期刊发行年份！')
        Formatofcreate=1
    if entryJournalPeriod.get()=='期' or entryJournalPeriod.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入文章所在期刊期数！')
        Formatofcreate=1

    AuthorNameinput()#调用输入作者姓名的函数
    
    result+=entryJournalTitle.get()+'[J].'
    result+=entryJournalName.get()+','
    result+=entryJournalYear.get()+','
    
    if entryJournalVolume.get()=='卷（可缺省）' or entryJournalVolume.get()=='':#可缺省条件单独判断
        result+=entryJournalPeriod.get()+':'
    else:
        result+=entryJournalVolume.get()+'('+entryJournalPeriod.get()+'):'
        
    Page_1st=entryJournalPages_1st.get()
    Page_2nd=entryJournalPages_2nd.get()
    Pagesaregood(Page_1st,Page_2nd) #调用判断页码是否合法的函数
    
    if Formatofcreate==0:
        listboxRef.insert(tkinter.END,result) #将结果插入listbox
    else:
        Formatofcreate=0 #如果有错误，结果不能插入，同时将格式置为0，下次重新判断
        
def JournalHelp():#帮助按钮
    Tips='(1)如该文献为网络文献，将[J]改为[J/OL],在最后的\'.\'后添加文献所在网址，如：\n李炳穆,韩国图书馆法[J/OL].图书情报工作,2008,52(6);6-12[2013-10-25].http://www.docin.com/p-400265742.html.\n(2)如有DOI号码，一并在后标注，如:\n WALLS S C, BARICHIVICH W J, BROWN M E. Drought, deluge and declines: the impact of precipitation extremes on amphibians in a changing climate [J/OL]. Biology, 2013,2(1):399-418[2013-11-04].http://www.mdpi.com/2079-7737/2/1/399.DOI:10.3390/biology2010399.'
    tkinter.messagebox.showinfo(title='提示',message=Tips)

def Journal():#Journal是默认值，期刊论文[J]
    global labelJournalLocation
    labelJournalLocation = tkinter.Label(root,text='当前参考文献格式位置：期刊论文'
                                  ,justify=tkinter.RIGHT,width=150)
    labelJournalLocation.place(x=15,y=40,width=180,height=20)
    
    global labelJournalAuthor
    labelJournalAuthor = tkinter.Label(root,text='作   者：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelJournalAuthor.place(x=9,y=70,width=50,height=20)
    global entryJournalAuthor
    entryJournalAuthor = EntryWithPlaceholder(root, "多个姓名以英文逗号隔开")
    entryJournalAuthor.place(x=60,y=70,width=250,height=20)
    global labelJournalTitle
    labelJournalTitle = tkinter.Label(root,text='标   题：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelJournalTitle.place(x=9,y=100,width=50,height=20)
    global entryJournalTitle
    entryJournalTitle = EntryWithPlaceholder(root,"请输入文章标题")
    entryJournalTitle.place(x=60,y=100,width=250,height=20)
    global labelJournalName
    labelJournalName = tkinter.Label(root,text='期刊名：',justify=tkinter.RIGHT,width=150,fg='blue')
    labelJournalName.place(x=10,y=130,width=50,height=20)
    global entryJournalName
    entryJournalName = EntryWithPlaceholder(root, "请输入期刊名称")
    entryJournalName.place(x=60,y=130,width=250,height=20)
    global labelJournalYear
    labelJournalYear = tkinter.Label(root,text='期刊年份：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelJournalYear.place(x=9,y=160,width=65,height=20)
    global entryJournalYear
    entryJournalYear = EntryWithPlaceholder(root,"年份,如2007")
    entryJournalYear.place(x=75,y=160,width=100,height=20)
    global labelJournalVolume
    labelJournalVolume = tkinter.Label(root,text='卷：',justify=tkinter.RIGHT,width=30,fg='blue')
    labelJournalVolume.place(x=180,y=160,width=30,height=20)
    global entryJournalVolume
    entryJournalVolume = EntryWithPlaceholder(root,"卷（可缺省）")
    entryJournalVolume.place(x=210,y=160,width=100,height=20)
    global labelJournalPages
    labelJournalPages = tkinter.Label(root,text='起止页：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelJournalPages.place(x=9,y=190,width=50,height=20)
    global labelJournal_Pages
    labelJournal_Pages = tkinter.Label(root,text='~',justify=tkinter.RIGHT,width=10,fg='blue')
    labelJournal_Pages.place(x=108,y=190,width=20,height=20)
    global entryJournalPages_1st
    entryJournalPages_1st = EntryWithPlaceholder(root,"起始页")
    entryJournalPages_1st.place(x=60,y=190,width=50,height=20)
    global entryJournalPages_2nd
    entryJournalPages_2nd = EntryWithPlaceholder(root,"终止页")
    entryJournalPages_2nd.place(x=125,y=190,width=50,height=20)
    global labelJournalPeriod
    labelJournalPeriod = tkinter.Label(root,text='期：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelJournalPeriod.place(x=180,y=190,width=30,height=20)
    global entryJournalPeriod
    entryJournalPeriod = EntryWithPlaceholder(root,"期")
    entryJournalPeriod.place(x=210,y=190,width=100,height=20)
    global buttonJournalCreate
    buttonJournalCreate = tkinter.Button(root,text='生成参考文献格式',width=20,height=1,command=JournalCreate)
    buttonJournalCreate.place(x=90,y=220)
    global buttonJournalHelp
    buttonJournalHelp = tkinter.Button(root,text='?',width=3,height=1,command=JournalHelp)
    buttonJournalHelp.place(x=275,y=220)
    global buttonJournalEmpty
    buttonJournalEmpty=tkinter.Button(root,text='清空表单',width=6,height=1,command=JournalEmpty)
    buttonJournalEmpty.place(x=258,y=35)
    
def MonographEmpty():#清空图书/专著[M]表单并恢复注释
    entryMonographAuthor.delete(0,'end')
    entryMonographTitle.delete(0,'end')
    entryMonographPress.delete(0,'end')
    entryMonographYear.delete(0,'end')
    entryMonographArea.delete(0,'end')
    entryMonographPages_1st.delete(0,'end')
    entryMonographPages_2nd.delete(0,'end')
    entryMonographAuthor.put_placeholder()
    entryMonographTitle.put_placeholder()
    entryMonographPress.put_placeholder()
    entryMonographYear.put_placeholder()
    entryMonographArea.put_placeholder()
    entryMonographPages_1st.put_placeholder()
    entryMonographPages_2nd.put_placeholder()


def MonographCreate():#生成图书/专著[M]参考文献格式
    global result,AuthorName,Formatofcreate
    AuthorName=entryMonographAuthor.get().split(',')#将作者按英文逗号分隔，写入列表
    Formatofcreate=0 #布尔变量判断格式是否正确，为1禁止输入
    
    if entryMonographAuthor.get()=='多个姓名以英文逗号隔开' or entryMonographAuthor.get()=='':
        #防止此时光标刚好停在文本框，而此时又没有数据写入，故有空字符串，下同理，不赘述
        tkinter.messagebox.showinfo(title='Error!',message='请输入作者名称！')
        Formatofcreate=1
    if entryMonographTitle.get()=='请输入书籍名称' or entryMonographTitle.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入书籍名称！')
        Formatofcreate=1
    if entryMonographPress.get()=='请输入出版社名称' or entryMonographPress.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入出版社名称！')
        Formatofcreate=1
    if entryMonographYear.get()=='出版的年份' or entryMonographYear.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入书籍发行年份！')
        Formatofcreate=1
    if entryMonographArea.get()=='出版社所在地' or entryMonographArea.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入书籍出版社所在地！')
        Formatofcreate=1

    AuthorNameinput()
    
    result+=entryMonographTitle.get()+'[M].'
    result+=entryMonographPress.get()+':'
    result+=entryMonographArea.get()+','
    result+=entryMonographYear.get()+':'
        
    Page_1st=entryMonographPages_1st.get()
    Page_2nd=entryMonographPages_2nd.get()
    Pagesaregood(Page_1st,Page_2nd)
    
    if Formatofcreate==0:
        listboxRef.insert(tkinter.END,result)
    else:
        Formatofcreate=0
        
def MonographHelp():#帮助按钮
    Tips='(1)专著中析出的文献请到GB/T 7714-2015中寻找表示方法；\n(2)如书名有第×册，第×版等其他题名信息，在书名后加\':其他题名信息\'，如：\n师伏堂日记:第4册[M].北京:北京图书馆出版社,2009:155\n(3)如有译者信息，在\'[M].\'后添加，如：\n库恩,科学革命的结构:第4版[M].金吾伦,胡新和,译.2版,北京:北京大学出版社,2012.\n(4)电子图书及专著的表示方法与电子期刊类似，如：\n侯文顺.高分子物理:高分子材料分析、选择与改性[M/OL].北京:化学工业出版社,2010:119[2012-11-27].http://apabi.lib.pku.edu.cn/usp/pku/pub.mvc?pid=book.detail&metaid=m.20111114-HGS-889-0228'
    tkinter.messagebox.showinfo(title='提示',message=Tips)

def Monograph():#图书/专著[M]
    global labelMonographLocation
    labelMonographLocation = tkinter.Label(root,text='当前参考文献格式位置：图书/专著'
                                  ,justify=tkinter.RIGHT,width=185)
    labelMonographLocation.place(x=15,y=40,width=185,height=20)
    global buttonMonographEmpty
    buttonMonographEmpty=tkinter.Button(root,text='清空表单',width=6,height=1,command=MonographEmpty)
    buttonMonographEmpty.place(x=258,y=35)
    global labelMonographAuthor
    labelMonographAuthor = tkinter.Label(root,text='作   者：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelMonographAuthor.place(x=9,y=70,width=50,height=20)
    global entryMonographAuthor
    entryMonographAuthor = EntryWithPlaceholder(root, "多个姓名以英文逗号隔开")
    entryMonographAuthor.place(x=60,y=70,width=250,height=20)
    global labelMonographTitle
    labelMonographTitle = tkinter.Label(root,text='书   名：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelMonographTitle.place(x=9,y=100,width=50,height=20)
    global entryMonographTitle
    entryMonographTitle = EntryWithPlaceholder(root,"请输入书籍名称")
    entryMonographTitle.place(x=60,y=100,width=250,height=20)
    global labelMonographPress
    labelMonographPress = tkinter.Label(root,text='出版社名：',justify=tkinter.RIGHT,width=150,fg='blue')
    labelMonographPress.place(x=9,y=130,width=65,height=20)
    global entryMonographPress
    entryMonographPress = EntryWithPlaceholder(root, "请输入出版社名称")
    entryMonographPress.place(x=75,y=130,width=235,height=20)
    global labelMonographArea
    labelMonographArea = tkinter.Label(root,text='出版地区：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelMonographArea.place(x=9,y=160,width=65,height=20)
    global labelMonographYear
    labelMonographYear = tkinter.Label(root,text='出版年份：',justify=tkinter.RIGHT,width=65,fg='blue')
    labelMonographYear.place(x=180,y=160,width=65,height=20)
    global entryMonographYear
    entryMonographYear = EntryWithPlaceholder(root, "出版的年份")
    entryMonographYear.place(x=242,y=160,width=68,height=20)
    global entryMonographArea
    entryMonographArea = EntryWithPlaceholder(root,"出版社所在地")
    entryMonographArea.place(x=75,y=160,width=100,height=20)
    global labelMonographPages
    labelMonographPages = tkinter.Label(root,text='起止页：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelMonographPages.place(x=9,y=190,width=50,height=20)
    global labelMonograph_Pages
    labelMonograph_Pages = tkinter.Label(root,text='~',justify=tkinter.RIGHT,width=10,fg='blue')
    labelMonograph_Pages.place(x=108,y=190,width=20,height=20)
    global entryMonographPages_1st
    entryMonographPages_1st = EntryWithPlaceholder(root,"起始页")
    entryMonographPages_1st.place(x=60,y=190,width=50,height=20)
    global entryMonographPages_2nd
    entryMonographPages_2nd = EntryWithPlaceholder(root,"终止页")
    entryMonographPages_2nd.place(x=125,y=190,width=50,height=20)
    global buttonMonographCreate
    buttonMonographCreate = tkinter.Button(root,text='生成参考文献格式',width=20,height=1,command=MonographCreate)
    buttonMonographCreate.place(x=90,y=220)
    global buttonMonographHelp
    buttonMonographHelp = tkinter.Button(root,text='?',width=3,height=1,command=MonographHelp)
    buttonMonographHelp.place(x=275,y=220)

def DissertationEmpty():#清空学位论文/毕业论文[D]表单并恢复注释
    entryDissertationAuthor.delete(0,'end')
    entryDissertationPress.delete(0,'end')
    entryDissertationTitle.delete(0,'end')
    entryDissertationYear.delete(0,'end')
    entryDissertationArea.delete(0,'end')
    
    entryDissertationAuthor.put_placeholder()
    entryDissertationPress.put_placeholder()
    entryDissertationTitle.put_placeholder()
    entryDissertationYear.put_placeholder()
    entryDissertationArea.put_placeholder()

def DissertationCreate():#生成学位论文/毕业论文[D]参考文献格式
    global result,Formatofcreate
    Formatofcreate=0 #布尔变量判断格式是否正确，为1禁止输入
    
    if entryDissertationAuthor.get()=='请输入学位论文作者' or entryDissertationAuthor.get()=='':
        #防止此时光标刚好停在文本框，而此时又没有数据写入，故有空字符串，下同理，不赘述
        tkinter.messagebox.showinfo(title='Error!',message='请输入学位论文作者名称！')
        Formatofcreate=1
    if entryDissertationTitle.get()=='请输入学位论文标题' or entryDissertationTitle.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入学位论文标题！')
        Formatofcreate=1
    if entryDissertationPress.get()=='请输入保存的单位名称' or entryDissertationPress.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入保存的单位名称！')
        Formatofcreate=1
    if entryDissertationYear.get()=='发表的年份' or entryDissertationYear.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入论文发表年份！')
        Formatofcreate=1
    if entryDissertationArea.get()=='单位所在地区' or entryDissertationArea.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入单位所在地区！')
        Formatofcreate=1

    result=entryDissertationAuthor.get()+'.'
    #学位论文/毕业论文都是单人撰写，所以不需要调用AuthorNameinput函数
    result+=entryDissertationTitle.get()+'[D].'
    result+=entryDissertationArea.get()+':'
    result+=entryDissertationPress.get()+','
    result+=entryDissertationYear.get()+'.'
        
    if Formatofcreate==0:
        listboxRef.insert(tkinter.END,result)
    else:
        Formatofcreate=0

def DissertationHelp():#帮助按钮
    Tips='电子学位论文表示与电子期刊文献表示类似，如：\n吴云芳.面向中文信息处理的现代汉语并列结构研究[D/OL].北京:北京大学,2003[2013-10-14].http://thesis.lib.pku.edu.cn/dlib/list.asp?lang=gb&type=Reader&DocGroupID=4&DocID=6328.'
    tkinter.messagebox.showinfo(title='提示',message=Tips)
    
def Dissertation():#学位论文/毕业论文[D]
    global labelDissertationLocation
    labelDissertationLocation = tkinter.Label(root,text='当前参考文献格式位置：学位论文'
                                  ,justify=tkinter.RIGHT,width=185)
    labelDissertationLocation.place(x=15,y=40,width=185,height=20)
    global buttonDissertationEmpty
    buttonDissertationEmpty=tkinter.Button(root,text='清空表单',width=6,height=1,command=DissertationEmpty)
    buttonDissertationEmpty.place(x=258,y=35)
    global labelDissertationAuthor
    labelDissertationAuthor = tkinter.Label(root,text='作   者：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelDissertationAuthor.place(x=9,y=70,width=50,height=20)
    global entryDissertationAuthor
    entryDissertationAuthor = EntryWithPlaceholder(root, "请输入学位论文作者")
    entryDissertationAuthor.place(x=60,y=70,width=250,height=20)
    global labelDissertationTitle
    labelDissertationTitle = tkinter.Label(root,text='标   题：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelDissertationTitle.place(x=9,y=100,width=50,height=20)
    global entryDissertationTitle
    entryDissertationTitle = EntryWithPlaceholder(root,"请输入学位论文标题")
    entryDissertationTitle.place(x=60,y=100,width=250,height=20)
    global labelDissertationPress
    labelDissertationPress = tkinter.Label(root,text='保存单位：',justify=tkinter.RIGHT,width=150,fg='blue')
    labelDissertationPress.place(x=9,y=130,width=65,height=20)
    global entryDissertationPress
    entryDissertationPress = EntryWithPlaceholder(root, "请输入保存的单位名称")
    entryDissertationPress.place(x=75,y=130,width=235,height=20)
    global labelDissertationArea
    labelDissertationArea = tkinter.Label(root,text='所属地区：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelDissertationArea.place(x=9,y=160,width=65,height=20)
    global labelDissertationYear
    labelDissertationYear = tkinter.Label(root,text='发表年份：',justify=tkinter.RIGHT,width=65,fg='blue')
    labelDissertationYear.place(x=180,y=160,width=65,height=20)
    global entryDissertationYear
    entryDissertationYear = EntryWithPlaceholder(root, "发表的年份")
    entryDissertationYear.place(x=242,y=160,width=68,height=20)
    global entryDissertationArea
    entryDissertationArea = EntryWithPlaceholder(root,"单位所在地区")
    entryDissertationArea.place(x=75,y=160,width=100,height=20)
    global buttonDissertationCreate
    buttonDissertationCreate = tkinter.Button(root,text='生成参考文献格式',width=20,height=1,command=DissertationCreate)
    buttonDissertationCreate.place(x=90,y=220)
    global buttonDissertationHelp
    buttonDissertationHelp = tkinter.Button(root,text='?',width=3,height=1,command=DissertationHelp)
    buttonDissertationHelp.place(x=275,y=220)

def SymposiumEmpty():#清空论文集、会议论文[C]表单并恢复注释
    entrySymposiumAuthor.delete(0,'end')
    entrySymposiumTitle.delete(0,'end')
    entrySymposiumName.delete(0,'end')
    entrySymposiumPress.delete(0,'end')
    entrySymposiumArea.delete(0,'end')
    entrySymposiumPages_1st.delete(0,'end')
    entrySymposiumPages_2nd.delete(0,'end')
    entrySymposiumYear.delete(0,'end')

    entrySymposiumAuthor.put_placeholder()
    entrySymposiumTitle.put_placeholder()
    entrySymposiumName.put_placeholder()
    entrySymposiumPress.put_placeholder()
    entrySymposiumArea.put_placeholder()
    entrySymposiumPages_1st.put_placeholder()
    entrySymposiumPages_2nd.put_placeholder()
    entrySymposiumYear.put_placeholder()

def SymposiumCreate():#生成论文集、会议论文[C]参考文献格式
    global result,AuthorName,Formatofcreate
    AuthorName=entrySymposiumAuthor.get().split(',')#将作者按英文逗号分隔，写入列表
    Formatofcreate=0 #布尔变量判断格式是否正确，为1禁止输入
    
    if entrySymposiumAuthor.get()=='多个姓名以英文逗号隔开' or entrySymposiumAuthor.get()=='':
        #防止此时光标刚好停在文本框，而此时又没有数据写入，故有空字符串，下同理，不赘述
        tkinter.messagebox.showinfo(title='Error!',message='请输入作者名称！')
        Formatofcreate=1
    if entrySymposiumTitle.get()=='请输入论文标题' or entrySymposiumTitle.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入文章标题！')
        Formatofcreate=1
    if entrySymposiumName.get()=='请输入论文集名称' or entrySymposiumName.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入论文集名称！')
        Formatofcreate=1
    if entrySymposiumYear.get()=='出版的年份' or entrySymposiumYear.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入论文集发行年份！')
        Formatofcreate=1
    if entrySymposiumPress.get()=='出版机构名称' or entrySymposiumPress.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入出版机构名称！')
        Formatofcreate=1
    if entrySymposiumArea.get()=='机构所在地' or entrySymposiumArea.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入出版机构所在地！')
        Formatofcreate=1

    AuthorNameinput()
    
    result+=entrySymposiumTitle.get()+'[C].'
    result+=entrySymposiumName.get()+'.'
    result+=entrySymposiumArea.get()+':'
    result+=entrySymposiumPress.get()+','
    result+=entrySymposiumYear.get()+'.'
        
    Page_1st=entrySymposiumPages_1st.get()
    Page_2nd=entrySymposiumPages_2nd.get()
    Pagesaregood(Page_1st,Page_2nd)
    
    if Formatofcreate==0:
        listboxRef.insert(tkinter.END,result)
    else:
        Formatofcreate=0

def SymposiumHelp():#帮助按钮
    Tips='(1)全体论文集应用[G]表示，如：\n中国职工教育研究会.职工教育研究论文集[G].北京:人民教育出版社,1985.\n(2)电子会议论文等表示方法与电子期刊文献类似，如：\n陈志勇.中国财税文化价值研究:“中国财税文化国际学术研讨会”论文集[C/OL].北京:经济科学出版社,2011[2013-10-141.http://apabi.lib.pku.edu.cn/usp/pku/pub.mvc?pid=book.detail&metaid=m.20110628-BPO-889-0135&cult=CN'
    tkinter.messagebox.showinfo(title='提示',message=Tips)

def Symposium():#论文集、会议论文[C]
    global labelSymposiumLocation
    labelSymposiumLocation = tkinter.Label(root,text='当前参考文献格式位置：论 文 集'
                                  ,justify=tkinter.RIGHT,width=150)
    labelSymposiumLocation.place(x=15,y=40,width=180,height=20)
    global buttonSymposiumEmpty
    buttonSymposiumEmpty=tkinter.Button(root,text='清空表单',width=6,height=1,command=SymposiumEmpty)
    buttonSymposiumEmpty.place(x=258,y=35)
    global labelSymposiumAuthor
    labelSymposiumAuthor = tkinter.Label(root,text='作   者：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelSymposiumAuthor.place(x=9,y=70,width=50,height=20)
    global entrySymposiumAuthor
    entrySymposiumAuthor = EntryWithPlaceholder(root, "多个姓名以英文逗号隔开")
    entrySymposiumAuthor.place(x=60,y=70,width=250,height=20)
    global labelSymposiumTitle
    labelSymposiumTitle = tkinter.Label(root,text='标   题：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelSymposiumTitle.place(x=9,y=100,width=50,height=20)
    global entrySymposiumTitle
    entrySymposiumTitle = EntryWithPlaceholder(root,"请输入论文标题")
    entrySymposiumTitle.place(x=60,y=100,width=250,height=20)
    global labelSymposiumName
    labelSymposiumName = tkinter.Label(root,text='论文集名：',justify=tkinter.RIGHT,width=150,fg='blue')
    labelSymposiumName.place(x=9,y=130,width=65,height=20)
    global entrySymposiumName
    entrySymposiumName = EntryWithPlaceholder(root, "请输入论文集名称")
    entrySymposiumName.place(x=75,y=130,width=235,height=20)
    global labelSymposiumPress
    labelSymposiumPress = tkinter.Label(root,text='出版机构：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelSymposiumPress.place(x=9,y=160,width=65,height=20)
    global entrySymposiumPress
    entrySymposiumPress = EntryWithPlaceholder(root,"出版机构名称")
    entrySymposiumPress.place(x=75,y=160,width=100,height=20)
    global labelSymposiumArea
    labelSymposiumArea = tkinter.Label(root,text='出版地区：',justify=tkinter.RIGHT,width=65,fg='blue')
    labelSymposiumArea.place(x=180,y=160,width=65,height=20)
    global entrySymposiumArea
    entrySymposiumArea = EntryWithPlaceholder(root,"机构所在地")
    entrySymposiumArea.place(x=245,y=160,width=65,height=20)
    global labelSymposiumPages
    labelSymposiumPages = tkinter.Label(root,text='起止页：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelSymposiumPages.place(x=9,y=190,width=50,height=20)
    global labelSymposium_Pages
    labelSymposium_Pages = tkinter.Label(root,text='~',justify=tkinter.RIGHT,width=10,fg='blue')
    labelSymposium_Pages.place(x=108,y=190,width=20,height=20)
    global entrySymposiumPages_1st
    entrySymposiumPages_1st = EntryWithPlaceholder(root,"起始页")
    entrySymposiumPages_1st.place(x=60,y=190,width=50,height=20)
    global entrySymposiumPages_2nd
    entrySymposiumPages_2nd = EntryWithPlaceholder(root,"终止页")
    entrySymposiumPages_2nd.place(x=125,y=190,width=50,height=20)
    global labelSymposiumYear
    labelSymposiumYear = tkinter.Label(root,text='出版年份：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelSymposiumYear.place(x=180,y=190,width=65,height=20)
    global entrySymposiumYear
    entrySymposiumYear = EntryWithPlaceholder(root,"出版的年份")
    entrySymposiumYear.place(x=245,y=190,width=65,height=20)
    global buttonSymposiumCreate
    buttonSymposiumCreate = tkinter.Button(root,text='生成参考文献格式',width=20,height=1,command=SymposiumCreate)
    buttonSymposiumCreate.place(x=90,y=220)
    global buttonSymposiumHelp
    buttonSymposiumHelp = tkinter.Button(root,text='?',width=3,height=1,command=SymposiumHelp)
    buttonSymposiumHelp.place(x=275,y=220)

def ReportEmpty():#清空报告[R]表单并恢复注释
    entryReportAuthor.delete(0,'end')
    entryReportTitle.delete(0,'end')
    entryReportArea.delete(0,'end')
    entryReportOrg.delete(0,'end')
    entryReportYear.delete(0,'end')
    
    entryReportAuthor.put_placeholder()
    entryReportTitle.put_placeholder()
    entryReportArea.put_placeholder()
    entryReportOrg.put_placeholder()
    entryReportYear.put_placeholder()

def ReportCreate():#生成报告[R]参考文献格式
    global result,AuthorName,Formatofcreate
    AuthorName=entryReportAuthor.get().split(',')#将作者按英文逗号分隔，写入列表
    Formatofcreate=0 #布尔变量判断格式是否正确，为1禁止输入
    
    if entryReportAuthor.get()=='多个姓名以英文逗号隔开' or entryReportAuthor.get()=='':
        #防止此时光标刚好停在文本框，而此时又没有数据写入，故有空字符串，下同理，不赘述
        tkinter.messagebox.showinfo(title='Error!',message='请输入作者名称！')
        Formatofcreate=1
    if entryReportTitle.get()=='请输入报告标题' or entryReportTitle.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入报告标题！')
        Formatofcreate=1
    if entryReportArea.get()=='请输入报告地区' or entryReportArea.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入报告地区！')
        Formatofcreate=1
    if entryReportOrg.get()=='请输入发表报告的单位' or entryReportOrg.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入发表报告的单位！')
        Formatofcreate=1
    if entryReportYear.get()=='报告年份，如2017' or entryReportYear.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入报告发表年份！')
        Formatofcreate=1

    AuthorNameinput()
    
    result+=entryReportTitle.get()+'[R].'
    result+=entryReportArea.get()+':'
    result+=entryReportOrg.get()+','
    result+=entryReportYear.get()+'.'
    
    if Formatofcreate==0:
        listboxRef.insert(tkinter.END,result)
    else:
        Formatofcreate=0

def ReportHelp():#帮助按钮
    Tips='电子报告与电子期刊文献表示方法类似，如：\n中华人民共和国国务院新闻办公室.国防白皮书:中国武装力量的多样化运用[R/OL].(2013-04-16)[2014-06-11].http://www.mod.gov.cn/affair/2013-04/16/content_442839.htm'
    tkinter.messagebox.showinfo(title='提示',message=Tips)

def Report():#报告[R]
    global labelReportLocation
    labelReportLocation = tkinter.Label(root,text='当前参考文献格式位置：报    告'
                                  ,justify=tkinter.RIGHT,width=150)
    labelReportLocation.place(x=15,y=40,width=180,height=20)
    global buttonReportEmpty
    buttonReportEmpty=tkinter.Button(root,text='清空表单',width=6,height=1,command=ReportEmpty)
    buttonReportEmpty.place(x=258,y=35)
    global labelReportAuthor
    labelReportAuthor = tkinter.Label(root,text='作   者：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelReportAuthor.place(x=9,y=70,width=50,height=20)
    global entryReportAuthor
    entryReportAuthor = EntryWithPlaceholder(root, "多个姓名以英文逗号隔开")
    entryReportAuthor.place(x=60,y=70,width=250,height=20)
    global labelReportTitle
    labelReportTitle = tkinter.Label(root,text='标   题：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelReportTitle.place(x=9,y=100,width=50,height=20)
    global entryReportTitle
    entryReportTitle = EntryWithPlaceholder(root,"请输入报告标题")
    entryReportTitle.place(x=60,y=100,width=250,height=20)
    global labelReportArea
    labelReportArea = tkinter.Label(root,text='报告地：',justify=tkinter.RIGHT,width=150,fg='blue')
    labelReportArea.place(x=10,y=130,width=50,height=20)
    global entryReportArea
    entryReportArea = EntryWithPlaceholder(root, "请输入报告地区")
    entryReportArea.place(x=60,y=130,width=250,height=20)
    global labelReportOrg
    labelReportOrg = tkinter.Label(root,text='主办单位：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelReportOrg.place(x=9,y=160,width=65,height=20)
    global entryReportOrg
    entryReportOrg = EntryWithPlaceholder(root,"请输入发表报告的单位")
    entryReportOrg.place(x=75,y=160,width=235,height=20)
    global labelReportYear
    labelReportYear = tkinter.Label(root,text='报告年份：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelReportYear.place(x=9,y=190,width=65,height=20)
    global entryReportYear
    entryReportYear = EntryWithPlaceholder(root,"报告年份，如2017")
    entryReportYear.place(x=75,y=190,width=235,height=20)
    global buttonReportCreate
    buttonReportCreate = tkinter.Button(root,text='生成参考文献格式',width=20,height=1,command=ReportCreate)
    buttonReportCreate.place(x=90,y=220)
    global buttonReportHelp
    buttonReportHelp = tkinter.Button(root,text='?',width=3,height=1,command=ReportHelp)
    buttonReportHelp.place(x=275,y=220)

def PatentEmpty():#清空专利文献[P]表单并恢复注释
    entryPatentAuthor.delete(0,'end')
    entryPatentTitle.delete(0,'end')
    entryPatentCoun.delete(0,'end')
    entryPatentNum.delete(0,'end')
    entryPatentDate.delete(0,'end')

    entryPatentAuthor.put_placeholder()
    entryPatentTitle.put_placeholder()
    entryPatentCoun.put_placeholder()
    entryPatentNum.put_placeholder()
    entryPatentDate.put_placeholder()

def PatentCreate():#生成专利文献[P]参考文献格式
    global result,AuthorName,Formatofcreate
    AuthorName=entryPatentAuthor.get().split(',')#将作者按英文逗号分隔，写入列表
    Formatofcreate=0 #布尔变量判断格式是否正确，为1禁止输入
    
    if entryPatentAuthor.get()=='多个专利所有者以英文逗号隔开' or entryPatentAuthor.get()=='':
        #防止此时光标刚好停在文本框，而此时又没有数据写入，故有空字符串，下同理，不赘述
        tkinter.messagebox.showinfo(title='Error!',message='请输入专利作者名称！')
        Formatofcreate=1
    if entryPatentTitle.get()=='请输入专利名称' or entryPatentTitle.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入专利名称！')
        Formatofcreate=1
    if entryPatentCoun.get()=='请输入专利申请地区/国家' or entryPatentCoun.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入专利申请地区/国家！')
        Formatofcreate=1
    if entryPatentNum.get()=='请输入专利号码' or entryPatentNum.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入专利号码！')
        Formatofcreate=1
    if entryPatentDate.get()=='请输入专利发布日期，格式：yyyy-mm-dd' or entryPatentDate.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入专利发布日期！')
        Formatofcreate=1

    AuthorNameinput()
    
    result+=entryPatentTitle.get()+':'
    result+=entryPatentNum.get()+'[P].'
    result+=entryPatentDate.get()+'.'
    
    if Formatofcreate==0:
        listboxRef.insert(tkinter.END,result)
    else:
        Formatofcreate=0

def PatentHelp():#帮助按钮
    Tips='电子专利文献与电子期刊论文文献参考文献格式类似，如：\nKOSEKI A, MOMOSE H, KAWAHITO M, et al. Compiler: US828402 [P/OL]. 2002-05-25[2002-05-28].http://ff&p=1&u=netahtml/PTO/search-bool.html&r=5&f=G&.l=50&col=AND&d=PG01&sl=IBM.AS.&OS=AN/IBM/RS=AN/IBM.'
    tkinter.messagebox.showinfo(title='提示',message=Tips)

def Patent():#专利文献[P]
    global labelPatentLocation
    labelPatentLocation = tkinter.Label(root,text='当前参考文献格式位置：专利文献'
                                  ,justify=tkinter.RIGHT,width=150)
    labelPatentLocation.place(x=15,y=40,width=180,height=20)
    global buttonPatentEmpty
    buttonPatentEmpty=tkinter.Button(root,text='清空表单',width=6,height=1,command=PatentEmpty)
    buttonPatentEmpty.place(x=258,y=35)
    global labelPatentAuthor
    labelPatentAuthor = tkinter.Label(root,text='专利所有者：',justify=tkinter.RIGHT,width=70,fg='blue')
    labelPatentAuthor.place(x=9,y=70,width=70,height=20)
    global entryPatentAuthor
    entryPatentAuthor = EntryWithPlaceholder(root, "多个专利所有者以英文逗号隔开")
    entryPatentAuthor.place(x=75,y=70,width=235,height=20)
    global labelPatentTitle
    labelPatentTitle = tkinter.Label(root,text='专利标题：',justify=tkinter.RIGHT,width=65,fg='blue')
    labelPatentTitle.place(x=9,y=100,width=65,height=20)
    global entryPatentTitle
    entryPatentTitle = EntryWithPlaceholder(root,"请输入专利名称")
    entryPatentTitle.place(x=75,y=100,width=235,height=20)
    global labelPatentCoun
    labelPatentCoun = tkinter.Label(root,text='专利国别：',justify=tkinter.RIGHT,width=65,fg='blue')
    labelPatentCoun.place(x=10,y=130,width=65,height=20)
    global entryPatentCoun
    entryPatentCoun = EntryWithPlaceholder(root, "请输入专利申请地区/国家")
    entryPatentCoun.place(x=75,y=130,width=235,height=20)
    global labelPatentNum
    labelPatentNum = tkinter.Label(root,text='专利号：',justify=tkinter.RIGHT,width=65,fg='blue')
    labelPatentNum.place(x=9,y=160,width=65,height=20)
    global entryPatentNum
    entryPatentNum = EntryWithPlaceholder(root,"请输入专利号码")
    entryPatentNum.place(x=75,y=160,width=235,height=20)
    global labelPatentDate
    labelPatentDate = tkinter.Label(root,text='发布日期：',justify=tkinter.RIGHT,width=65,fg='blue')
    labelPatentDate.place(x=9,y=190,width=65,height=20)
    global entryPatentDate
    entryPatentDate = EntryWithPlaceholder(root,"请输入专利发布日期，格式：yyyy-mm-dd")
    entryPatentDate.place(x=75,y=190,width=235,height=20)
    global buttonPatentCreate
    buttonPatentCreate = tkinter.Button(root,text='生成参考文献格式',width=20,height=1,command=PatentCreate)
    buttonPatentCreate.place(x=90,y=220)
    global buttonPatentHelp
    buttonPatentHelp = tkinter.Button(root,text='?',width=3,height=1,command=PatentHelp)
    buttonPatentHelp.place(x=275,y=220)

def StandardEmpty():#清空标准文献[S]表单并恢复注释
    entryStandardNum.delete(0,'end')
    entryStandardTitle.delete(0,'end')
    entryStandardArea.delete(0,'end')
    entryStandardAuthor.delete(0,'end')
    entryStandardYear.delete(0,'end')

    entryStandardNum.put_placeholder()
    entryStandardTitle.put_placeholder()
    entryStandardArea.put_placeholder()
    entryStandardAuthor.put_placeholder()
    entryStandardYear.put_placeholder()

def StandardCreate():#生成标准文献[S]参考文献格式
    global result,AuthorName,Formatofcreate
    Formatofcreate=0 #布尔变量判断格式是否正确，为1禁止输入
    
    if entryStandardNum.get()=='请输入标准代号' or entryStandardNum.get()=='':
        #防止此时光标刚好停在文本框，而此时又没有数据写入，故有空字符串，下同理，不赘述
        tkinter.messagebox.showinfo(title='Error!',message='请输入标准代号！')
        Formatofcreate=1
    if entryStandardTitle.get()=='请输入标准名称' or entryStandardTitle.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入标准名称！')
        Formatofcreate=1
    if entryStandardArea.get()=='请输入标准出版地区' or entryStandardArea.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入标准出版地区！')
        Formatofcreate=1
    if entryStandardYear.get()=='请输入标准出版年份' or entryStandardYear.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入标准出版年份！')
        Formatofcreate=1
    
    result=entryStandardTitle.get()+':'
    result+=entryStandardNum.get()+'[S].'
    result+=entryStandardArea.get()+':'
    result+=entryStandardYear.get()+'.'
    
    if Formatofcreate==0:
        listboxRef.insert(tkinter.END,result)
    else:
        Formatofcreate=0
        
def StandardHelp():#帮助按钮
    Tips='(1)有文献可考，2019年以后制定,起草标准,不再署名单位,个人。GB/T 7714-2015中推荐的表示方法如下所示：\n全国信息与文献标准化技术委员会文献著录:第4部分 非书资料:GB/T 3792.4-2009[S].北京:中国标准出版社,2010:3\n(2)电子标准文件与电子期刊文献参考文献格式类似，如：\n Information and documentation-the Dublin core metadata element set: ISO 15836: 2009 [S/OL].[2013-03-24].http://www.iso.org/iso/home/store/catalogue_tc/catalogue_detail.htm? csnumber=52142'
    tkinter.messagebox.showinfo(title='提示',message=Tips)
    
def Standard():#标准文献[S]
    global labelStandardLocation
    labelStandardLocation = tkinter.Label(root,text='当前参考文献格式位置：标    准'
                                  ,justify=tkinter.RIGHT,width=150)
    labelStandardLocation.place(x=15,y=40,width=180,height=20)
    global buttonStandardEmpty
    buttonStandardEmpty=tkinter.Button(root,text='清空表单',width=6,height=1,command=StandardEmpty)
    buttonStandardEmpty.place(x=258,y=35)
    global labelStandardNum
    labelStandardNum = tkinter.Label(root,text='标准代号：',justify=tkinter.RIGHT,width=65,fg='blue')
    labelStandardNum.place(x=10,y=70,width=65,height=20)
    global entryStandardNum
    entryStandardNum = EntryWithPlaceholder(root, "请输入标准代号")
    entryStandardNum.place(x=75,y=70,width=235,height=20)
    global labelStandardTitle
    labelStandardTitle = tkinter.Label(root,text='标准名称：',justify=tkinter.RIGHT,width=65,fg='blue')
    labelStandardTitle.place(x=10,y=100,width=65,height=20)
    global entryStandardTitle
    entryStandardTitle = EntryWithPlaceholder(root,"请输入标准名称")
    entryStandardTitle.place(x=75,y=100,width=235,height=20)
    global labelStandardArea
    labelStandardArea = tkinter.Label(root,text='出版地区：',justify=tkinter.RIGHT,width=65,fg='blue')
    labelStandardArea.place(x=10,y=130,width=65,height=20)
    global entryStandardArea
    entryStandardArea = EntryWithPlaceholder(root, "请输入标准出版地区")
    entryStandardArea.place(x=75,y=130,width=235,height=20)
    global labelStandardAuthor
    labelStandardAuthor = tkinter.Label(root,text='出版者：',justify=tkinter.RIGHT,width=65,fg='blue')
    labelStandardAuthor.place(x=9,y=160,width=65,height=20)
    global entryStandardAuthor
    entryStandardAuthor = EntryWithPlaceholder(root,"2019年起,制定,起草标准,不再署名单位,个人。")
    entryStandardAuthor.place(x=75,y=160,width=235,height=20)
    entryStandardAuthor['state']='disabled'
    global labelStandardYear
    labelStandardYear = tkinter.Label(root,text='出版年份：',justify=tkinter.RIGHT,width=65,fg='blue')
    labelStandardYear.place(x=9,y=190,width=65,height=20)
    global entryStandardYear
    entryStandardYear = EntryWithPlaceholder(root,"请输入标准出版年份，如2017")
    entryStandardYear.place(x=75,y=190,width=235,height=20)
    global buttonStandardCreate
    buttonStandardCreate = tkinter.Button(root,text='生成参考文献格式',width=20,height=1,command=StandardCreate)
    buttonStandardCreate.place(x=90,y=220)
    global buttonStandardHelp
    buttonStandardHelp = tkinter.Button(root,text='?',width=3,height=1,command=StandardHelp)
    buttonStandardHelp.place(x=275,y=220)

def NewspaperEmpty():#清空报纸析出文献[N]表单并恢复注释
    entryNewspaperAuthor.delete(0,'end')
    entryNewspaperTitle.delete(0,'end')
    entryNewspaperName.delete(0,'end')
    entryNewspaperDate.delete(0,'end')
    entryNewspaperLayout.delete(0,'end')
    
    entryNewspaperAuthor.put_placeholder()
    entryNewspaperTitle.put_placeholder()
    entryNewspaperName.put_placeholder()
    entryNewspaperDate.put_placeholder()
    entryNewspaperLayout.put_placeholder()

def NewspaperCreate():#生成报纸析出文献[N]参考文献格式
    global result,AuthorName,Formatofcreate
    AuthorName=entryNewspaperAuthor.get().split(',')#将作者按英文逗号分隔，写入列表
    Formatofcreate=0 #布尔变量判断格式是否正确，为1禁止输入
    
    if entryNewspaperAuthor.get()=='多个姓名以英文逗号隔开' or entryNewspaperAuthor.get()=='':
        #防止此时光标刚好停在文本框，而此时又没有数据写入，故有空字符串，下同理，不赘述
        tkinter.messagebox.showinfo(title='Error!',message='请输入作者名称！')
        Formatofcreate=1
    if entryNewspaperTitle.get()=='请输入文章标题' or entryNewspaperTitle.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入文章标题！')
        Formatofcreate=1
    if entryNewspaperName.get()=='请输入报纸名称' or entryNewspaperName.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入报纸名称！')
        Formatofcreate=1
    if entryNewspaperDate.get()=='请输入报纸日期，格式:yyyy-mm-dd' or entryNewspaperDate.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入报纸日期！')
        Formatofcreate=1
    if entryNewspaperLayout.get()=='请输入所在版面' or entryNewspaperLayout.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入所在版面！')
        Formatofcreate=1

    AuthorNameinput()
    
    result+=entryNewspaperTitle.get()+'[N].'
    result+=entryNewspaperName.get()+','
    result+=entryNewspaperDate.get()+'('
    result+=entryNewspaperLayout.get()+').'
    
    if Formatofcreate==0:
        listboxRef.insert(tkinter.END,result)
    else:
        Formatofcreate=0
        
def NewspaperHelp():#帮助按钮
    Tips='电子报纸参考文献格式与电子期刊类似，如：\n 刘裕国,杨柳,张洋,等.雾来袭，如何突围[N/OL].人民日报,2013-01-12[2013-11-06].http://paper.people.com.cn/rmrb/html/2013-01/12/nw.D110000renmrb_20130112_204.htm'
    tkinter.messagebox.showinfo(title='提示',message=Tips)

def Newspaper():#报纸析出文献[N]
    global labelNewspaperLocation
    labelNewspaperLocation = tkinter.Label(root,text='当前参考文献格式位置：报纸文章'
                                  ,justify=tkinter.RIGHT,width=150)
    labelNewspaperLocation.place(x=15,y=40,width=180,height=20)
    global buttonNewspaperEmpty
    buttonNewspaperEmpty=tkinter.Button(root,text='清空表单',width=6,height=1,command=NewspaperEmpty)
    buttonNewspaperEmpty.place(x=258,y=35)
    global labelNewspaperAuthor
    labelNewspaperAuthor = tkinter.Label(root,text='作   者：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelNewspaperAuthor.place(x=9,y=70,width=50,height=20)
    global entryNewspaperAuthor
    entryNewspaperAuthor = EntryWithPlaceholder(root, "多个姓名以英文逗号隔开")
    entryNewspaperAuthor.place(x=60,y=70,width=250,height=20)
    global labelNewspaperTitle
    labelNewspaperTitle = tkinter.Label(root,text='标   题：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelNewspaperTitle.place(x=9,y=100,width=50,height=20)
    global entryNewspaperTitle
    entryNewspaperTitle = EntryWithPlaceholder(root,"请输入文章标题")
    entryNewspaperTitle.place(x=60,y=100,width=250,height=20)
    global labelNewspaperName
    labelNewspaperName = tkinter.Label(root,text='报纸名称：',justify=tkinter.RIGHT,width=65,fg='blue')
    labelNewspaperName.place(x=10,y=130,width=65,height=20)
    global entryNewspaperName
    entryNewspaperName = EntryWithPlaceholder(root, "请输入报纸名称")
    entryNewspaperName.place(x=75,y=130,width=235,height=20)
    global labelNewspaperDate
    labelNewspaperDate = tkinter.Label(root,text='报纸日期：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelNewspaperDate.place(x=9,y=160,width=65,height=20)
    global entryNewspaperDate
    entryNewspaperDate = EntryWithPlaceholder(root,"请输入报纸日期，格式:yyyy-mm-dd")
    entryNewspaperDate.place(x=75,y=160,width=235,height=20)
    global labelNewspaperLayout
    labelNewspaperLayout = tkinter.Label(root,text='所在版面：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelNewspaperLayout.place(x=9,y=190,width=65,height=20)
    global entryNewspaperLayout
    entryNewspaperLayout = EntryWithPlaceholder(root,"请输入所在版面")
    entryNewspaperLayout.place(x=75,y=190,width=235,height=20)
    global buttonNewspaperCreate
    buttonNewspaperCreate = tkinter.Button(root,text='生成参考文献格式',width=20,height=1,command=NewspaperCreate)
    buttonNewspaperCreate.place(x=90,y=220)
    global buttonNewspaperHelp
    buttonNewspaperHelp = tkinter.Button(root,text='?',width=3,height=1,command=NewspaperHelp)
    buttonNewspaperHelp.place(x=275,y=220)

def EBOLEmpty():#清空电子文献[EB/OL]表单并恢复注释
    entryEBOLAuthor.delete(0,'end')
    entryEBOLTitle.delete(0,'end')
    entryEBOLAdd.delete(0,'end')
    entryEBOLDate.delete(0,'end')
    
    entryEBOLAuthor.put_placeholder()
    entryEBOLTitle.put_placeholder()
    entryEBOLAdd.put_placeholder()
    entryEBOLDate.put_placeholder()

def EBOLCreate():#生成电子文献[EB/OL]参考文献格式
    global result,AuthorName,Formatofcreate
    AuthorName=entryEBOLAuthor.get().split(',')#将作者按英文逗号分隔，写入列表
    Formatofcreate=0 #布尔变量判断格式是否正确，为1禁止输入
    
    if entryEBOLAuthor.get()=='多个姓名以英文逗号隔开' or entryEBOLAuthor.get()=='':
        #防止此时光标刚好停在文本框，而此时又没有数据写入，故有空字符串，下同理，不赘述
        tkinter.messagebox.showinfo(title='Error!',message='请输入作者名称！')
        Formatofcreate=1
    if entryEBOLTitle.get()=='请输入文章标题' or entryEBOLTitle.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入文章标题！')
        Formatofcreate=1
    if entryEBOLAdd.get()=='请输入详细的来源地址或网址' or entryEBOLAdd.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入详细的来源地址或网址！')
        Formatofcreate=1
    if entryEBOLDate.get()=='请输入出版日期，格式:yyyy-mm-dd' or entryEBOLDate.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入出版日期！')
        Formatofcreate=1

    AuthorNameinput()
    
    result+=entryEBOLTitle.get()+'[EB/OL].'
    result+=entryEBOLAdd.get()+','
    result+=entryEBOLDate.get()+'.'
    
    if Formatofcreate==0:
        listboxRef.insert(tkinter.END,result)
    else:
        Formatofcreate=0

def EBOLHelp():#帮助按钮
    Tips='网上期刊、联机网上数据库、磁带数据库、电子图书、光盘图书等电子资料请参照GB/T 7714-2015规定的电子文献引用规范或参考文献提供方的参考文献引文格式，此处由于数据冗杂不方便编写故略去，仅保留使用频次最多的网上电子公告或网址。\n'
    tkinter.messagebox.showinfo(title='提示',message=Tips)

def EBOL():#电子文献[EB/OL]
    global labelEBOLLocation
    labelEBOLLocation = tkinter.Label(root,text='当前参考文献格式位置：电子文献'
                                  ,justify=tkinter.RIGHT,width=150)
    labelEBOLLocation.place(x=15,y=40,width=180,height=20)
    global buttonEBOLEmpty
    buttonEBOLEmpty=tkinter.Button(root,text='清空表单',width=6,height=1,command=EBOLEmpty)
    buttonEBOLEmpty.place(x=258,y=35)
    global labelEBOLAuthor
    labelEBOLAuthor = tkinter.Label(root,text='作   者：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelEBOLAuthor.place(x=9,y=70,width=50,height=20)
    global entryEBOLAuthor
    entryEBOLAuthor = EntryWithPlaceholder(root, "多个姓名以英文逗号隔开")
    entryEBOLAuthor.place(x=60,y=70,width=250,height=20)
    global labelEBOLTitle
    labelEBOLTitle = tkinter.Label(root,text='标   题：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelEBOLTitle.place(x=9,y=100,width=50,height=20)
    global entryEBOLTitle
    entryEBOLTitle = EntryWithPlaceholder(root,"请输入文章标题")
    entryEBOLTitle.place(x=60,y=100,width=250,height=20)
    global labelEBOLAdd
    labelEBOLAdd = tkinter.Label(root,text='出处网址：',justify=tkinter.RIGHT,width=65,fg='blue')
    labelEBOLAdd.place(x=10,y=130,width=65,height=20)
    global entryEBOLAdd
    entryEBOLAdd = EntryWithPlaceholder(root, "请输入详细的来源地址或网址")
    entryEBOLAdd.place(x=75,y=130,width=235,height=20)
    global labelEBOLDate
    labelEBOLDate = tkinter.Label(root,text='出版日期：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelEBOLDate.place(x=9,y=160,width=65,height=20)
    global entryEBOLDate
    entryEBOLDate = EntryWithPlaceholder(root,"请输入出版日期，格式:yyyy-mm-dd")
    entryEBOLDate.place(x=75,y=160,width=235,height=20)
    global labelEBOLType
    labelEBOLType = tkinter.Label(root,text='文献类型：',justify=tkinter.RIGHT,width=50,fg='blue')
    labelEBOLType.place(x=9,y=190,width=65,height=20)
    global entryEBOLType
    entryEBOLType = EntryWithPlaceholder(root,"网上电子公告或网址[EB/OL]")
    entryEBOLType.place(x=75,y=190,width=235,height=20)
    entryEBOLType['state']='disabled'
    global buttonEBOLCreate
    buttonEBOLCreate = tkinter.Button(root,text='生成参考文献格式',width=20,height=1,command=EBOLCreate)
    buttonEBOLCreate.place(x=90,y=220)
    global buttonEBOLHelp
    buttonEBOLHelp = tkinter.Button(root,text='?',width=3,height=1,command=EBOLHelp)
    buttonEBOLHelp.place(x=275,y=220)

def OthersEmpty():#清空其他文献[Z]表单并恢复注释
    entryOthersAuthor.delete(0,'end')
    entryOthersTitle.delete(0,'end')
    entryOthersArea.delete(0,'end')
    entryOthersOrg.delete(0,'end')
    entryOthersYear.delete(0,'end')

    entryOthersAuthor.put_placeholder()
    entryOthersTitle.put_placeholder()
    entryOthersArea.put_placeholder()
    entryOthersOrg.put_placeholder()
    entryOthersYear.put_placeholder()

def OthersCreate():#生成其他文献[Z]参考文献格式
    global result,AuthorName,Formatofcreate
    AuthorName=entryOthersAuthor.get().split(',')#将作者按英文逗号分隔，写入列表
    Formatofcreate=0 #布尔变量判断格式是否正确，为1禁止输入
    
    if entryOthersAuthor.get()=='多个作者以英文逗号隔开' or entryOthersAuthor.get()=='':
        #防止此时光标刚好停在文本框，而此时又没有数据写入，故有空字符串，下同理，不赘述
        tkinter.messagebox.showinfo(title='Error!',message='请输入作者名称！')
        Formatofcreate=1
    if entryOthersTitle.get()=='请输入专利名称' or entryOthersTitle.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入专利名称！')
        Formatofcreate=1
    if entryOthersArea.get()=='请输入文章出版地区' or entryOthersArea.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入文章出版地区！')
        Formatofcreate=1
    if entryOthersOrg.get()=='请输入出版单位名称' or entryOthersOrg.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入出版单位名称！')
        Formatofcreate=1
    if entryOthersYear.get()=='请输入标准出版年份，如2017' or entryOthersYear.get()=='':
        tkinter.messagebox.showinfo(title='Error!',message='请输入标准出版年份！')
        Formatofcreate=1

    AuthorNameinput()
    
    result+=entryOthersTitle.get()+'[Z].'
    result+=entryOthersArea.get()+':'
    result+=entryOthersOrg.get()+','
    result+=entryOthersYear.get()+'.'
    
    if Formatofcreate==0:
        listboxRef.insert(tkinter.END,result)
    else:
        Formatofcreate=0

def OthersHelp():#帮助按钮
    Tips='这里没什么好提示的o∩_∩o，就给个范例吧~\n 范为民.1318例药品不良反应报告[Z].北京:天津市药品监督管理局,2018-2-18.32(1):51-53.'
    tkinter.messagebox.showinfo(title='提示',message=Tips)
    
def Others():#其他文献[Z]
    global labelOthersLocation
    labelOthersLocation = tkinter.Label(root,text='当前参考文献格式位置：其他文献'
                                  ,justify=tkinter.RIGHT,width=150)
    labelOthersLocation.place(x=15,y=40,width=180,height=20)
    global buttonOthersEmpty
    buttonOthersEmpty=tkinter.Button(root,text='清空表单',width=6,height=1,command=OthersEmpty)
    buttonOthersEmpty.place(x=258,y=35)
    global labelOthersAuthor
    labelOthersAuthor = tkinter.Label(root,text='主要作者：',justify=tkinter.RIGHT,width=65,fg='blue')
    labelOthersAuthor.place(x=10,y=70,width=65,height=20)
    global entryOthersAuthor
    entryOthersAuthor = EntryWithPlaceholder(root, "多个作者以英文逗号隔开")
    entryOthersAuthor.place(x=75,y=70,width=235,height=20)
    global labelOthersTitle
    labelOthersTitle = tkinter.Label(root,text='文章标题：',justify=tkinter.RIGHT,width=65,fg='blue')
    labelOthersTitle.place(x=10,y=100,width=65,height=20)
    global entryOthersTitle
    entryOthersTitle = EntryWithPlaceholder(root,"请输入文章标题")
    entryOthersTitle.place(x=75,y=100,width=235,height=20)
    global labelOthersArea
    labelOthersArea = tkinter.Label(root,text='出版地区：',justify=tkinter.RIGHT,width=65,fg='blue')
    labelOthersArea.place(x=10,y=130,width=65,height=20)
    global entryOthersArea
    entryOthersArea = EntryWithPlaceholder(root, "请输入文章出版地区")
    entryOthersArea.place(x=75,y=130,width=235,height=20)
    global labelOthersOrg
    labelOthersOrg = tkinter.Label(root,text='出版单位：',justify=tkinter.RIGHT,width=65,fg='blue')
    labelOthersOrg.place(x=9,y=160,width=65,height=20)
    global entryOthersOrg
    entryOthersOrg = EntryWithPlaceholder(root,"请输入出版单位名称")
    entryOthersOrg.place(x=75,y=160,width=235,height=20)
    global labelOthersYear
    labelOthersYear = tkinter.Label(root,text='出版年份：',justify=tkinter.RIGHT,width=65,fg='blue')
    labelOthersYear.place(x=9,y=190,width=65,height=20)
    global entryOthersYear
    entryOthersYear = EntryWithPlaceholder(root,"请输入标准出版年份，如2017")
    entryOthersYear.place(x=75,y=190,width=235,height=20)
    global buttonOthersCreate
    buttonOthersCreate = tkinter.Button(root,text='生成参考文献格式',width=20,height=1,command=OthersCreate)
    buttonOthersCreate.place(x=90,y=220)
    global buttonOthersHelp
    buttonOthersHelp = tkinter.Button(root,text='?',width=3,height=1,command=OthersHelp)
    buttonOthersHelp.place(x=275,y=220)

def deleteSelection():#将listbox中选中的数据删除掉
    selection = listboxRef.curselection()
    if not selection:
        tkinter.messagebox.showinfo(title='Information',message='No Selection!')
    else:
        l=len(selection)
        while(l>0):
            listboxRef.delete(selection[0])
            l-=1

def deleteall():#清空listbox
    if listboxRef.size()!=0:
        listboxRef.delete(0,'end')
    else:
        tkinter.messagebox.showinfo(title='提示',message='列表已经空了！')

def addToClipboard( string ):#保存表单到剪切板，与saveall配合使用
    from tkinter import Tk
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(string)
    r.update()
    r.destroy()
    
def saveall():#保存表单到剪切板，与addToClipboard配合使用
    if listboxRef.size()!=0:
        PrintContent=''
        for i in range(listboxRef.size()):
            PrintContent+='['+str(i+1)+']'+listboxRef.get(i)+'\n'
            addToClipboard(PrintContent)
        tkinter.messagebox.showinfo(title='提示',message='已复制到剪切板！')
    else:
        tkinter.messagebox.showinfo(title='提示',message='列表空！')
    
labelFormat = tkinter.Label(root,text='请选择参考文献格式类型：'
                            ,justify=tkinter.RIGHT,width=50)
labelFormat.place(x=10,y=5,width=150,height=20)

comboFormat = tkinter.ttk.Combobox(root,width=300)
comboFormat['value']=('期刊论文','图书/专著','学位论文/毕业论文',
                      '论文集','报告','专利文献','国际/国家标准','报纸文章',
                      '电子文献/网站网址','其他未说明的文献类型') #参考文献类型combobox候选项

comboFormat.current(0);#默认值0，Journal期刊论文
doallentry();forgetallentry();#全部做一遍，全部forget，此时内存存储所有表单，防止Entry重叠引起输入错误
Journal();#调用初始值Journal

comboFormat.place(x=160,y=5,width=150,height=20)

def comboChange(event):#如果combobox选项改变，那么将表单转成改变后对应的参考文献表单
    global ref_format
    ref_format=comboFormat.get()
    forgetallentry();
    if ref_format=='期刊论文':
        Journal();
    elif ref_format=='图书/专著':
        Monograph();
    elif ref_format=='学位论文/毕业论文':
        Dissertation();
    elif ref_format=='论文集':
        Symposium();
    elif ref_format=='报告':
        Report();
    elif ref_format=='专利文献':
        Patent();
    elif ref_format=='国际/国家标准':
        Standard();
    elif ref_format=='报纸文章':
        Newspaper();
    elif ref_format=='电子文献/网站网址':
        EBOL();
        EBOLHelp();
    elif ref_format=='其他未说明的文献类型':
        Others();
        
comboFormat.bind('<<ComboboxSelected>>',comboChange)#绑定combobox选择改变操作

labelList = tkinter.Label(root,text='参考文献格式列表：',justify=tkinter.RIGHT,width=110)
labelList.place(x=330,y=5,width=110,height=20)
listboxRef = tkinter.Listbox(root,width=400,selectmode=tkinter.EXTENDED)#添加参考文献格式列表combobox
listboxRef.place(x=340,y=30,width=400,height=225)

buttondeleteSelection = tkinter.Button(root,text='删除所选项',width=75,command=deleteSelection)
buttondeleteSelection.place(x=750,y=30,width=75,height=30)
buttondeleteall = tkinter.Button(root,text='清空列表',width=75,command=deleteall)
buttondeleteall.place(x=750,y=120,width=75,height=30)
buttonsaveall = tkinter.Button(root,text='导出列表',width=75,command=saveall)
buttonsaveall.place(x=750,y=220,width=75,height=30)

if __name__=="__main__":
    root.mainloop()

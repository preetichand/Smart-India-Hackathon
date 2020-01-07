import datetime
import sys  
sys.path.append('D:\Project Git Hub\Jarvis_Assistant\Jarvis')
from M2_VTTV.VTTV import text_voice as v
from M3_Pwriter.fwrite import file_op as fop
from M3_Pwriter.formatter import format as fw, dr_detail as dd
from M7_editor.texteditor import*
from M8_webSearch.web_Search import Gsearch_python as gp
from M4_Database.dbOperations import Database as db

class task:
    def execute(query):
        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            v.speak(f"Sir, the time is {strTime}")
            
        elif 'cription' in query:
            content=fw.set_format()
            fop.write_text(content)
            editor()
            db.Insert()
            
        elif 'my profile' in query:
            detail=dd.set_detail()
            fop.write_detail(detail)
            editor2()

        elif 'search' in query:
            v.speak("What can I search for you.")
            a = gp(v.takeCommand())
            a.Gsearch()
            
        else:
            v.speak("Sorry! I didn't get anything.")
            

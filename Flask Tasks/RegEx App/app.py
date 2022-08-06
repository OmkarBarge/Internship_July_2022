from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route('/',methods = ['GET','POST'])
def index_page():
    
    if request.method == 'POST':
        #Saving the data in Variable which is capture from Front End.
        reg_search = request.form['req_exp']  
        txt = request.form['txt']
       
       #Created empty list to save the index number of finds in string and send it to html page
        m_s = []
        m_e = []

        count = 0

        #this for loop run the regex on string and the save the index number in above empty list with help of function name start() and end(). 
        for match in re.finditer(reg_search, txt):
            count+=1
            ms = match.start()
            me = match.end()
            m_s.append(ms)
            m_e.append(me)

        #returning the index page and variables to index.html page.
        return render_template('index.html',count = count,m_s = m_s,m_e=m_e)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)




    